import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import MessagesPlaceholder, ChatPromptTemplate

load_dotenv() #carregar key do .env

#modelo da resposta normal
model = ChatGroq(
    api_key=os.environ.get('GROQ_API_KEY'), #pegar GROQ_API_KEY do .env
    model_name = 'llama-3.1-8b-instant'
)

system_prompt = '''Você é um assistente com respostas resumidas, objetivas e diretas.
Um usuário terá que pedir para marcar uma terapia. Pegue o nome do terapeuta, data, e horário com o usuário. Esses 3 são obrigatórios. 
Caso falte algum, peça pro usuário falar o que falta.
Observação: a data será dada em dia da semana (segunda, terça...). Se o usuário colocar a data em números, diga-o para falar em dia da semana.
Observação 2: O horário deve ser colocado como relógio convencional (19:30, 11:00). Se o usuário colocar apenas as horas, assuma que os minutos serão 00
(Usuário: 19 horas -> Horário: 19:00)'''

# resposta normal pro user
def resposta_chatbot(pergunta, model, mensagens):
    msgs = [
        ('system', system_prompt),
        MessagesPlaceholder('history'),
        ('user', '{pergunta}')
    ]

    prompt = ChatPromptTemplate.from_messages(msgs)
    chain = prompt | model

    resposta = chain.invoke({
        'history': mensagens,
        'pergunta': pergunta
    })

    return resposta.content

