# 🚀 QUICKSTART - Get Phynix Django Running in 5 Minutes!

## Prerequisites
- Python 3.10+
- PostgreSQL installed
- Git (optional)

---

## Step-by-Step Instructions

### 1. Extract the ZIP
```bash
unzip Phynix-Django-Complete.zip
cd Phynix-Django-Complete
```

### 2. Create Virtual Environment
```bash
# Create venv
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate

# On Mac/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup Database
```bash
# Open PostgreSQL
psql -U postgres

# Create database
CREATE DATABASE phynix_db;
\q
```

### 5. Configure Secrets
```bash
# Copy the example file
cp .env.example .env

# Edit .env and add YOUR secrets:
# - SUPABASE_URL (from your Streamlit secrets)
# - SUPABASE_KEY (from your Streamlit secrets)
# - SUPABASE_SERVICE_KEY (from your Streamlit secrets)
# - HUGGINGFACE_TOKEN (optional, from huggingface.co)
# - DB_PASSWORD (your PostgreSQL password)
```

**Minimal .env to get started:**
```env
SECRET_KEY=change-this-to-random-string
DEBUG=True
DB_NAME=phynix_db
DB_USER=postgres
DB_PASSWORD=your_postgres_password
DB_HOST=localhost
DB_PORT=5432
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
SUPABASE_SERVICE_KEY=your_service_key
```

### 6. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create Admin User (Optional)
```bash
python manage.py createsuperuser
# Follow prompts to create username/password
```

### 8. RUN THE SERVER! 🚀
```bash
python manage.py runserver
```

### 9. Open in Browser
Go to: **http://localhost:8000**

---

## 🎉 You're Done!

You should see:
- Login page at http://localhost:8000/login/
- Chat page at http://localhost:8000/chat/ (after login)
- Admin panel at http://localhost:8000/admin/

---

## 🐛 Common Issues

### "No module named 'django'"
```bash
pip install -r requirements.txt
```

### "FATAL: database does not exist"
```bash
psql -U postgres
CREATE DATABASE phynix_db;
\q
```

### "ImproperlyConfigured: Set the SECRET_KEY"
Edit your `.env` file and add:
```env
SECRET_KEY=your-random-secret-key-here
```

### "No such table: users"
```bash
python manage.py migrate
```

### Images not showing
```bash
python manage.py collectstatic --noinput
```

---

## 🔄 Daily Workflow

```bash
# 1. Activate virtual environment
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 2. Run server
python manage.py runserver

# 3. Open http://localhost:8000

# 4. Stop server: Ctrl+C
```

---

## 📁 Important Files

| File | Purpose |
|------|---------|
| `.env` | Your secrets (CREATE THIS!) |
| `manage.py` | Django commands |
| `requirements.txt` | Dependencies |
| `SETUP_GUIDE.md` | Detailed setup |
| `README.md` | Full documentation |

---

## 🎯 Next Steps After Running

1. **Test Login**: Create an account at `/login/`
2. **Test Chat**: Send a message to Ashva
3. **Check Admin**: Go to `/admin/` and login
4. **View Database**: Check that messages are saved

---

## 📞 Need Help?

- Check `SETUP_GUIDE.md` for detailed instructions
- Check `README.md` for full documentation
- Your Streamlit code is the reference for features

---

## ⚡ Super Quick Test (No Database)

Just want to see if Django works?

```bash
pip install django
python manage.py runserver
```

If you see the Django welcome page, it's working!

---

**That's it! Your Streamlit app is now Django! 🎉**
