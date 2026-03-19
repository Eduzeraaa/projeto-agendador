from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import timedelta, datetime

def autenticacao(): #autenticação
    SCOPES = ["https://www.googleapis.com/auth/calendar"]

    creds = service_account.Credentials.from_service_account_file(
        "credentials.json",
        scopes=SCOPES
    )
    service = build("calendar", "v3", credentials=creds)
    return service



def disponibilidade(horario, data, dono_calendario): #verificar disponibilidade do calendário
    formato_date = '%Y-%m-%d'
    formato_time = '%H:%M:%S'
    parsed_date = datetime.strptime(data, formato_date)
    parsed_time = datetime.strptime(horario, formato_time)
    end_time = parsed_time + timedelta(hours=1)
    busy = {
  "timeMin": f'{parsed_date.date()}T{parsed_time.time().isoformat()}-03:00',
  "timeMax": f'{parsed_date.date()}T{end_time.time().isoformat()}-03:00',
  "timeZone": 'America/Sao_Paulo',
  "items": [
    {
      "id": f'{dono_calendario}'
    }
  ]
}
    return busy



def criar_evento(cliente, data, horario, profissional, service): #criar evento se horário estiver disponível
    formato_date = '%Y-%m-%d'
    formato_time = '%H:%M:%S'
    parsed_date = datetime.strptime(data, formato_date)
    parsed_time = datetime.strptime(horario, formato_time)
    end_time = parsed_time + timedelta(hours=1)


    event = {
        'summary': f'Agendamento {cliente}',
        'description': f'{profissional}, você tem um agendamento com {cliente} às {parsed_time.time()}',
        'start': {
            'dateTime': f'{parsed_date.date()}T{parsed_time.time().isoformat()}',
            'timeZone': 'America/Sao_Paulo',
        },
        'end': {
            'dateTime': f'{parsed_date.date()}T{end_time.time().isoformat()}',
            'timeZone': 'America/Sao_Paulo'
        },
        'reminders':{
            'useDefault': False,
            'overrides': [
                {'method': 'popup', 'minutes': 0},
                {'method': 'popup', 'minutes': 15}
            ],
        },
    }
    
    if profissional == 'Francinei':
        dono_calendario = 'ea8e71587199978594185c52d4c51f225a130a2933f8f7e4a72203a8cab2553c@group.calendar.google.com'
    
        busy = disponibilidade(horario, data, dono_calendario)
        disp = service.freebusy().query(body=busy).execute()
        if disp['calendars'][dono_calendario]['busy']:
            return

        else:
            evento = service.events().insert(
        calendarId=f'{dono_calendario}',
        body=event
        ).execute()
        
        
        
    elif profissional == 'Mauro':
        dono_calendario = '4363821852a55eb92935ae7019dc03dd01596e4b9b74eecd3e9b6ae2eab2b89e@group.calendar.google.com'
        busy = disponibilidade(horario, data, dono_calendario)
        disp = service.freebusy().query(body=busy).execute()
        if disp['calendars'][dono_calendario]['busy']:
            return

        else:
            evento = service.events().insert(
        calendarId=f'{dono_calendario}',
        body=event
        ).execute()
            return evento
