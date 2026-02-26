import json 
import os 
def agendamento(terapeuta, data, horario): 
    formatacao = { 'terapeuta': terapeuta, 
        'data': data, 
        'horario': horario 
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

