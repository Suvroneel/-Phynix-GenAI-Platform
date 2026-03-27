"""
GenAI Backend for Phynix Mental Health Chatbot
Integrates with BERT emotion detection for empathetic responses
Uses Hugging Face Inference API with multiple model support
"""

from huggingface_hub import InferenceClient
import streamlit as st


class PhynixAI:
    def __init__(self, hf_token=None):
        """
        Initialize the GenAI model with Hugging Face Inference API
        
       
        """
        # Get token from Streamlit secrets or parameter
        if hf_token:
            self.hf_token = hf_token
        else:
            try:
                # Try both possible secret names
                self.hf_token = st.secrets.get("HF_TOKEN") or st.secrets.get("HUGGINGFACE_TOKEN")
            except:
                self.hf_token = None
                print("Warning: No HF token found. App will work but with lower rate limits.")
        
        # Initialize client with token
        self.client = InferenceClient(token=self.hf_token)
        
        # Available models - verified working as of Jan 2025
        self.available_models = {
            "llama": "meta-llama/Llama-3.1-8B-Instruct",
            
        }
        
        # Default model 
        self.current_model = self.available_models["llama"]
        
        # System prompt for mental health context
        self.system_prompt = """You are Ashva, a compassionate AI companion within the Phynix mental health platform. Your role is to:
- Listen empathetically and validate emotions
- Provide supportive, non-judgmental responses
- Ask gentle follow-up questions when appropriate
- Never diagnose or provide medical advice
- Encourage professional help for serious concerns
- Keep responses conversational and warm (2-4 sentences typically)
- Use a caring, understanding tone"""
    
    def set_model(self, model_name):
        """Change the active GenAI model"""
        if model_name in self.available_models:
            self.current_model = self.available_models[model_name]
            return True
        return False
    
    def generate_response(
        self, 
        user_message, 
        detected_emotion=None, 
        risk_level=None,
        chat_history=None, 
        max_tokens=300, 
        temperature=0.7
    ):
        """
        Generate empathetic AI response based on user input and emotion context
        
        Args:
            user_message: User's input text
            detected_emotion: Emotion detected by BERT (e.g., "sadness", "joy")
            risk_level: Risk level from emotion analysis (e.g., "High", "Low")
            chat_history: List of previous messages for context
            max_tokens: Maximum response length
            temperature: Creativity level (0.0-1.0)
        
        Returns:
            AI generated response text
        """
        try:
            # Build context-aware prompt
            emotion_context = ""
            if detected_emotion and risk_level:
                emotion_context = f"\n[Context: User's detected emotion is '{detected_emotion}' with {risk_level} risk level. Respond with appropriate empathy and care.]"
            
            # Prepare messages with system prompt
            messages = [
                {"role": "system", "content": self.system_prompt + emotion_context}
            ]
            
            # Add chat history if provided
            if chat_history:
                messages.extend(chat_history)
            
            # Add current user message
            messages.append({
                "role": "user",
                "content": user_message
            })
            
            # Generate response using Inference API
            response = self.client.chat_completion(
                model=self.current_model,
                messages=messages,
                max_tokens=max_tokens,
                temperature=temperature,
            )
            
            # Extract the response text
            ai_response = response.choices[0].message.content
            
            # Clean up response (remove any system artifacts)
            ai_response = ai_response.strip()
            
            return ai_response
            
        except Exception as e:
            # Fallback error handling
            error_msg = str(e)
            if "rate limit" in error_msg.lower():
                return "I'm experiencing high demand right now. Could you try again in a moment?"
            elif "model" in error_msg.lower():
                return "I'm having trouble connecting right now. Please try switching models or check back soon."
            else:
                return f"I'm having a technical issue. Please try again. (Error: {error_msg[:50]})"
    
    def get_model_info(self):
        """Return current model information"""
        return {
            "current": self.current_model,
            "available": list(self.available_models.keys())
        }
    
    def is_token_configured(self):
        """Check if HF token is configured"""
        return self.hf_token is not None



"""
=== WHAT THIS FILE DOES ===

This is the GenAI backend for Phynix that replaces hard-coded responses with AI-generated replies.

KEY COMPONENTS:
1. PhynixAI class - Main AI interface
2. 5 Hugging Face models - Llama, Mistral, Zephyr, Phi, Gemma (user can switch)
3. Mental health system prompt - Makes AI respond empathetically
4. Emotion context integration - AI knows user's emotion + risk level from BERT

HOW IT WORKS:
- User message + BERT emotion + risk level → GenAI model
- AI generates personalized, context-aware response (not random template!)
- Returns empathetic reply that matches user's emotional state

WHY WE USE THIS:
- Fluid, natural conversations instead of repetitive hard-coded replies
- AI adjusts tone based on emotion (more caring for sadness, upbeat for joy)
- Each response is unique and contextual
- Maintains conversation history for coherent dialogue

INTEGRATION:
- Called by chat_genai.py after BERT detects emotion
- Works with or without HF token (token gives better rate limits)
- Handles errors gracefully with user-friendly fallback messages
"""
