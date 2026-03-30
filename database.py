from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

client = MongoClient(os.getenv("MONGODB_URI"))

db_terapeutas = client.horario_terapeutas
db_barbearia = client.horario_barbearia


def create_database(data, horario, telefone, cliente, profissional, profissao, event):

    dados = {
        'cliente': cliente,
        'data': data,
        'horario': horario,
        'profissional': profissional,
        'telefone': telefone,
        'status': 'agendado',
        'google_event_id': event['id']
    }
    if profissao == 'Terapeuta':
        db_terapeutas.agendamento.insert_one(dados)

    elif profissao == 'Barbeiro':
        db_barbearia.agendamento.insert_one(dados)

def buscar_agendamento(telefone, data, horario, profissional):
    if profissional == 'Francinei':
        return db_terapeutas.agendamento.find_one({
            'telefone': telefone,
            'data': data,
            'horario': horario,
            'status': 'agendado'
        })
    elif profissional == 'Mauro':
        return db_barbearia.agendamento.find_one({
            'telefone': telefone,
            'data': data,
            'horario': horario,
            'status': 'agendado'
        })
    

def desativar_agendamento_database(agendamento, profissional):
    if profissional == 'Francinei':
        db_terapeutas.agendamento.update_one(
            {'_id': agendamento['_id']},
            {'$set': {'status': 'cancelado'}}
        )
    elif profissional == 'Mauro':
        db_barbearia.agendamento.update_one(
            {'_id': agendamento['_id']},
            {'$set': {'status': 'cancelado'}}
        )

