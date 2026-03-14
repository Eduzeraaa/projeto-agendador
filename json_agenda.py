import json 
import os 
def agendamento(profissional, data, horario, cliente): 
    formatacao = { 'profissional': profissional, 
        'data': data, 
        'horario': horario,
        'cliente': cliente
    } 
    
    if os.path.exists('agenda.json'): 
        with open('agenda.json', 'r', encoding='utf-8') as arquivo: 
            dados = json.load(arquivo) 
            
    else: 
        dados = [] 
        
    dados.append(formatacao) 
    
    with open ('agenda.json', 'w', encoding='utf-8') as arquivo: 
        json.dump(dados, arquivo, ensure_ascii=False, indent=4) 
        
    return arquivo 
