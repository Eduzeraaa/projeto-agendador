import os
from langchain_groq import ChatGroq
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()

class Saida_esperada(BaseModel):
    data: str = Field(description='Data agendada, modelo americano: yyyy-mm-dd. Se o usuário não informar a data, assuma que data = "..."')
    horario: str = Field(description='Horário agendado, desta forma: HH:MM:SS. Se o usuário não informar o horário, assuma que horario = "..."')


# cria o modelo só pro output parser
model = ChatGroq(
    api_key=os.environ.get('GROQ_API_KEY'),
    model_name='llama-3.1-8b-instant'
)

llm_estruturada = model.with_structured_output(Saida_esperada)

def parse_agendamento(pergunta):
    return llm_estruturada.invoke(pergunta)
