# 🇧🇷 Agendador de Horários Automatizado

## 📌 Descrição
O **Agendador de Horários Automatizado** é um sistema inteligente que permite aos clientes marcar consultas com profissionais de forma simples, rápida e conversacional.

Utilizando **LLM (Groq)**, o sistema interpreta mensagens em linguagem natural, valida informações e realiza agendamentos automaticamente no **Google Calendar**.

Ideal para consultórios, prestadores de serviço e profissionais que desejam automatizar sua agenda com mais eficiência e menos esforço manual.

---

## ⚙️ Funcionalidades
- Seleção do profissional via interface interativa  
- Inserção do nome do cliente  
- Agendamento via chat em linguagem natural  
- Validação de dados (evita datas passadas e entradas inválidas)  
- Tratamento de erros da LLM (evita falhas no sistema)  
- Verificação de disponibilidade no Google Calendar  
- Sugestão automática de horários alternativos quando há conflito  
- Confirmação antes de criar o agendamento  
- Memória de contexto (permite continuar a conversa mesmo com mensagens incompletas)  
- Histórico de mensagens durante a sessão  

---

## 🧠 Diferenciais
- Interação natural com o usuário (sem formulários rígidos)  
- Sistema resiliente a erros de entrada  
- Fluxo conversacional inteligente  
- Experiência próxima a um chatbot real de produção  

---

## 🛠️ Tecnologias
- **Python + Streamlit** → backend e interface web  
- **Groq LLM** (`langchain-groq`) → interpretação de mensagens  
- **Google Calendar API** → verificação de disponibilidade e criação de eventos  

---

## 🚀 Próximos Passos
- Integração com autenticação via Google OAuth  
- Suporte a múltiplos profissionais com contas próprias  
- Personalização de horários (expediente e intervalos)  
- Deploy com domínio personalizado  

---

# 🇺🇸 Automated Scheduling System

## 📌 Description
The **Automated Scheduling System** is an intelligent solution that allows clients to book appointments with professionals through a conversational interface.

Using a **Groq LLM**, the system understands natural language, validates inputs, and automatically creates events in **Google Calendar**.

---

## ⚙️ Features
- Professional selection via interactive interface  
- Customer name input  
- Chat-based scheduling using natural language  
- Data validation (prevents past dates and invalid inputs)  
- LLM error handling (prevents system crashes)  
- Google Calendar availability checking  
- Automatic suggestion of alternative time slots  
- Confirmation before booking  
- Context memory (handles incomplete follow-up messages)  
- Chat history during session  

---

## 🧠 Highlights
- Natural interaction (no rigid forms)  
- Robust error handling  
- Intelligent conversational flow  
- Production-like chatbot experience  

---

## 🛠️ Technologies
- **Python + Streamlit** → backend and web interface  
- **Groq LLM** (`langchain-groq`) → message interpretation  
- **Google Calendar API** → availability and event creation  

---

## 🚀 Next Steps
- Google OAuth integration  
- Multi-user (multi-professional) support  
- Custom working hours and availability  
- Custom domain deployment  
