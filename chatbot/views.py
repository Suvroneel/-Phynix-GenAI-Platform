"""
Chatbot API Views
Handles chat messages, emotion detection, AI responses
"""

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db import transaction

from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer, ChatMessageSerializer
from ai_core.bert_service import predict_emotion
from ai_core.genai_service import generate_ai_response

import logging

logger = logging.getLogger(__name__)


class ChatViewSet(viewsets.ModelViewSet):
    """
    API endpoints for chat functionality
    """
    permission_classes = [IsAuthenticated]
    serializer_class = MessageSerializer
    
    def get_queryset(self):
        """Return messages for the current user"""
        return Message.objects.filter(user=self.request.user)
    
    @action(detail=False, methods=['post'])
    @transaction.atomic
    def send_message(self, request):
        """
        Send a chat message and get AI response
        
        Request:
        {
            "message": "I'm feeling great today!",
            "conversation_id": 123,  # optional
            "model": "zephyr"  # optional
        }
        
        Response:
        {
            "user_message": {...},
            "ai_response": {...},
            "emotion": "joy",
            "risk_level": "Low",
            "confidence": 0.95
        }
        """
        try:
            serializer = ChatMessageSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            
            user_message_text = serializer.validated_data['message']
            conversation_id = serializer.validated_data.get('conversation_id')
            model_name = serializer.validated_data.get('model', 'zephyr')
            
            # Step 1: Get or create conversation
            if conversation_id:
                conversation = Conversation.objects.get(
                    id=conversation_id,
                    user=request.user
                )
            else:
                conversation = Conversation.objects.create(user=request.user)
            
            # Step 2: BERT Emotion Detection
            emotion_result = predict_emotion(user_message_text)
            detected_emotion = emotion_result['emotion']
            confidence = emotion_result['confidence']
            risk_level = emotion_result['risk_level']
            
            # Step 3: Get conversation history for context
            previous_messages = conversation.messages.order_by('created_at')[:10]
            chat_history = []
            for msg in previous_messages:
                chat_history.append({
                    "role": "user",
                    "content": msg.user_message
                })
                chat_history.append({
                    "role": "assistant",
                    "content": msg.ai_reply
                })
            
            # Step 4: Generate AI Response
            ai_result = generate_ai_response(
                user_message=user_message_text,
                detected_emotion=detected_emotion,
                risk_level=risk_level,
                chat_history=chat_history,
                model_name=model_name
            )
            ai_reply = ai_result['response']
            model_used = ai_result['model_used']
            
            # Step 5: Save message to database
            message = Message.objects.create(
                conversation=conversation,
                user=request.user,
                user_message=user_message_text,
                predicted_emotion=detected_emotion,
                confidence_score=confidence,
                risk_level=risk_level,
                ai_reply=ai_reply,
                ai_model_used=model_used
            )
            
            # Step 6: Return response
            return Response({
                'conversation_id': conversation.id,
                'message_id': message.id,
                'user_message': user_message_text,
                'ai_response': ai_reply,
                'emotion': detected_emotion,
                'risk_level': risk_level,
                'confidence': confidence,
                'model_used': model_used,
                'timestamp': message.created_at
            }, status=status.HTTP_201_CREATED)
            
        except Conversation.DoesNotExist:
            return Response(
                {'error': 'Conversation not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            logger.error(f"Error in send_message: {e}")
            return Response(
                {'error': 'Failed to process message'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    @action(detail=False, methods=['get'])
    def conversations(self, request):
        """Get all conversations for the current user"""
        conversations = Conversation.objects.filter(user=request.user)
        serializer = ConversationSerializer(conversations, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def conversation_messages(self, request, pk=None):
        """Get all messages in a conversation"""
        try:
            conversation = Conversation.objects.get(id=pk, user=request.user)
            messages = conversation.messages.all()
            serializer = MessageSerializer(messages, many=True)
            return Response(serializer.data)
        except Conversation.DoesNotExist:
            return Response(
                {'error': 'Conversation not found'},
                status=status.HTTP_404_NOT_FOUND
            )
    
    @action(detail=True, methods=['delete'])
    def clear_conversation(self, request, pk=None):
        """Clear/delete a conversation"""
        try:
            conversation = Conversation.objects.get(id=pk, user=request.user)
            conversation.delete()
            return Response(
                {'message': 'Conversation cleared'},
                status=status.HTTP_204_NO_CONTENT
            )
        except Conversation.DoesNotExist:
            return Response(
                {'error': 'Conversation not found'},
                status=status.HTTP_404_NOT_FOUND
            )
    
    @action(detail=False, methods=['post'])
    def new_conversation(self, request):
        """Start a new conversation"""
        conversation = Conversation.objects.create(user=request.user)
        serializer = ConversationSerializer(conversation)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
