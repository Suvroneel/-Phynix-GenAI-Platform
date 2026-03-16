from supabase import create_client, Client, ClientOptions
from datetime import datetime, timezone
import streamlit as st
import uuid

supabase_url = st.secrets['SUPABASE_URL']
supabase_key = st.secrets['SUPABASE_KEY']
supabase: Client = create_client(supabase_url, supabase_key, options=ClientOptions(postgrest_client_timeout=60))

BUCKET = "journal-images"


def get_today_entry_count(user_name: str) -> int:
    today_midnight = datetime.now().replace(
        hour=0, minute=0, second=0, microsecond=0
    ).astimezone(timezone.utc).isoformat()

    response = supabase.table("mood_journal") \
        .select("id", count="exact") \
        .eq("user_name", user_name) \
        .gte("created_at", today_midnight) \
        .execute()

    return response.count or 0


def fetch_today_entries(user_name: str) -> list:
    today_midnight = datetime.now().replace(
        hour=0, minute=0, second=0, microsecond=0
    ).astimezone(timezone.utc).isoformat()

    response = supabase.table("mood_journal") \
        .select("*") \
        .eq("user_name", user_name) \
        .gte("created_at", today_midnight) \
        .order("created_at", desc=True) \
        .execute()

    return response.data or []


def upload_image(user_name: str, file) -> str | None:
    try:
        ext = file.name.split(".")[-1]
        path = f"{user_name}/{uuid.uuid4().hex}.{ext}"
        supabase.storage.from_(BUCKET).upload(
            path,
            file.read(),
            {"content-type": file.type}
        )
        return supabase.storage.from_(BUCKET).get_public_url(path)
    except Exception as e:
        st.error(f"Image upload failed: {e}")
        return None


def insert_entry(user_name: str, user_email: str, entry_text: str, image_url: str = None) -> bool:
    try:
        supabase.table("mood_journal").insert({
            "user_name":  user_name,
            "user_email": user_email,
            "entry":      entry_text,
            "image_url":  image_url,
        }).execute()
        return True
    except Exception as e:
        st.error(f"Could not save entry: {e}")
        return False