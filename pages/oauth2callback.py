"""
OAuth2 Callback Handler
"""

import streamlit as st
from supabase import create_client, Client


# Supabase setup
supabase_url = st.secrets['SUPABASE_URL']
supabase_key = st.secrets['SUPABASE_KEY']
supabase: Client = create_client(supabase_url, supabase_key)

st.info("🔄 Completing sign-in...")

# Get session from Supabase (handles OAuth automatically)
try:
    session = supabase.auth.get_session()
    
    if session and session.access_token:
        user = supabase.auth.get_user()
        
        if user and user.user:
            # Store in session state
            st.session_state["access_token"] = session.access_token
            st.session_state["refresh_token"] = session.refresh_token
            st.session_state["user_email"] = user.user.email
            st.session_state["logged_in"] = True
            
            # Redirect to Logout.py (which will handle username check)
            st.switch_page("Logout.py")
    else:
        st.error("No session found")
        st.switch_page("Logout.py")
        
except Exception as e:
    st.error(f"Error: {str(e)}")
    st.switch_page("Logout.py")