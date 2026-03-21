import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from parser_llm import parse_agendamento
from calendar_service import autenticacao, disponibilidade, criar_evento
from datetime import datetime

load_dotenv()  # carregar key do .env

# inicializar modelo
model = ChatGroq(
    api_key=os.environ.get('GROQ_API_KEY'),
    model_name='llama-3.1-8b-instant'
)

system_prompt = '''Você é um assistente com respostas resumidas, objetivas e diretas.
Um cliente terá que pedir para marcar um agendamento. Pegue a data e o horário do agendamento com ele.
Observação: você pegará a data que o cliente enviou (deve conter dia, mês e ano), e transformar no modelo americano yyyy-mm-dd (com hífen).
Observação 2: O horário deve ser colocado como relógio convencional (19:30, 11:00) COM SEGUNDOS. Se o cliente colocar apenas as horas, assuma que os minutos serão 00,
e os segundos sempre serão 00.
(Usuário: 19 horas -> Horário: 19:00:00)
Não precisa ficar se relembrando que o usuário enviou tudo, nem pedir confirmação. Se ele enviou tudo que é necessário, apenas encerre a conversa educadamente.
Ex de resposta: Olá (nome do cliente), prazer em atendê-lo. O agendamento está marcado com a (nome do profissional) para o dia (DD/MM/YYYY) às (HH/MM/SS). Obrigado!
Importante: é proibido tentar adivinhar o nome do cliente, nem a data ou horário. Pegue exatamente o que ele enviar, e formate do jeito que foi pedido.
Se data for uma string "..." ou horário for uma string "...", significa que o cliente não enviou a data ou horário, respectivamente.'''
mensagens = []  # histórico de conversa

service = autenticacao()  # autenticação




# ===================== Integração do Streamlit =========================

st.title('Agendador de horários')

cliente = st.text_input("Insira seu nome e aperte enter:", key="name")

f'Olá, {st.session_state.name}! Seja bem-vindo ao nosso sistema de agendamento. Por favor, escolha um profissional e informe a data e horário desejados para o seu agendamento.'

st.warning("⚠️ Não nos responsabilizamos por qualquer problema externo dos agendamentos automatizados. Verifique seus dados antes de enviar a mensagem. Quando for inserir data na mensagem, insira DIA, MÊS E ANO. Exemplo: quero marcar no dia 20/08/2026 às 19:30.")

df = pd.DataFrame({ #! Botão que escolhe o profissional
    'Profissionais': ['Francinei', 'Mauro'],
    })

profissional = st.selectbox(
    'Com quem você quer agendar?',
     df['Profissionais'])

'Você quer agendar com: ', profissional



if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if "confirmar" not in st.session_state: #! variável de controle para mostrar a mensagem de confirmação apenas uma vez
    st.session_state.confirmar = False

if "dados" not in st.session_state: #! variável de controle para mostrar a mensagem de dados faltando apenas uma vez
    st.session_state.dados = None

if "clicado" not in st.session_state: #! variável de controle para limpar a mensagem de confirmação após clicar no botão de confirmação
    st.session_state.clicado = False

if "contexto" not in st.session_state: #! variável de controle para contextualizar a conversa, armazenando data e horário do agendamento para usar na mensagem de confirmação
    st.session_state.contexto = {
        "data": None,
        "horario": None
    }




if prompt := st.chat_input("Digite data e horário desejados para agendamento: "):
    mensagem = st.chat_message("user").markdown(prompt) #! mensagem do usuário
    st.session_state.messages.append({"role": "user", "content": prompt})

    if not cliente or cliente.strip() == "":
        st.warning("⚠️ Por favor, insira seu nome antes de continuar.")
        st.stop()

    st.session_state.confirmar = False #! botao de confirmacao nao aparecerá 
    

    try:
        # parse do agendamento
        obj_agendamento = parse_agendamento(prompt)
        data = obj_agendamento.data
        horario = obj_agendamento.horario

        #! completar com a memória de contexto, caso o cliente não envie a data ou horário na mensagem atual, mas tenha enviado em mensagens anteriores.
        if data == "...":
            data = st.session_state.contexto["data"]

        if horario == "...":
            horario = st.session_state.contexto["horario"]

        #! atualizar memória de contexto, caso o cliente tenha enviado a data ou horário na mensagem atual.
        if data != "...":
            st.session_state.contexto["data"] = data

        if horario != "...":
            st.session_state.contexto["horario"] = horario


        dados = { #! dicionário para passar os dados necessários para criar o evento no calendário
            'data': data,
            'horario': horario,
            'cliente': cliente,
            'profissional': profissional
        }


        st.session_state.dados = dados



        if horario == "..." or data == "...":
            resposta = f'Desculpe {cliente}, algumas informações estão faltando para realizar o agendamento. Por favor, envie a mensagem novamente seguindo as instruções fornecidas acima.'
            st.chat_message("assistant").markdown(resposta)
            st.session_state.messages.append({"role": "assistant", "content": resposta})
            st.session_state.confirmar = False #! não mostrar botão de confirmação, pq os dados estão incompletos

        else: #! dados completos. proximo passo: verificar se data é passada ou futura, e se o horário está disponível no calendário do profissional escolhido

            if data < datetime.now().date().isoformat(): #! verificar se a data é passada, comparando com a data atual
                resposta = f"Desculpe {cliente}, não é possível agendar para uma data passada. Por favor, escolha uma data futura."
                st.chat_message("assistant").markdown(resposta)
                st.session_state.messages.append({"role": "assistant", "content": resposta})
                st.session_state.confirmar = False #! não mostrar botão de confirmação, pq é uma data passada

            else: #! data é futura. proximo passo: verificar disponibilidade do horário no calendário do profissional escolhido

                # definir dono do calendário
                if profissional == 'Francinei':
                    dono_calendario = 'ea8e71587199978594185c52d4c51f225a130a2933f8f7e4a72203a8cab2553c@group.calendar.google.com'
                elif profissional == 'Mauro':
                    dono_calendario = '4363821852a55eb92935ae7019dc03dd01596e4b9b74eecd3e9b6ae2eab2b89e@group.calendar.google.com'

                busy = disponibilidade(horario, data, dono_calendario)
                verificar_disponivel = service.freebusy().query(body=busy).execute()

                if verificar_disponivel['calendars'][dono_calendario]['busy']: # horario ocupado
                    horarios_disponiveis = []
                    formato_time = '%H:%M:%S'


                    for hora in range(8, 18): #! cria uma lista de horários disponíveis, testando da hora 8 até a hora 18 (horário comercial simulado)
                        if hora < 10:
                            hora = f'0{hora}'
                        horario_teste = datetime.strptime(f'{hora}:00:00', formato_time).time()
                        busy_teste = disponibilidade(horario_teste.isoformat(), data, dono_calendario)
                        disp_teste = service.freebusy().query(body=busy_teste).execute()
                        if not disp_teste['calendars'][dono_calendario]['busy']:
                            horario_livre = f'{hora}:00'
                        horarios_disponiveis.append(horario_livre)
                        horarios_disponiveis = list(dict.fromkeys(horarios_disponiveis))


                    if not horarios_disponiveis: #! autoexplicativo
                        resposta = f"Desculpe {cliente}, não há horários disponíveis para o dia {data}. Por favor, escolha outra data."
                        st.chat_message("assistant").markdown(resposta)

                        st.session_state.confirmar = False #! não mostrar botão de confirmação, pq o horário escolhido não está disponível
                    
                    resposta = f"Desculpe {cliente}, esse horário não está disponível. Os horários disponíveis para o dia que você escolheu são: {', '.join(horarios_disponiveis)}. Por favor, escolha um desses horários."
                    
                    
                    

                else: #horario disponível
                    resposta = f'Você quer agendar com {profissional} para o dia {data} às {horario}. Por favor, confirme seu agendamento clicando no botão abaixo.'

                    st.session_state.confirmar = True #! mostrar botão de confirmação, pq os dados estão completos e o horário está disponível

                st.chat_message("assistant").markdown(resposta)
                st.session_state.messages.append({"role": "assistant", "content": resposta})

                mensagens.append(('user', mensagem))
                mensagens.append(('assistant', resposta))
        

    except Exception as e:
        resposta = f'Desculpe {cliente}, ocorreu um erro ao processar seu pedido. Por favor, envie a mensagem novamente seguindo as instruções fornecidas acima.'
        st.error(f'Erro: {e}')
        st.chat_message("assistant").markdown(resposta)
        st.session_state.messages.append({"role": "assistant", "content": resposta})
        st.session_state.confirmar = False #! não mostrar botão de confirmação, pq ocorreu um erro e os dados podem estar incompletos ou mal inseridos


if st.session_state.confirmar and not st.session_state.clicado: #! botão de confirmação só aparece se os dados estiverem completos e o horário estiver disponível
    try:
        if st.button('Confirmar agendamento'):
            dados = st.session_state.dados
            st.session_state.clicado = True #! para não criar o evento mais de uma vez, caso o usuário clique mais de uma vez no botão de confirmação
            criar_evento(dados['cliente'], dados['data'], dados['horario'], dados['profissional'], service)
            resposta = f'Agendamento confirmado! Obrigado e até a próxima, {cliente}!'



            st.chat_message("assistant").markdown(resposta)
            st.session_state.messages.append({"role": "assistant", "content": resposta})

            st.session_state.confirmar = False #! resetar variável de controle para não mostrar a mensagem de confirmação novamente
            st.session_state.dados = None #! resetar dados do agendamento

            st.rerun() #! para sumir o botão de confirmação e a mensagem de confirmação após clicar no botão

            


    except Exception as e:
        resposta = f'Desculpe {cliente}, ocorreu um erro ao confirmar seu agendamento. Por favor, tente novamente.'
        st.error(f'Erro: {e}')
        st.chat_message("assistant").markdown(resposta)
        st.session_state.messages.append({"role": "assistant", "content": resposta})
