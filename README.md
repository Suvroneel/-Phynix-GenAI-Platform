# Phynix: AI-Powered Mental Health Chatbot Platform (BERT + OLLAMA)

**🔗 Live Demo:** [https://phynix.streamlit.app/](https://phynix.streamlit.app/)



Phynix is an **end-to-end AI mental health platform** designed to provide users a secure and interactive environment to express emotions, track mental well-being, and receive personalized guidance. The heart of the system is **Ashva**, now enhanced with **BERT for emotion detection** and **OLLAMA for smoother, context-aware responses**, creating a hybrid GenAI workflow for improved conversational support.



This platform is **multi-page**, **multi-layered**, and production-ready, combining a sophisticated frontend, AI/NLP backend, and relational database analytics.

---

## Table of Contents

- [Overview](#overview)  
- [Page Descriptions](#page-descriptions)  
  - [Login & Signup Page](#login--signup-page)  
  - [Chat Page](#chat-page)  
  - [Home Page](#home-page)  
  - [Mood Journal Page](#mood-journal-page)  
- [Backend Architecture](#backend-architecture)  
- [AI & NLP Layer](#ai--nlp-layer)  
- [Frontend & UX Design](#frontend--ux-design)  
- [Technologies Used](#technologies-used)  
- [Deployment](#deployment)  
- [Future Enhancements](#future-enhancements)  

---

## Overview

Phynix serves as a **digital mental health companion**, combining:  

- **Hybrid Conversational AI**: Emotion detection via BERT, response generation via OLLAMA for fluent and empathetic interactions.  
- **Analytics & Dashboards**: Track emotional trends, risk levels, and confidence metrics over time.  
- **Private Journaling**: Secure mood journaling for personal reflection.  

The platform emphasizes **privacy, data security, and actionable insights**, offering a mental refuge for individuals dealing with stress, anxiety, or depression.

---

## Page Descriptions

### Login & Signup Page

**Purpose:** Provides secure user authentication, account creation, and session management to access the Phynix platform.

![Login](https://github.com/Suvroneel/Phynix-Mental-Health-Chatbot/blob/Suvroneel-patch-1/Site%20Images/Login.png)

![Signup](https://github.com/Suvroneel/Phynix-Mental-Health-Chatbot/blob/Suvroneel-patch-1/Site%20Images/Signup.png)

**Key Features & Technical Details:**

- **Login:** Users authenticate via Supabase; session tokens stored securely.  
- **Signup:** Collects username, email, password; validates input; stores credentials in PostgreSQL.  
- **UI & UX:** Tab-based, responsive forms with inline error messages and validation feedback.  
- **Workflow:** Login → session storage → Chat page; Signup → email verification → Chat page.

---

### Chat Page

**Purpose:** Core interaction interface with Ashva, enabling users to express emotions and receive context-aware, empathetic support.

![Chat](https://github.com/Suvroneel/Phynix-Mental-Health-Chatbot/blob/a4c386cbf01e77109956934c15b14f8402244c04/Site%20Images/Phynix_Chat_Interface_UI.png)

**Key Features & Technical Details:**  
- **Dynamic Chat Interface:**  
  - Styled chat bubbles for user and bot messages.  
  - Maintains history via `st.session_state` for session persistence.  
- **Emotion & Risk Analysis:**  
  - BERT predicts one of seven emotions; OLLAMA generates context-aware responses.  
  - Risk levels and confidence scores calculated and displayed with emoji indicators.  
- **Database Integration:**  
  - Supabase/PostgreSQL stores messages, predicted emotions, risk, confidence, and bot replies.  
- **UX Enhancements:**  
  - Collapsible analysis block after each message.  
  - “New Chat” button resets conversation safely.

---

### Home Page

**Purpose:** Central dashboard offering insights, metrics, and daily motivational guidance.

![Home1](https://github.com/Suvroneel/Phynix-Mental-Health-Chatbot/blob/6d5cd83a7bfa73ad670949ac791646df8c842ced/Site%20Images/Home_1.png)  
![Home2](https://github.com/Suvroneel/Phynix-Mental-Health-Chatbot/blob/6d5cd83a7bfa73ad670949ac791646df8c842ced/Site%20Images/Home_2.png)

**Key Features & Technical Details:**  
- Dashboard charts for emotion trends, confidence levels, and risk progression.  
- Personalized advice and motivational quotes.  
- Session-safe retrieval ensures consistent metrics across pages.  

---

### Mood Journal Page

**Purpose:** Private journaling space for users to log reflections and track emotional well-being.

![Mood Journal](https://github.com/Suvroneel/Phynix-Mental-Health-Chatbot/blob/6d5cd83a7bfa73ad670949ac791646df8c842ced/Site%20Images/Mood_journal.png)

**Key Features & Technical Details:**  
- Profile management with editable bio and verified badge.  
- Secure, private journal entries per user.  
- Authentication enforced via Supabase tokens.  
- Streamlit column layout with custom CSS for cards and buttons.

---

## Backend Architecture

- **Supabase Authentication:** Manages login/signup with secure token-based sessions.  
- **PostgreSQL Data Layer:** Stores `user_data` (messages, emotions, risk, confidence, replies), mood journal entries, and profile info.  
- **Data Flow:**  
  1. User input → Streamlit frontend  
  2. BERT predicts emotion → OLLAMA generates response  
  3. Messages and analytics stored in PostgreSQL  
  4. Dashboard retrieves metrics dynamically

---

## AI & NLP Layer

- **BERT-based Emotion Classification:** Classifies input into seven emotion categories.  
- **OLLAMA Response Generation:** Produces fluent, empathetic responses based on context and emotion.  
- **Structured Outputs:** JSON schemas with deduplication and validation.  
- **Integration:** Predictions triggered on message submission and rendered in chat UI.

---

## Frontend & UX Design

- **Streamlit Multi-Page App:** Chat, Home, Mood Journal.  
- **Dynamic UI Elements:** Chat bubbles, collapsible analysis, progress charts, motivational quotes.  
- **Custom CSS Styling:** Buttons, cards, animations.  
- **Responsive Layout:** Multi-column design for dashboards and profile pages.

---

## Technologies Used

- **Frontend:** Streamlit, HTML/CSS  
- **Backend:** Supabase, PostgreSQL  
- **Machine Learning:** Python, BERT (emotion classification), OLLAMA (response generation)  
- **Visualization:** Streamlit charts, custom progress bars

---

## Deployment

- **Streamlit Cloud** or local deployment via:  
```bash

streamlit run  Logout.py
```
### Future Enhancements

Databricks / MLflow logging for experiments

Documentation & code cleanup

Optional Dockerization & batch endpoints for production

Advanced multi-agent GenAI workflows for enriched conversational experience
