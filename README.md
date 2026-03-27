# Phynix

> *The more you talk to it, the more it becomes YOURS.*

Most AI talks at you. Phynix grows with you. It remembers how you felt last session, notices your patterns over time, and meets you where you actually are instead of starting from zero every single time.


**🔗 Live Demo:** https://phynix.streamlit.app/

Phynix is an **end-to-end AI mental health platform** designed to provide users a secure and interactive environment to express emotions, track mental well-being, and receive personalized AI-powered guidance. The heart of the system is **Ashva**, an intelligent companion powered by **BERT for emotion detection** and **advanced Generative AI models** for empathetic, context-aware conversations.

This platform is **multi-page**, **multi-layered**, and production-ready, combining a sophisticated frontend, hybrid AI/NLP backend, and relational database analytics.

---

## 🆕 Recent Updates

### v2.1.1 - Ashva Diaries (Mood Journal) - March 2026
Replaced the static placeholder with a fully functional journaling feature. Users can write daily reflections, optionally attach an image, and view today's entries as timestamped cards. Entries are stored in Supabase PostgreSQL with images in a dedicated Supabase Storage bucket. Fresh slate every day at midnight IST. Built with privacy-first design — no mood tagging, no sentiment analysis, just open reflection.

### v2.0 - Multi-Model GenAI Backend - February 2026
Replaced static hard-coded responses with a live multi-model GenAI backend. Ashva now generates dynamic, context-aware empathetic responses using 5 LLMs (Llama 3.1, Mistral 7B, Zephyr 7B, Phi-2, Gemma 2B) via Hugging Face Inference API. Users can switch models in real-time mid-conversation.

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

Phynix serves as a **digital mental health companion**, combining:

- **Hybrid Conversational AI**: Emotion classification via fine-tuned BERT, coupled with state-of-the-art Generative AI models for fluid, empathetic dialogue
- **Multi-Model Architecture**: Supports 5 different AI models with real-time switching capabilities for optimal response quality
- **Analytics & Dashboards**: Track emotional trends, risk levels, and confidence metrics over time
- **Private Journaling**: Secure mood journaling for personal reflection and mental health tracking

The platform emphasizes **privacy, data security, and actionable insights**, offering a mental refuge for individuals dealing with stress, anxiety, or depression.

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
│   ├── 1_Chat.py                   # Chat interface with Ashva
│   ├── 2_Home.py                   # Analytics dashboard
│   └── 3_Mood Journal.py           # Mood journaling
│
├── Utils/                           # Core utilities
│   ├── ashva.py                    # AI orchestration
│   ├── model.py                    # BERT emotion classification
│   ├── gen_ai.py                   # Generative AI integration
│   ├── database.py                 # Database operations
│   ├── config.py                   # Configuration
│   ├── reply.py                    # Response generation
│   ├── emotion_responses.py        # Emotion templates
│   ├── advice.py                   # Advice generation
│   ├── personality.py              # AI personality
│   ├── profile.py                  # User profiles
│   ├── Progression_Chart.py        # Analytics charts
│   ├── sidebar.py                  # Sidebar components
│   ├── footer.py                   # Footer components
│   ├── title.py                    # Title utilities
│   ├── Website_Title.py            # Title config
│   ├── Otp_verification.py         # OTP system
│   ├── Automated_Messages.py       # Auto messages
│   ├── feedback.py                 # Feedback system
│   ├── journal.py                  # Mood journal logic
│   └── __init__.py
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
│   ├── icons/                      # Favicons
│   └── profiles/                   # Profile avatars
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

- **Login:** Users authenticate via Supabase; session tokens stored securely
- **Signup:** Collects username, email, password; validates input; stores credentials in PostgreSQL
- **UI & UX:** Tab-based, responsive forms with inline error messages and validation feedback
- **Workflow:** Login → session storage → Chat page; Signup → email verification → Chat page

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
  - BERT model classifies user input into seven emotion categories
  - GenAI models generate contextually appropriate, empathetic responses based on detected emotion
  - Risk levels and confidence scores calculated and displayed with emoji indicators
  - Collapsible analysis section showing emotion breakdown and risk assessment
  
- **Multi-Model Support:**
  - Real-time model switching between 5 different AI architectures
  - Adjustable creativity (temperature) and response length controls
  - Model-specific optimizations for different conversation contexts
  
- **Database Integration:**
  - Supabase/PostgreSQL stores complete conversation history
  - Tracks messages, predicted emotions, risk levels, confidence scores, and AI-generated replies
  - Historical data powers analytics dashboard
  
- **UX Enhancements:**
  - "New Chat" button with safe conversation reset
  - Model selector with dropdown interface
  - Real-time streaming responses with character-by-character display

---

### Home Page

**Purpose:** Central dashboard offering insights, metrics, and daily motivational guidance.

![Home1](Site%20Images/Home_1.png)
![Home2](Site%20Images/Home_2.png)

**Key Features & Technical Details:**

- Interactive dashboard charts for emotion trends, confidence levels, and risk progression
- Personalized advice based on emotional patterns
- Daily motivational quotes and mental health tips
- Session-safe data retrieval ensures consistent metrics across pages
- Visual analytics powered by historical conversation data

---

### Mood Journal Page

**Purpose:** A private space for daily reflection — write freely, attach a photo, and let your thoughts exist without judgment.

![Mood Journal](https://github.com/Suvroneel/Phynix-GenAI-Platform/blob/Suvroneel-patch-1/Site%20Images/Ashva_diary.png)

**Key Features & Technical Details:**

- **Ashva Diaries** — open text journaling with optional image attachment
- Fresh slate every day at midnight IST — no clutter from previous days
- Entries stored securely in Supabase PostgreSQL with images in Supabase Storage bucket
- Timestamped cards displaying today's reflections
- Clear button to wipe today's view without deleting data
- Privacy-first — no mood tagging, no sentiment analysis, no judgment
- Profile management with editable bio and verified badge
- Authentication enforced via Supabase session tokens

---

## Backend Architecture

- **Supabase Authentication:** Token-based secure session management with refresh capabilities
- **PostgreSQL Data Layer:** 
  - `user_credentials` table for authentication
  - `user_data` table storing messages, emotions, risk levels, confidence scores, and AI replies
  - `mood_journal` table for private journaling entries
  - `journal-images` Supabase Storage bucket for image uploads
  
- **AI Inference Pipeline:**
  1. User input → Streamlit frontend
  2. BERT emotion classification model predicts emotional state
  3. Generative AI model (user-selected) generates contextual response
  4. Risk assessment algorithm calculates safety metrics
  5. All data persisted to PostgreSQL for analytics
  6. Dashboard queries historical data for trend visualization

---

## AI & NLP Layer

### Emotion Classification (BERT)
- **Fine-tuned BERT model** for mental health context
- Classifies user messages into **seven emotion categories**:
  - Joy, Sadness, Anger, Fear, Surprise, Disgust, Neutral
- Provides **confidence scores** for each prediction
- **Risk level assessment** based on detected emotions and sentiment intensity
- Real-time inference with sub-second response times

### Generative AI Response System
Phynix leverages **Hugging Face Inference API** with support for **5 state-of-the-art language models**:

- **Llama 3.1 (8B-Instruct)** - Meta's flagship model
  - Fast, general-purpose conversational AI
  - Excellent instruction-following capabilities
  - Strong context understanding

- **Mistral (7B-Instruct)** - Mistral AI
  - Superior reasoning and analytical responses
  - Balanced between speed and quality
  - Great for complex emotional discussions

- **Zephyr (7B-Beta)** - HuggingFace
  - Specifically optimized for chat interactions
  - Empathetic response generation
  - Fine-tuned for helpful, harmless conversations

- **Phi-2** - Microsoft
  - Lightweight and efficient
  - Fast response times
  - Good for quick supportive messages

- **Gemma (2B-IT)** - Google
  - Compact yet capable
  - Balanced performance across use cases
  - Optimized for instruction-following

### AI Integration Features
- **Real-time model switching** - Users can switch between models mid-conversation
- **Context-aware responses** - Full conversation history maintained for coherent dialogue
- **Temperature control** - Adjustable creativity from factual (0.0) to creative (1.0)
- **Token length management** - Configurable response lengths (100-1000 tokens)
- **Emotion-based prompting** - AI responses tailored to detected emotional state
- **Fallback handling** - Graceful error management with user-friendly messages

### Technical Implementation
```python
# Multi-model architecture with dynamic selection
models = {
    "llama": "meta-llama/Llama-3.1-8B-Instruct",
    "mistral": "mistralai/Mistral-7B-Instruct-v0.3",
    "zephyr": "HuggingFaceH4/zephyr-7b-beta",
    "phi": "microsoft/phi-2",
    "gemma": "google/gemma-2-2b-it"
}

# Inference pipeline
1. User message → BERT emotion detection
2. Emotion label + conversation history → GenAI model
3. AI generates empathetic, context-aware response
4. Response stored with metadata (emotion, risk, confidence)
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
  - Real-time model selector
  
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
- **Supabase** - Authentication, real-time database, and storage
- **PostgreSQL** - Relational data storage and analytics
- **Python** - Core application logic

### Machine Learning & AI
- **BERT (Transformers)** - Emotion classification model
- **Hugging Face Inference API** - Multi-model GenAI backend
  - Llama 3.1 (Meta)
  - Mistral (Mistral AI)
  - Zephyr (HuggingFace)
  - Phi-2 (Microsoft)
  - Gemma (Google)
- **PyTorch** - Deep learning framework
- **TensorFlow** - Model training and inference

### Data & Analytics
- **Pandas** - Data manipulation and analysis
- **Streamlit Charts** - Interactive visualizations
- **Custom Analytics** - Emotion trends and risk tracking

---

## Deployment

### Local Development
```bash
# Clone repository
git clone https://github.com/Suvroneel/Phynix-Mental-Health-Chatbot.git
cd Phynix-Mental-Health-Chatbot

# Install dependencies
pip install -r requirements.txt

# Configure Hugging Face token (optional but recommended)
# Create .streamlit/secrets.toml:
# HUGGINGFACE_TOKEN = "hf_your_token_here"

# Run application
streamlit run Logout.py
```

### Production Deployment
- **Platform:** Streamlit Community Cloud
- **Environment Configuration:** 
  - Supabase credentials via Streamlit secrets
  - Optional Hugging Face API token for enhanced rate limits
- **Continuous Deployment:** Auto-deploy from GitHub repository
- **Scalability:** Serverless architecture with automatic scaling

---

## Future Enhancements

- [ ] **Advanced AI Features**
  - Multi-agent conversation systems
  - Specialized therapeutic approaches (CBT, DBT)
  - Voice interaction capabilities
  - Real-time crisis detection with emergency routing

- [ ] **Analytics & ML**
  - Databricks / MLflow integration for experiment tracking
  - Predictive mental health insights
  - Personalized intervention recommendations
  - Advanced sentiment analysis with multi-dimensional metrics

- [ ] **Platform Expansion**
  - Multi-language support (10+ languages)
  - Mobile app (iOS/Android)
  - Therapist collaboration portal
  - Integration with wearables for holistic health tracking

- [ ] **Infrastructure**
  - Docker containerization
  - Kubernetes orchestration
  - Enhanced caching and performance optimization
  - Batch processing endpoints for large-scale analytics

- [ ] **Community & Compliance**
  - HIPAA compliance certification
  - Open-source contribution guidelines
  - Comprehensive API documentation
  - User guide and tutorial videos

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

This project is open source and available under the [MIT License](LICENSE).

---

## Acknowledgments

- **Mental health resources:** If you're in crisis, please contact your local emergency services or mental health helpline
- **Technology:** Built with Streamlit, Hugging Face, Supabase, and BERT
- **Community:** Thanks to all contributors and mental health advocates

---

**Developed by Suvroneel** | [GitHub](https://github.com/Suvroneel) | [Live Demo](https://phynix.streamlit.app/)
