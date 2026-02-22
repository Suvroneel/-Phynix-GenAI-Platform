"""
Chatbot Models - Conversation and Message Storage
Replaces Supabase user_data table
"""

from django.db import models
from django.conf import settings

class Conversation(models.Model):
    """
    Conversation session for a user
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'conversations'
        ordering = ['-updated_at']
    
    def __str__(self):
        return f"Conversation {self.id} - {self.user.username}"


class Message(models.Model):
    """
    Individual message in a conversation
    Stores: user message, predicted emotion, risk level, AI reply
    """
    
    EMOTION_CHOICES = [
        ('joy', 'Joy'),
        ('sadness', 'Sadness'),
        ('anger', 'Anger'),
        ('fear', 'Fear'),
        ('surprise', 'Surprise'),
        ('disgust', 'Disgust'),
        ('neutral', 'Neutral'),
    ]
    
    RISK_CHOICES = [
        ('Low', 'Low'),
        ('Neutral', 'Neutral'),
        ('Moderate', 'Moderate'),
        ('High', 'High'),
    ]
    
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='messages')
    
    # User message
    user_message = models.TextField()
    
    # BERT emotion detection results
    predicted_emotion = models.CharField(max_length=20, choices=EMOTION_CHOICES)
    confidence_score = models.FloatField(default=0.0)  # BERT confidence
    risk_level = models.CharField(max_length=20, choices=RISK_CHOICES)
    
    # AI generated reply
    ai_reply = models.TextField()
    ai_model_used = models.CharField(max_length=50, default='zephyr')  # Which GenAI model
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'messages'
        ordering = ['created_at']
    
    def __str__(self):
        return f"{self.user.username}: {self.user_message[:50]}"
    
    @property
    def emotion_display(self):
        """Get emotion with emoji"""
        emotion_emoji = {
            'joy': '😊',
            'sadness': '😢',
            'anger': '😠',
            'fear': '😨',
            'surprise': '😲',
            'disgust': '🤢',
            'neutral': '😐',
        }
        return f"{emotion_emoji.get(self.predicted_emotion, '')} {self.predicted_emotion.capitalize()}"
