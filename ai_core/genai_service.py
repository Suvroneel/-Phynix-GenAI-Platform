"""
Generative AI Service using Hugging Face Inference API
Port of Utils/gen_ai.py from Streamlit to Django
"""

from huggingface_hub import InferenceClient
from django.conf import settings
import logging

logger = logging.getLogger(__name__)


class PhynixAI:
    """
    GenAI backend for empathetic AI responses
    Uses Hugging Face Inference API with multiple model support
    """
    
    _instance = None
    
    def __new__(cls):
        """Singleton pattern"""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialize()
        return cls._instance
    
    def _initialize(self):
        """Initialize the GenAI service"""
        self.hf_token = settings.HUGGINGFACE_TOKEN
        self.client = InferenceClient(token=self.hf_token)
        self.available_models = settings.GENAI_MODELS
        self.current_model = self.available_models[settings.DEFAULT_GENAI_MODEL]
        
        # System prompt for mental health context
        self.system_prompt = """You are Ashva, a compassionate AI companion within the Phynix mental health platform. Your role is to:
- Listen empathetically and validate emotions
- Provide supportive, non-judgmental responses
- Ask gentle follow-up questions when appropriate
- Never diagnose or provide medical advice
- Encourage professional help for serious concerns
- Keep responses conversational and warm (2-4 sentences typically)
- Use a caring, understanding tone"""
        
        logger.info(f"GenAI initialized with model: {self.current_model}")
    
    def set_model(self, model_name: str) -> bool:
        """Change the active GenAI model"""
        if model_name in self.available_models:
            self.current_model = self.available_models[model_name]
            logger.info(f"Switched to model: {self.current_model}")
            return True
        return False
    
    def generate_response(
        self,
        user_message: str,
        detected_emotion: str = None,
        risk_level: str = None,
        chat_history: list = None,
        max_tokens: int = 300,
        temperature: float = 0.7
    ) -> str:
        """
        Generate empathetic AI response
        
        Args:
            user_message: User's input text
            detected_emotion: Emotion detected by BERT
            risk_level: Risk level from emotion analysis
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
                for msg in chat_history:
                    messages.append({
                        "role": msg.get("role", "user"),
                        "content": msg.get("content", "")
                    })
            
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
            ai_response = response.choices[0].message.content.strip()
            
            logger.info(f"Generated response for emotion: {detected_emotion}")
            return ai_response
            
        except Exception as e:
            logger.error(f"Error generating AI response: {e}")
            
            # Fallback error handling
            error_msg = str(e)
            if "rate limit" in error_msg.lower():
                return "I'm experiencing high demand right now. Could you try again in a moment?"
            elif "model" in error_msg.lower():
                return "I'm having trouble connecting right now. Please try switching models or check back soon."
            else:
                return "I'm having a technical issue. Please try again."
    
    def get_model_info(self) -> dict:
        """Return current model information"""
        current_key = [k for k, v in self.available_models.items() if v == self.current_model][0]
        return {
            "current": self.current_model,
            "current_key": current_key,
            "available": list(self.available_models.keys())
        }
    
    def is_token_configured(self) -> bool:
        """Check if HF token is configured"""
        return self.hf_token is not None


# Global instance
genai_service = PhynixAI()


def generate_ai_response(
    user_message: str,
    detected_emotion: str = None,
    risk_level: str = None,
    chat_history: list = None,
    model_name: str = None
) -> dict:
    """
    Convenience function to generate AI response
    
    Args:
        user_message: User's message
        detected_emotion: Emotion from BERT
        risk_level: Risk level
        chat_history: Previous messages
        model_name: Optional model to use
    
    Returns:
        {
            'response': str,
            'model_used': str
        }
    """
    if model_name:
        genai_service.set_model(model_name)
    
    response = genai_service.generate_response(
        user_message=user_message,
        detected_emotion=detected_emotion,
        risk_level=risk_level,
        chat_history=chat_history
    )
    
    return {
        'response': response,
        'model_used': genai_service.get_model_info()['current_key']
    }
