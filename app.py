import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from json_agenda import agendamento
from parser_llm import parse_agendamento
from chatbot_module import resposta_chatbot
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
Ex de resposta: Olá (nome do cliente), prazer em atendê-lo. O agendamento está marcado com a (nome do profissional) para o dia (DD/MM/YYYY) às (HH/MM/SS). Obrigado!'''

mensagens = []  # histórico de conversa

service = autenticacao()  # autenticação




# ===================== Integração do Streamlit =========================

st.title('Agendador de horários')

cliente = st.text_input("Insira seu nome:", key="name")

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



text_box = st.container(height=290) #! text box do chat

if prompt := st.chat_input("Digite data e horário desejados para agendamento: "): 
    mensagem = text_box.chat_message("user").markdown(prompt) #! mensagem do usuário
    st.session_state.messages.append({"role": "user", "content": prompt})

    # parse do agendamento
    obj_agendamento = parse_agendamento(prompt)
    data = obj_agendamento.data
    horario = obj_agendamento.horario

    # definir dono do calendário
    if profissional == 'Francinei':
        dono_calendario = 'ea8e71587199978594185c52d4c51f225a130a2933f8f7e4a72203a8cab2553c@group.calendar.google.com'
    elif profissional == 'Mauro':
        dono_calendario = '4363821852a55eb92935ae7019dc03dd01596e4b9b74eecd3e9b6ae2eab2b89e@group.calendar.google.com'

    busy = disponibilidade(horario, data, dono_calendario)
    disp = service.freebusy().query(body=busy).execute()

    if disp['calendars'][dono_calendario]['busy']: # horario ocupado
        resposta = f"Desculpe {cliente}, o horário solicitado para {profissional} está ocupado. Por favor, escolha outro horário."

    else: #horario disponível
        criar_evento(cliente, data, horario, profissional, service)
        resposta = f"Olá {cliente}, prazer em atendê-lo. O agendamento está marcado com {profissional} para o dia {data} às {horario}. Obrigado!"


    text_box.chat_message("assistant").markdown(resposta)
    st.session_state.messages.append({"role": "assistant", "content": resposta})

    mensagens.append(('user', mensagem))
    mensagens.append(('assistant', resposta))




