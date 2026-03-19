# 🇧🇷 Agendador de Horários Automatizado

## Descrição
O **Agendador de Horários Automatizado** é um sistema que permite aos clientes marcar consultas ou horários com profissionais de forma simples e rápida via chat web.  
Ele integra **Streamlit**, **Google Calendar API** e uma **LLM (Groq)** para interpretar mensagens e criar eventos automaticamente.

O sistema é ideal para pequenos consultórios, serviços de atendimento ou qualquer cenário em que profissionais precisem de agendamentos automatizados e organizados.

---

## Funcionalidades
- Escolha do profissional via menu interativo.  
- Inserção do nome do cliente.  
- Agendamento via chat: basta enviar data e horário.  
- Criação automática de eventos no Google Calendar.  
- Chat mantém histórico durante a sessão.  
- Aviso de responsabilidade para garantir que o usuário insira **dia, mês e ano** corretamente.  

---

## Tecnologias
- **Python + Streamlit** → backend e interface web.  
- **Groq LLM** via `langchain-groq` → interpretação de mensagens e extração de dados do agendamento.  
- **Google Calendar API** → criação de eventos

---

# 🇺🇸 Automated Scheduling System

## Description
The **Automated Scheduling System** allows clients to quickly book appointments with professionals via web chat.  
It integrates **Streamlit**, **Google Calendar API**, and **LLM (Groq)** to automatically create events.

## Features
- Professional selection via interactive dropdown  
- Customer name input  
- Booking via chat by sending date and time  
- Automatic Google Calendar event creation  
- Chat history maintained during the session  
- Disclaimer to ensure correct **day, month, and year** input  

## Technologies
- **Python + Streamlit** → backend and web interface  
- **Groq LLM** via `langchain-groq` → message interpretation  
- **Google Calendar API** → event creation
