# Projeto Agendador
🇧🇷

## Descrição
Projeto feito em Python utilizando LangChain, Pydantic, Groq e Google Calendar API.  
Permite que usuários marquem agendamentos com profissionais através de um chatbot que interpreta e processa automaticamente as informações, e cria eventos diretamente no Google Calendar do profissional.

## Funcionamento
1. O usuário envia uma mensagem para o chatbot informando: nome do profissional, data, horário da consulta, e seu próprio nome.  
2. O modelo interpreta a mensagem e, através de um String Output Parser, cria quatro variáveis:
   - profissional
   - data
   - horário
   - cliente
3. O chatbot verifica se o horário está disponível no calendário do profissional.  
4. Se disponível, cria o evento no Google Calendar e confirma a marcação ao usuário.  
5. As variáveis extraídas também são usadas para criar um dicionário, que é adicionado a uma lista.  
6. A lista completa é salva em um arquivo JSON (`agenda.json`), contendo todos os agendamentos realizados.

## Tecnologias utilizadas
- Python
- LangChain
- Pydantic
- Groq (Llama 3.1)
- Parser LLM
- Google Calendar API

### Detalhes da integração
O projeto utiliza a API do Google Calendar para:
- Verificar se o horário do profissional está ocupado (`freebusy`)  
- Criar eventos automaticamente no calendário do profissional  
- Garantir que não haja conflitos entre agendamentos

A utilização do parser LLM permite separar o processamento de linguagem da lógica de persistência e da lógica de calendário, tornando o projeto modular, testável e fácil de manter.

## Observações
- Projeto modular: funções separadas para chatbot, parser LLM, persistência em JSON e integração com Google Calendar.  
- Fácil manutenção e futuras evoluções, como integração com WhatsApp ou múltiplos profissionais.

---

# Scheduler Project
🇺🇸

## Description
Project built in Python using LangChain, Pydantic, Groq, and Google Calendar API.  
Allows users to schedule appointments with professionals through a chatbot that interprets and automatically processes the information, creating events directly in the professional's Google Calendar.

## How it works
1. The user sends a message to the chatbot providing: the professional's name, appointment date and time, and their own name.  
2. The model interprets the message and, using a String Output Parser, generates four variables:
   - professional
   - date
   - time
   - client
3. The chatbot checks if the time slot is available in the professional's calendar.  
4. If available, it creates the event in Google Calendar and confirms the appointment to the user.  
5. The extracted variables are also used to create a dictionary, which is appended to a list.  
6. The complete list is saved in a JSON file (`agenda.json`), containing all scheduled appointments.

## Technologies used
- Python
- LangChain
- Pydantic
- Groq (Llama 3.1)
- LLM Parser
- Google Calendar API

### Integration details
The project uses the Google Calendar API to:
- Check if the professional's time slot is busy (`freebusy`)  
- Automatically create events in the professional's calendar  
- Ensure there are no scheduling conflicts

Using the LLM parser separates language processing from data persistence and calendar logic, making the project modular, testable, and easy to maintain.

## Notes
- Modular project: separate functions for chatbot, LLM parser, JSON persistence, and Google Calendar integration.  
- Easy maintenance and ready for future expansions, such as WhatsApp integration or multiple professionals.
