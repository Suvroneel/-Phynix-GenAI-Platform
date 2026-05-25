# Phynix Ai

> *The more you talk to it, the more it becomes YOURS.*

Most AI talks at you. Phynix grows with you. It remembers how you felt last session, notices your patterns over time, and meets you where you actually are instead of starting from zero every single time.


**🔗 Live Demo:** https://phynix.streamlit.app/

Phynix is an **end-to-end mood-aware GenAI platform** designed to give users a personalised AI experience that genuinely evolves with them. The heart of the system is **Ashva**, an intelligent companion powered by **BERT for emotion detection** and **Llama** for empathetic, context-aware conversations.

This platform is **multi-page**, **multi-layered**, and production-ready, combining a sophisticated frontend, hybrid AI/NLP backend, and relational database analytics.

---

## 🆕 Recent Updates

### v2.2 - RAG Memory Engine + pgvector - April 2026
Ashva now actually remembers you. Not just your last emotion, but real context from both your past conversations and diary entries. Built a unified RAG pipeline using pgvector on a PostgreSQL base with sentence-transformers for semantic embeddings. Every chat message and diary entry gets embedded and stored in a vector store. When you return, Ashva retrieves the most semantically relevant memories across both sources and uses them to generate a genuinely personal welcome, powered by the LLM. The more you talk and write, the more Ashva actually knows you. Falls back to emotion-based greeting if no embeddings exist yet, and a generic welcome for brand new users. This is what "the more you talk to it, the more it becomes YOURS" actually means under the hood.

### v2.1.1 - Ashva Diaries (Mood Journal) - March 2026
Replaced the static placeholder with a fully functional journaling feature. Users can write daily reflections, optionally attach an image, and view today's entries as timestamped cards. Entries are stored securely with images handled via cloud storage buckets. Fresh slate every day at midnight IST. Built with privacy-first design, no mood tagging, no sentiment analysis, just open reflection.

### v2.0 - GenAI Backend - February 2026
Replaced static hard-coded responses with a live GenAI backend. Ashva now generates dynamic, context-aware empathetic responses using Llama via Hugging Face Inference API.

---

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
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

Phynix serves as a **mood-aware GenAI platform**, combining:

- **Hybrid Conversational AI**: Emotion classification via fine-tuned BERT, coupled with Llama for fluid, empathetic dialogue
- **Analytics & Dashboards**: Track emotional trends, risk levels, and confidence metrics over time
- **Private Journaling**: Secure daily journaling that feeds into the RAG memory pool

The platform emphasises **personalisation, privacy, and genuine contextual awareness** over generic AI responses.

---

## 📁 Project Structure

```

Phynix-Mental-Health-Chatbot/
├── Logout.py                        # Main entry point & authentication
├── requirements.txt                 # Python dependencies
├── Dockerfile                       # Docker configuration
├── README.md                        # Documentation
├── .gitignore                       # Git ignore rules
├── .gitattributes                   # Git attributes
├── history.png                      # Project history image
│
├── pages/                           # Streamlit pages
│   ├── 1_Chat.py                    # Chat interface with Ashva
│   ├── 2_Home.py                    # Analytics dashboard
│   └── 3_Mood Journal.py            # Mood journaling
│
├── Utils/                           # Core utilities
│   ├── ashva.py                     # AI orchestration
│   ├── model.py                     # BERT emotion classification
│   ├── gen_ai.py                    # Generative AI integration
│   ├── database.py                  # Database operations
│   ├── config.py                    # Configuration
│   ├── reply.py                     # Response generation
│   ├── emotion_responses.py         # Emotion templates
│   ├── advice.py                    # Advice generation
│   ├── personality.py               # AI personality
│   ├── profile.py                   # User profiles
│   ├── Progression_Chart.py         # Analytics charts
│   ├── sidebar.py                   # Sidebar components
│   ├── footer.py                    # Footer components
│   ├── title.py                     # Title utilities
│   ├── Website_Title.py             # Title config
│   ├── Otp_verification.py         # OTP system
│   ├── Automated_Messages.py        # Auto messages
│   ├── feedback.py                  # Feedback system
│   ├── journal.py                   # Mood journal logic
│   └── **init**.py
│
├── auth/                            # Authentication
│   └── google_login_migration/
│       ├── Logout.py
│       └── README.md
│
├── SQL/                             # Database schemas
│   └── user_data_rows.sql
│
├── Functions/                       # Helper functions
│   └── title.py
│
├── images/                          # Static assets
│   ├── default.png
│   ├── logo-black&white.png
│   ├── sigmund-ljJDx95-6gE-unsplash.png
│   ├── icons/                       # Favicons
│   └── profiles/                    # Profile avatars
│
├── Lottie/                          # Animations
│   └── Animation - 1750949119838.json
│
├── favicon_io/                      # Favicon files
│
├── Site Images/                     # Screenshots
│
├── Old versions/                    # Legacy code
│
└── .idea/                           # IDE config

```

---

## Page Descriptions

### Login & Signup Page

**Purpose:** Provides secure user authentication, account creation, and session management to access the Phynix platform.

![Login](Site%20Images/Login.png)
![Signup](Site%20Images/Signup.png)

**Key Features & Technical Details:**

- **Login:** Users authenticate via secure tokens; session tokens stored securely
- **Signup:** Collects username, email, password; validates input; stores credentials in PostgreSQL data layer
- **UI & UX:** Tab-based, responsive forms with inline error messages and validation feedback
- **Workflow:** Login -> session storage -> Chat page; Signup -> email verification -> Chat page

---

### Chat Page

**Purpose:** Core interaction interface with Ashva, enabling users to express emotions and receive context-aware, empathetic support powered by Generative AI.

![Chat](https://github.com/Suvroneel/Phynix-GenAI-Platform/blob/Suvroneel-patch-1/Site%20Images/Phynix_Genai_Chat.png?raw=true)

**Key Features & Technical Details:**

- **Dynamic Chat Interface:**
  - Styled chat bubbles for user and bot messages with smooth animations
  - Maintains conversation history via session state for contextual responses
  - Typing indicators and real-time response generation
  
- **Emotion & Risk Analysis:**
  - Fine-tuned BERT transformer model classifies user input into seven emotion categories
  - Llama generates contextually appropriate, empathetic responses based on detected emotion
  - Risk levels and confidence scores calculated and displayed with emoji indicators
  - Collapsible analysis section showing emotion breakdown and risk assessment
  
- **Database Integration:**
  - Backend database stores complete conversation history safely
  - Tracks messages, predicted emotions, risk levels, confidence scores, and AI-generated replies
  - Historical data powers analytics dashboard
  
- **UX Enhancements:**
  - "New Chat" button with safe conversation reset
  - Real-time responses with character-by-character display

---

### Home Page

**Purpose:** Central dashboard offering insights, metrics, and daily motivational guidance.

![Home1](Site%20Images/Home_1.png)
![Home2](Site%20Images/Home_2.png)

**Key Features & Technical Details:**

- Interactive dashboard charts for emotion trends, confidence levels, and risk progression
- Personalized advice based on longitudinal emotional patterns
- Daily motivational quotes and tips
- Session-safe data retrieval ensures consistent metrics across pages
- Visual analytics powered by historical conversation data

---

### Mood Journal Page

**Purpose:** A private space for daily reflection, write freely, attach a photo, and let your thoughts exist without judgment.

![Mood Journal](https://github.com/Suvroneel/Phynix-GenAI-Platform/blob/Suvroneel-patch-1/Site%20Images/Ashva_diary.png)

**Key Features & Technical Details:**

- **Ashva Diaries** -- open text journaling with optional image attachment
- Fresh slate every day at midnight IST -- no clutter from previous days
- Entries stored securely in relational tables with multi-modal assets routed to private cloud buckets
- Timestamped cards displaying today's reflections
- Clear button to wipe today's view without deleting data
- Privacy-first -- no mood tagging, no sentiment analysis, no judgment
- Profile management with editable bio and verified badge
- Authentication enforced via secure session tokens

---

## Backend Architecture

- **Secure Authentication:** Token-based secure session management with refresh capabilities
- **PostgreSQL Data Layer:** 
  - Relational schemas handle secure credential verification, long-term state mapping, and private diary entries asynchronously
  - Dedicated storage bucket pipeline handles image uploads seamlessly
  
- **AI Inference Pipeline:**
  1. User input -> Streamlit frontend
  2. BERT emotion classification model predicts emotional state in real time
  3. Context-aware RAG search pulls historical context markers via pgvector similarity matching
  4. Llama generates fluid, empathetic response backed by the extracted context
  5. Risk assessment logic calculates safety metrics dynamically
  6. All data persisted to PostgreSQL for analytical tracking and trend visualization

---

## AI & NLP Layer

### Emotion Classification (BERT)
- **Fine-tuned BERT model** optimized for real-time sequence classification
- Classifies user messages into **seven emotion categories**:
  - Joy, Sadness, Anger, Fear, Surprise, Disgust, Neutral
- Provides **confidence scores** for each prediction loop
- **Risk level assessment** calculated programmatically based on detected emotions and intensity metrics
- Real-time inference with sub-second response times

### Generative AI Response System
Phynix uses **Llama** via the **Hugging Face Inference API** for all AI-generated responses.

- **Fast, general-purpose conversational AI**
- **Excellent instruction-following capabilities**
- **Strong context understanding across multi-turn conversations**
- **Emotion-aware prompting** -- responses are tailored to the user's detected emotional state

### AI Integration Features
- **Context-aware responses** -- full conversation history maintained for coherent dialogue
- **Temperature control** -- adjustable creativity from factual (0.0) to creative (1.0)
- **Token length management** -- configurable response lengths
- **Emotion-based prompting** -- AI responses tailored directly to detected emotional state
- **Fallback handling** -- graceful error management with user-friendly messages

### Technical Implementation Workflow

```

1. User message -> BERT emotion detection
2. Spatial vector search (pgvector) returns top-ranked emotional context matches
3. Emotion label + historical memories + conversation history -> Llama
4. AI generates empathetic, context-aware response
5. Response stored cleanly with metadata (emotion, risk, confidence)

```

---

## Frontend & UX Design

- **Streamlit Multi-Page App:** 
  - Chat interface with AI-powered responses
  - Analytics dashboard (Home)
  - Private mood journaling
  
- **Dynamic UI Elements:** 
  - Chat bubbles with smooth typing animations
  - Collapsible analysis sections
  - Interactive progress charts and metrics
  - Motivational quotes and daily guidance
  
- **Custom CSS Styling:** 
  - Gradient buttons with hover effects
  - Professional card layouts with shadows
  - Responsive typography (Inter font)
  - Consistent color scheme and branding
  
- **Responsive Layout:** 
  - Multi-column design for dashboards
  - Mobile-friendly interface
  - Optimized for various screen sizes

---

## Technologies Used

### Frontend
- **Streamlit** - Interactive web application framework
- **HTML/CSS** - Custom styling and responsive layouts
- **JavaScript** - Enhanced interactivity

### Backend
- **PostgreSQL / pgvector** - Relational data storage, analytics, and semantic vector similarity search
- **Python** - Core application logic

### Machine Learning & AI
- **BERT (Transformers)** - Sequence classification for emotion mapping
- **Hugging Face Inference API** - Llama GenAI backend
- **Sentence-Transformers** - Text embeddings pipeline for semantic memory
- **PyTorch / TensorFlow** - Deep learning frameworks

### Data & Analytics
- **Pandas** - Data manipulation and analysis
- **Streamlit Charts** - Interactive visualizations
- **Custom Analytics** - Longitudinal emotion trends and risk tracking

---

## Deployment

### Local Development
```bash
# Clone repository
git clone [https://github.com/Suvroneel/Phynix-Mental-Health-Chatbot.git](https://github.com/Suvroneel/Phynix-Mental-Health-Chatbot.git)
cd Phynix-Mental-Health-Chatbot

# Install dependencies
pip install -r requirements.txt

# Run application
streamlit run Logout.py

```

### Production Deployment

* **Platform:** Streamlit Community Cloud
* **Environment Configuration:**
* Environment keys and database credentials stored securely via production secrets
* Optional Hugging Face API token for enhanced rate limits


* **Continuous Deployment:** Auto-deploy from GitHub repository
* **Scalability:** Serverless architecture with automatic scaling

---

## Future Enhancements

* [ ] **Advanced AI Features**
* Multi-agent conversation systems
* Specialized therapeutic approaches (CBT, DBT)
* Voice interaction capabilities
* Real-time crisis detection with emergency routing


* [ ] **Analytics & ML**
* Databricks / MLflow integration for experiment tracking
* Predictive mood insights
* Personalized intervention recommendations
* Advanced sentiment analysis with multi-dimensional metrics


* [ ] **Platform Expansion**
* Multi-language support (10+ languages)
* Mobile app (iOS/Android)
* Therapist collaboration portal
* Integration with wearables for holistic health tracking


* [ ] **Infrastructure**
* Docker containerization
* Kubernetes orchestration
* Enhanced caching and performance optimization
* Batch processing endpoints for large-scale analytics


* [ ] **Community & Compliance**
* HIPAA compliance certification
* Open-source contribution guidelines
* Comprehensive API documentation
* User guide and tutorial videos



---

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## License

This project is open source and available under the [MIT License](https://www.google.com/search?q=LICENSE).

---

## Acknowledgments

* **Technology:** Built with Streamlit, Hugging Face, PostgreSQL, and BERT
* **Community:** Thanks to all contributors and supporters

---

**Developed by Suvroneel** | [GitHub](https://github.com/Suvroneel) | [Live Demo](https://www.google.com/url?sa=E&source=gmail&q=https://phynix.streamlit.app/)

