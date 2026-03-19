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
Um cliente terá que pedir para marcar um agendamento. Pegue a data e o horário do agendamento com ele.
Observação: você pegará a data que o cliente enviou (deve conter dia, mês e ano), e transformar no modelo americano yyyy-mm-dd (com hífen).
Observação 2: O horário deve ser colocado como relógio convencional (19:30, 11:00) COM SEGUNDOS. Se o cliente colocar apenas as horas, assuma que os minutos serão 00,
e os segundos sempre serão 00.
(Usuário: 19 horas -> Horário: 19:00:00)
Não precisa ficar se relembrando que o usuário enviou tudo, nem pedir confirmação. Se ele enviou tudo que é necessário, apenas encerre a conversa educadamente.
Ex de resposta: Olá (nome do cliente), prazer em atendê-lo. O agendamento está marcado com a (nome do profissional) para o dia (DD/MM/YYYY) às (HH/MM/SS). Obrigado!'''

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
