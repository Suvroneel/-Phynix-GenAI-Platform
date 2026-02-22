"""
BERT Emotion Detection Service
Port of Utils/model.py from Streamlit to Django
"""

import torch
import torch.nn.functional as F
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from django.conf import settings
import logging

logger = logging.getLogger(__name__)


class BERTEmotionDetector:
    """
    BERT-based emotion classification
    Uses: j-hartmann/emotion-english-distilroberta-base
    Detects 7 emotions: joy, sadness, anger, fear, surprise, disgust, neutral
    """
    
    _instance = None
    _model = None
    _tokenizer = None
    
    def __new__(cls):
        """Singleton pattern - load model only once"""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._load_model()
        return cls._instance
    
    def _load_model(self):
        """Load BERT model and tokenizer"""
        try:
            logger.info(f"Loading BERT model: {settings.BERT_MODEL_NAME}")
            
            self._tokenizer = AutoTokenizer.from_pretrained(settings.BERT_MODEL_NAME)
            self._model = AutoModelForSequenceClassification.from_pretrained(
                settings.BERT_MODEL_NAME
            )
            
            # Set to evaluation mode
            self._model.eval()
            
            logger.info("BERT model loaded successfully")
            
        except Exception as e:
            logger.error(f"Failed to load BERT model: {e}")
            raise
    
    def predict_emotion(self, text: str) -> dict:
        """
        Predict emotion from text
        
        Args:
            text: User message
        
        Returns:
            {
                'emotion': str (e.g., 'joy'),
                'confidence': float (0-1),
                'probabilities': dict of all emotions with probabilities
            }
        """
        try:
            # Tokenize input
            inputs = self._tokenizer(text, return_tensors='pt', truncation=True, max_length=512)
            
            # Get model predictions
            with torch.no_grad():
                outputs = self._model(**inputs)
                logits = outputs.logits
                probs = F.softmax(logits, dim=1)
            
            # Get predicted class
            predicted_class_id = torch.argmax(probs, dim=1).item()
            predicted_emotion = self._model.config.id2label[predicted_class_id]
            confidence = probs[0][predicted_class_id].item()
            
            # Get all emotion probabilities
            all_probs = {
                self._model.config.id2label[i]: probs[0][i].item()
                for i in range(len(probs[0]))
            }
            
            return {
                'emotion': predicted_emotion,
                'confidence': confidence,
                'probabilities': all_probs
            }
            
        except Exception as e:
            logger.error(f"Error predicting emotion: {e}")
            return {
                'emotion': 'neutral',
                'confidence': 0.0,
                'probabilities': {}
            }
    
    def get_risk_level(self, emotion: str) -> str:
        """
        Map emotion to risk level
        Port of emotion_responses.py logic
        
        Args:
            emotion: Predicted emotion
        
        Returns:
            Risk level: 'High', 'Moderate', 'Neutral', or 'Low'
        """
        emotion_to_risk = {
            'sadness': 'High',
            'fear': 'High',
            'anger': 'High',
            'disgust': 'Moderate',
            'neutral': 'Neutral',
            'joy': 'Low',
            'surprise': 'Low'
        }
        return emotion_to_risk.get(emotion.lower(), 'Neutral')


# Global instance
bert_detector = BERTEmotionDetector()


def predict_emotion(text: str) -> dict:
    """
    Convenience function to predict emotion
    
    Args:
        text: User message
    
    Returns:
        {
            'emotion': str,
            'confidence': float,
            'risk_level': str,
            'probabilities': dict
        }
    """
    result = bert_detector.predict_emotion(text)
    result['risk_level'] = bert_detector.get_risk_level(result['emotion'])
    return result
