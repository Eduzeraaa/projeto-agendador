import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from json_agenda import agendamento
from parser_llm import parse_agendamento
from chatbot_module import resposta_chatbot
from calendar_service import autenticacao, disponibilidade, criar_evento

load_dotenv()  # carregar key do .env

# inicializar modelo
model = ChatGroq(
    api_key=os.environ.get('GROQ_API_KEY'),
    model_name='llama-3.1-8b-instant'
)

system_prompt = '''Você é um assistente com respostas resumidas, objetivas e diretas.
Um cliente terá que pedir para marcar um agendamento. Pegue o nome do profissional (com quem ele quer marcar), data, horário e nome do cliente. Esses 4 são obrigatórios. 
Caso falte algum, peça pro cliente falar o que falta.
Observação: você pegará a data que o cliente enviou (deve conter dia, mês e ano), e transformar no modelo americano yyyy-mm-dd (com hífen).
Observação 2: O horário deve ser colocado como relógio convencional (19:30, 11:00) COM SEGUNDOS. Se o cliente colocar apenas as horas, assuma que os minutos serão 00,
e os segundos sempre serão 00.
(Usuário: 19 horas -> Horário: 19:00:00)
Não precisa ficar se relembrando que o usuário enviou tudo, nem pedir confirmação.'''

mensagens = []  # histórico de conversa

service = autenticacao()  # autenticação

while True:
    pergunta = input("User (digite 'x' para sair): ")
    if pergunta.lower() == 'x':
        print("Desligando...")
        break

    # parse do agendamento
    obj_agendamento = parse_agendamento(pergunta)
    cliente = obj_agendamento.cliente
    data = obj_agendamento.data
    horario = obj_agendamento.horario
    profissional = obj_agendamento.profissional

    # definir dono do calendário
    if profissional == 'Francinei':
        dono_calendario = 'ea8e71587199978594185c52d4c51f225a130a2933f8f7e4a72203a8cab2553c@group.calendar.google.com'
    elif profissional == 'Mauro':
        dono_calendario = '4363821852a55eb92935ae7019dc03dd01596e4b9b74eecd3e9b6ae2eab2b89e@group.calendar.google.com'
    else:
        print("Profissional não cadastrado.")
        continue

    # checar disponibilidade
    busy = disponibilidade(horario, data, dono_calendario)
    disp = service.freebusy().query(body=busy).execute()

    if disp['calendars'][dono_calendario]['busy']: # horario ocupado
        resposta = f"Desculpe {cliente}, o horário solicitado para {profissional} está ocupado. Por favor, escolha outro horário."

    else: #horario disponível
        criar_evento(cliente, data, horario, profissional, service)
        resposta = f"Olá {cliente}, prazer em atendê-lo. O agendamento está marcado com {profissional} para o dia {data} às {horario}. Obrigado!"

        # salvar no json
        agendamento(
            obj_agendamento.profissional,
            obj_agendamento.data,
            obj_agendamento.horario,
            obj_agendamento.cliente
        )

    # enviar resposta do chatbot
    print(f"Chatbot: {resposta}")

    # atualizar histórico
    mensagens.append(('user', pergunta))
    mensagens.append(('assistant', resposta))
