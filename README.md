# Projeto Agendador
🇧🇷
## Descrição
Projeto feito em Python utilizando **LangChain**, **Pydantic** e **Groq**.  
Permite que usuários marquem consultas com terapeutas através de um chatbot que interpreta e processa automaticamente as informações.

## Funcionamento

1. O usuário envia uma mensagem para o chatbot informando: **nome do terapeuta, data e horário** da consulta.  
2. O modelo interpreta a mensagem e, através de uma **String Output Parser**, cria três variáveis:  
   - `terapeuta`  
   - `data`  
   - `horario`  
3. O chatbot responde ao usuário confirmando as informações fornecidas.  
4. As variáveis extraídas são usadas para criar um **dicionário**, que é adicionado a uma lista.  
5. A lista completa é salva em um **arquivo JSON** (`agenda.json`), contendo todos os agendamentos realizados.

## Tecnologias utilizadas
- Python  
- LangChain  
- Pydantic  
- Groq (Llama 3.1)

## Observações
- Projeto modular: funções separadas para **chatbot**, **parser LLM** e **persistência em JSON**.  
- Fácil manutenção e futuras evoluções, como integração com WhatsApp ou múltiplos terapeutas.





# Scheduler Project
🇺🇸
## Description
Python project using **LangChain**, **Pydantic**, and **Groq**.  
Allows users to schedule appointments with therapists through a chatbot that interprets and processes the information automatically.

## How it works

1. The user sends a message to the chatbot with the **therapist's name, day, and time** of the appointment.  
2. The model interprets the message and, using a **String Output Parser**, generates three variables:  
   - `therapist`  
   - `day`  
   - `time`  
3. The chatbot responds to the user confirming the provided information.  
4. The extracted variables are used to create a **dictionary**, which is appended to a list.  
5. The complete list is saved in a **JSON file** (`agenda.json`), containing all scheduled appointments.

## Technologies used
- Python  
- LangChain  
- Pydantic  
- Groq (Llama 3.1)

## Notes
- Modular project: separate functions for **chatbot**, **LLM parser**, and **JSON persistence**.  
- Easy to maintain and ready for future expansions, such as WhatsApp integration or multiple therapists.
