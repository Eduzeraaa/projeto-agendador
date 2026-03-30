# 🇧🇷 Sistema de Agendamento Inteligente

## 📌 Descrição
O **Sistema de Agendamento Inteligente** é uma aplicação full-stack que automatiza o processo de marcação e cancelamento de horários com profissionais, utilizando linguagem natural.

O sistema combina **LLM (Groq)**, **Google Calendar API** e **MongoDB**, permitindo que usuários interajam como se estivessem conversando com um atendente real.

A aplicação interpreta mensagens, valida informações, gerencia disponibilidade em tempo real e sincroniza tudo entre banco de dados e calendário.

---

## ⚙️ Funcionalidades
- Seleção de profissional via interface (Streamlit)
- Agendamento via linguagem natural (chat)
- Cancelamento de agendamentos via chat
- Integração com Google Calendar em tempo real
- Verificação automática de disponibilidade
- Sugestão de horários alternativos
- Persistência de dados em MongoDB
- Atualização de status (agendado / cancelado)
- Validação de datas e horários
- Memória de contexto na conversa
- Histórico de mensagens na sessão

---

## 🧠 Diferenciais Técnicos
- Sistema conversacional com LLM (Groq)
- Sincronização entre banco de dados e Google Calendar
- Fluxo completo de CRUD de agendamentos (Create / Read / Update / Delete)
- Tratamento de inconsistências de dados entre serviços
- Arquitetura orientada a fluxo real de produção

---

## 🏗️ Arquitetura
Fluxo principal:

1. Usuário envia mensagem
2. LLM extrai data, horário e telefone
3. Sistema valida dados e disponibilidade
4. Criação do evento no Google Calendar
5. Persistência no MongoDB com `google_event_id`
6. Para cancelamento:
   - Busca no MongoDB
   - Remove evento do Google Calendar
   - Atualiza status no banco

---

## 🛠️ Tecnologias
- **Python**
- **Streamlit**
- **MongoDB (Atlas)**
- **Google Calendar API**
- **Groq LLM (Llama 3 via LangChain)**
- **Pydantic**

---

## 🧪 Aprendizados do Projeto
- Integração de APIs externas (Google Calendar)
- Manipulação de banco NoSQL (MongoDB)
- Construção de fluxos conversacionais com LLM
- Tratamento de estados em aplicações reais
- Sincronização de dados entre múltiplos sistemas

---

## 🚀 Próximos Passos
- Autenticação de usuários (Google OAuth)
- Painel administrativo para profissionais
- Multi-tenant (cada profissional com sua agenda isolada)
- Deploy em produção (Streamlit Cloud / Render)
- Sistema de notificações (WhatsApp ou e-mail)

---

# 🇺🇸 Smart Scheduling System

## 📌 Description
The **Smart Scheduling System** is a full-stack application that automates appointment booking and cancellation using natural language.

It integrates **Groq LLM**, **Google Calendar API**, and **MongoDB** to provide a real conversational scheduling experience.

The system processes user messages, validates availability, and keeps both database and calendar fully synchronized.

---

## ⚙️ Features
- Professional selection via UI
- Chat-based appointment scheduling
- Chat-based cancellation system
- Real-time Google Calendar integration
- Automatic availability checking
- Alternative time suggestions
- MongoDB persistence layer
- Appointment status tracking (scheduled / canceled)
- Context memory handling
- Session chat history

---

## 🧠 Technical Highlights
- LLM-powered conversational interface
- Full synchronization between database and calendar
- Complete CRUD workflow for appointments
- Robust multi-service data consistency handling
- Production-like architecture design

---

## 🏗️ Architecture Flow
1. User sends message
2. LLM extracts structured data
3. System validates input and availability
4. Event is created in Google Calendar
5. Data is stored in MongoDB with `google_event_id`
6. Cancellation flow:
   - Search in MongoDB
   - Delete event in Google Calendar
   - Update status in database

---

## 🛠️ Technologies
- Python
- Streamlit
- MongoDB Atlas
- Google Calendar API
- Groq LLM (Llama 3 via LangChain)
- Pydantic

---

## 🧪 Key Learnings
- API integration at production level
- NoSQL data modeling with MongoDB
- LLM-based conversational systems
- State management in real applications
- Multi-system data synchronization

---

## 🚀 Next Steps
- Google OAuth authentication
- Admin dashboard for professionals
- Multi-tenant architecture
- Production deployment
- Notification system (WhatsApp / Email)
