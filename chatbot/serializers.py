"""
Serializers for Phynix API
"""

from rest_framework import serializers
from .models import Conversation, Message
from journal.models import JournalEntry
from users.models import User, UserBio


# ===== User Serializers =====

class UserSerializer(serializers.ModelSerializer):
    """User profile serializer"""
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'display_name', 'bio', 'profile_image', 'created_at']
        read_only_fields = ['id', 'created_at']


class UserBioSerializer(serializers.ModelSerializer):
    """User bio serializer"""
    class Meta:
        model = UserBio
        fields = ['id', 'description', 'created_at']
        read_only_fields = ['id', 'created_at']


# ===== Chatbot Serializers =====

class MessageSerializer(serializers.ModelSerializer):
    """Message serializer"""
    emotion_display = serializers.ReadOnlyField()
    
    class Meta:
        model = Message
        fields = [
            'id', 'conversation', 'user_message', 'predicted_emotion',
            'confidence_score', 'risk_level', 'ai_reply', 'ai_model_used',
            'created_at', 'emotion_display'
        ]
        read_only_fields = ['id', 'created_at', 'emotion_display']


class ConversationSerializer(serializers.ModelSerializer):
    """Conversation serializer with message count"""
    message_count = serializers.SerializerMethodField()
    last_message = serializers.SerializerMethodField()
    
    class Meta:
        model = Conversation
        fields = ['id', 'created_at', 'updated_at', 'is_active', 'message_count', 'last_message']
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def get_message_count(self, obj):
        return obj.messages.count()
    
    def get_last_message(self, obj):
        last_msg = obj.messages.last()
        return last_msg.user_message[:50] if last_msg else None


class ChatMessageSerializer(serializers.Serializer):
    """Serializer for incoming chat messages"""
    message = serializers.CharField(required=True, max_length=5000)
    conversation_id = serializers.IntegerField(required=False, allow_null=True)
    model = serializers.ChoiceField(
        choices=['llama', 'mistral', 'zephyr', 'phi', 'gemma'],
        default='zephyr',
        required=False
    )


# ===== Journal Serializers =====

class JournalEntrySerializer(serializers.ModelSerializer):
    """Journal entry serializer"""
    class Meta:
        model = JournalEntry
        fields = ['id', 'title', 'content', 'mood', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


# ===== Analytics Serializers =====

class EmotionAnalyticsSerializer(serializers.Serializer):
    """Serializer for emotion analytics data"""
    emotion = serializers.CharField()
    count = serializers.IntegerField()
    percentage = serializers.FloatField()


class UserStatsSerializer(serializers.Serializer):
    """Serializer for user statistics"""
    total_messages = serializers.IntegerField()
    total_conversations = serializers.IntegerField()
    total_journal_entries = serializers.IntegerField()
    average_confidence = serializers.FloatField()
    most_common_emotion = serializers.CharField()
    current_risk_level = serializers.CharField()
