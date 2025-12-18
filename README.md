# Phynix: AI-Powered Mental Health Chatbot Platform

Phynix is an **end-to-end AI mental health platform** designed to provide users a secure and interactive environment to express emotions, track mental well-being, and receive personalized guidance. The heart of the system is **Ashva**, a BERT-powered chatbot that predicts user emotions, evaluates risk and confidence levels, and provides supportive responses.  

This platform is **multi-page**, **multi-layered**, and production-ready, combining a sophisticated frontend, AI/NLP backend, and relational database analytics.

---

## Table of Contents

- [Overview](#overview)  
- [Page Descriptions](#page-descriptions)  
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

- **Conversational AI** with real-time emotion recognition  
- **Analytics & dashboards** to visualize emotional trends, confidence, and risk levels  
- **Private journaling** for personal reflection  

The platform emphasizes **privacy, data security, and actionable insights**, offering a mental refuge for individuals dealing with stress, anxiety, or depression.

---

## Page Descriptions

### Chat Page

**Purpose:** Core interaction interface with Ashva, enabling users to express emotions and receive context-aware support.  

**Key Features & Technical Details:**  
- **Dynamic Chat Interface:**  
  - User and bot messages rendered in styled chat bubbles using custom CSS.  
  - Message history maintained via `st.session_state` for session persistence.  
- **Emotion & Risk Analysis:**  
  - User inputs processed by a BERT-based model predicting one of seven emotions.  
  - Risk levels and confidence scores calculated and displayed with emoji indicators.  
- **Database Integration:**  
  - Supabase/PostgreSQL tables (`user_data`) store messages, predicted emotions, risk, confidence, and chatbot replies.  
  - Session-safe insertion with error handling and API-level validations.  
- **Session Management:**  
  - Authentication via Supabase tokens (`access_token` / `refresh_token`).  
  - Graceful redirection to login/logout pages for invalid or expired sessions.  
- **UX Enhancements:**  
  - Dynamic greeting for first-time chat or empty history.  
  - Analysis collapsible block showing emotion and risk after each message.  
  - “New Chat” button resets conversation safely without losing authentication context.  

---

### Home Page

**Purpose:** Central dashboard offering insights, metrics, and daily motivational guidance.  

**Key Features & Technical Details:**  
- **Dashboard & Metrics:**  
  - Charts displaying emotion trends, confidence levels, and risk progression using historical chat data.  
  - Pulls analytics from PostgreSQL for personalized insights.  
- **Daily Advice / Motivation:**  
  - Randomized motivational quotes displayed with custom CSS styling.  
  - Ashva insights provide context-specific recommendations based on past interactions.  
- **Navigation & Interaction:**  
  - “Begin Your Journey” button links to Chat page for immediate interaction.  
  - Session-safe retrieval of messages ensures metrics remain consistent across pages.  
- **UX Enhancements:**  
  - Animated welcome messages, styled quote boxes, and responsive multi-column layout.  
  - Centralized, visually prominent calls-to-action to encourage engagement.

---

### Mood Journal Page

**Purpose:** Private and secure journaling space for users to log reflections and track emotional well-being.  

**Key Features & Technical Details:**  
- **Profile Management:**  
  - Displays user profile image, verified badge, username, and editable bio.  
  - Profile edits and bio updates saved in PostgreSQL.  
- **Journal Entries:**  
  - Secure private entries maintained per user.  
  - New entry button (under development) for structured diary input.  
- **Session & Security:**  
  - Authentication enforced via Supabase tokens.  
  - User session isolation ensures only authorized access to private entries.  
- **UX Enhancements:**  
  - Streamlit column layout for profile image, actions, and journal sections.  
  - Custom CSS for image styling, buttons, and card-like UI components.

---

## Backend Architecture

- **Supabase Authentication:**  
  - Manages user login/signup with secure token-based sessions.  
  - PostgreSQL stores `user_credentials` table with emails and usernames.  

- **PostgreSQL Data Layer:**  
  - `user_data` table tracks chat messages, predicted emotions, risk, confidence, and Ashva replies.  
  - Separate tables for mood journal entries, profile information, and historical analytics.  
  - Designed for multi-user scalability and secure storage.  

- **Data Flow:**  
  1. User input → Streamlit frontend  
  2. Emotion predicted via BERT model → Ashva response generated  
  3. Messages, emotions, and analytics stored in PostgreSQL via Supabase API  
  4. Dashboard metrics and advice dynamically retrieved from backend  

---

## AI & NLP Layer

- **BERT-based Emotion Classification:**  
  - Input text classified into one of seven emotions.  
  - Optimized for conversational sentiment analysis.  

- **Ashva Response Logic:**  
  - Responses generated dynamically based on predicted emotion and context.  
  - Risk and confidence levels computed from predicted emotion category.  

- **Integration:**  
  - Prediction triggered on message submission.  
  - Results saved in PostgreSQL and rendered dynamically in the chat UI.  

---

## Frontend & UX Design

- **Streamlit Multi-Page App:** Chat, Home, Mood Journal.  
- **Dynamic UI Elements:** Chat bubbles, collapsible analysis, progress charts, motivational quotes.  
- **Custom CSS Styling:** Buttons, chat bubbles, cards, animation effects.  
- **Responsive Layout:** Multi-column design for dashboards and profile pages.  

---

## Technologies Used

- **Frontend:** Streamlit, HTML/CSS for custom UI  
- **Backend:** Supabase, PostgreSQL  
- **Machine Learning:** Python, BERT (emotion classification)  
- **Visualization:** Streamlit charts, custom progress bars  

---

## Deployment

- **Streamlit Cloud** or **local deployment** via:  
```bash
streamlit run Chat.py

