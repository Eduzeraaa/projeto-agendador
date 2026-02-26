import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from json_agenda import agendamento
from parser_llm import parse_agendamento
from chatbot_module import resposta_chatbot



load_dotenv() #carregar key do .env

model = ChatGroq(
    api_key=os.environ.get('GROQ_API_KEY'), #pegar GROQ_API_KEY do .env
    model_name = 'llama-3.1-8b-instant'
)

system_prompt = '''Você é um assistente com respostas resumidas, objetivas e diretas.
Um usuário terá que pedir para marcar uma terapia. Pegue o nome do terapeuta, data, e horário com o usuário. Esses 3 são obrigatórios. 
Caso falte algum, peça pro usuário falar o que falta.
Observação: a data será dada em dia da semana (segunda, terça...). Se o usuário colocar a data em números, diga-o para falar em dia da semana.
Observação 2: O horário deve ser colocado como relógio convencional (19:30, 11:00). Se o usuário colocar apenas as horas, assuma que os minutos serão 00
(Usuário: 19 horas -> Horário: 19:00)
Não se preocupe se o usuário não colocar uma data específica. Apenas confirme.'''


mensagens = []  #histórico de conversa será armazenado nessa lista

while True:
    pergunta = input("User (digite 'x' para sair): ")
    if pergunta.lower() == 'x':
        print("Desligando...")
        break

    # resposta normal pro user
    resposta = resposta_chatbot(pergunta, model, mensagens)
    print(f"Chatbot: {resposta}")

    # output parser, que transformará algumas palavras em variáveis
    obj_agendamento = parse_agendamento(pergunta)  # retorna terapeuta, data, horario

    # salvar no json
    agendamento(
        obj_agendamento.terapeuta,
        obj_agendamento.data,
        obj_agendamento.horario
    )

    print(f"Agendamento confirmado: {obj_agendamento.terapeuta} dia {obj_agendamento.data} às {obj_agendamento.horario}")

    # atualiza  o histórico de mensagens
    mensagens.append(('user', pergunta))
    mensagens.append(('assistant', resposta))
