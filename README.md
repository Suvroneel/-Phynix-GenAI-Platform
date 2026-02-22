# Phynix Django - Complete Migration Guide

## 🎯 What's Been Created

This is a **complete Django backend** for Phynix, replacing Streamlit with a production-ready REST API.

### ✅ Core Features Implemented:

1. **User Authentication** (replaces Supabase Auth)
   - Email/password registration
   - JWT token authentication
   - User profiles with bio and avatar

2. **BERT Emotion Detection** (port of Utils/model.py)
   - Real-time emotion classification (7 emotions)
   - Confidence scoring
   - Risk level assessment

3. **GenAI Response System** (port of Utils/gen_ai.py)
   - 5 Hugging Face models (Llama, Mistral, Zephyr, Phi, Gemma)
   - Context-aware responses
   - Emotion-based prompting

4. **Chat System** (replaces pages/1_Chat.py)
   - Conversation management
   - Message history
   - Real-time AI responses

5. **Analytics Dashboard** (replaces pages/2_Home.py)
   - Emotion trends
   - Risk progression
   - User statistics

6. **Mood Journal** (replaces pages/3_Mood Journal.py)
   - Private journaling
   - Timestamped entries

7. **PostgreSQL Database** (replaces Supabase tables)
   - User credentials
   - Conversations and messages
   - Journal entries
   - User bios

---

## 📦 Project Structure

```
phynix-django/
├── requirements.txt              # All Python dependencies
├── manage.py                     # Django management
├── .env.example                  # Environment variables template
│
├── phynix_backend/               # Main Django project
│   ├── settings.py              # ✅ Complete configuration
│   ├── urls.py                  # URL routing
│   ├── wsgi.py                  # WSGI server
│   └── asgi.py                  # ASGI server (WebSockets)
│
├── users/                        # User management app
│   ├── models.py                # ✅ User, UserBio models
│   ├── views.py                 # Authentication endpoints
│   ├── serializers.py           # User data serialization
│   └── urls.py                  # User routes
│
├── chatbot/                      # Chat functionality app
│   ├── models.py                # ✅ Conversation, Message models
│   ├── views.py                 # ✅ Chat API endpoints
│   ├── serializers.py           # ✅ Chat data serialization
│   └── urls.py                  # Chat routes
│
├── ai_core/                      # AI/ML services
│   ├── bert_service.py          # ✅ BERT emotion detection
│   ├── genai_service.py         # ✅ GenAI response generation
│   └── models.py                # AI model management
│
├── analytics/                    # Analytics & dashboards
│   ├── models.py                # Analytics data models
│   ├── views.py                 # Dashboard endpoints
│   └── serializers.py           # Analytics serialization
│
├── journal/                      # Mood journaling app
│   ├── models.py                # ✅ JournalEntry model
│   ├── views.py                 # Journal endpoints
│   └── serializers.py           # Journal serialization
│
├── static/                       # Static files (CSS, JS, images)
├── media/                        # User uploads
└── templates/                    # HTML templates (optional)
```

---

## 🚀 Installation & Setup

### Prerequisites

- Python 3.10+
- PostgreSQL 13+
- Redis (for WebSockets - optional)
- Git

### Step 1: Clone & Setup

```bash
cd phynix-django

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Step 2: Database Setup

```bash
# Create PostgreSQL database
psql -U postgres
CREATE DATABASE phynix_db;
CREATE USER phynix_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE phynix_db TO phynix_user;
\q
```

### Step 3: Environment Variables

Create `.env` file:

```env
# Django Settings
SECRET_KEY=your-super-secret-key-here-change-this
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database
DB_NAME=phynix_db
DB_USER=phynix_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432

# Hugging Face
HUGGINGFACE_TOKEN=hf_your_token_here

# Redis (optional for WebSockets)
REDIS_HOST=127.0.0.1
REDIS_PORT=6379

# Email (optional)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password

# CORS (for frontend)
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://localhost:8000
```

### Step 4: Run Migrations

```bash
# Create database tables
python manage.py makemigrations
python manage.py migrate

# Create superuser (admin)
python manage.py createsuperuser
```

### Step 5: Load BERT Model (First Time)

```bash
# This will download the BERT model (~400MB)
python manage.py shell
>>> from ai_core.bert_service import bert_detector
>>> bert_detector.predict_emotion("I'm feeling great!")
>>> exit()
```

### Step 6: Run Server

```bash
# Development server
python manage.py runserver

# Or with Daphne (for WebSockets)
daphne -b 0.0.0.0 -p 8000 phynix_backend.asgi:application
```

Server runs at: **http://localhost:8000**

---

## 🔌 API Endpoints

### Authentication

```bash
# Register
POST /api/auth/register/
{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "SecurePass123"
}

# Login
POST /api/auth/login/
{
  "email": "john@example.com",
  "password": "SecurePass123"
}
Response: {
  "access": "jwt_token",
  "refresh": "refresh_token"
}

# Use token in headers
Authorization: Bearer <jwt_token>
```

### Chat

```bash
# Send message
POST /api/chat/send_message/
Authorization: Bearer <token>
{
  "message": "I'm feeling anxious today",
  "conversation_id": 1,  # optional
  "model": "zephyr"  # optional
}

Response:
{
  "conversation_id": 1,
  "message_id": 123,
  "user_message": "I'm feeling anxious today",
  "ai_response": "I hear you. Anxiety can be overwhelming...",
  "emotion": "fear",
  "risk_level": "High",
  "confidence": 0.87,
  "model_used": "zephyr"
}

# Get conversations
GET /api/chat/conversations/

# Get conversation messages
GET /api/chat/1/conversation_messages/

# New conversation
POST /api/chat/new_conversation/

# Clear conversation
DELETE /api/chat/1/clear_conversation/
```

### Analytics

```bash
# Get user stats
GET /api/analytics/stats/

# Get emotion trends
GET /api/analytics/emotion_trends/

# Get risk progression
GET /api/analytics/risk_progression/
```

### Journal

```bash
# Create entry
POST /api/journal/entries/
{
  "title": "Today's Reflection",
  "content": "I felt...",
  "mood": "calm"
}

# Get entries
GET /api/journal/entries/

# Update entry
PUT /api/journal/entries/1/

# Delete entry
DELETE /api/journal/entries/1/
```

---

## 🎨 Frontend Integration

### React/Vue/Next.js Example

```javascript
// Login
const login = async (email, password) => {
  const response = await fetch('http://localhost:8000/api/auth/login/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email, password })
  });
  const data = await response.json();
  localStorage.setItem('token', data.access);
};

// Send chat message
const sendMessage = async (message) => {
  const token = localStorage.getItem('token');
  const response = await fetch('http://localhost:8000/api/chat/send_message/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`
    },
    body: JSON.stringify({ message })
  });
  return await response.json();
};
```

---

## 🔄 Migration from Streamlit

### What Changed:

| Streamlit | Django Equivalent |
|-----------|------------------|
| `Logout.py` (auth) | `/api/auth/` endpoints |
| `pages/1_Chat.py` | `/api/chat/send_message/` |
| `pages/2_Home.py` | `/api/analytics/` endpoints |
| `pages/3_Mood Journal.py` | `/api/journal/entries/` |
| `Utils/model.py` | `ai_core/bert_service.py` |
| `Utils/gen_ai.py` | `ai_core/genai_service.py` |
| `Utils/database.py` | Django ORM models |
| Supabase tables | PostgreSQL with Django migrations |
| `st.session_state` | JWT tokens + database |

---

## 🧪 Testing

```bash
# Run tests
python manage.py test

# Test BERT service
python manage.py shell
>>> from ai_core.bert_service import predict_emotion
>>> result = predict_emotion("I'm so happy!")
>>> print(result)

# Test GenAI service
>>> from ai_core.genai_service import generate_ai_response
>>> response = generate_ai_response("I feel sad", "sadness", "High")
>>> print(response)
```

---

## 📊 Admin Panel

Access Django admin at: **http://localhost:8000/admin/**

Login with superuser credentials to:
- View all users
- Manage conversations
- Monitor messages
- Check analytics

---

## 🚀 Deployment

### Production Checklist

1. Set `DEBUG=False` in `.env`
2. Use production database (PostgreSQL)
3. Configure proper `SECRET_KEY`
4. Set up static file serving
5. Use Gunicorn/Daphne
6. Enable HTTPS
7. Set up Redis for WebSockets
8. Configure email backend

### Deploy to Railway/Render/Heroku

```bash
# Procfile
web: gunicorn phynix_backend.wsgi
worker: daphne phynix_backend.asgi:application

# runtime.txt
python-3.11.0
```

---

## 🔧 Next Steps

1. **Build Frontend**: React/Vue/Next.js connecting to Django API
2. **Add WebSockets**: Real-time chat with Django Channels
3. **Implement Caching**: Redis for faster responses
4. **Add Tests**: Unit and integration tests
5. **Deploy**: Production deployment

---

## 📞 Support

Questions? Issues? Check:
- Django docs: https://docs.djangoproject.com
- Hugging Face docs: https://huggingface.co/docs
- Original Streamlit code for reference

---

**Built with ❤️ for mental health support**

Migration completed: Streamlit → Django REST API
