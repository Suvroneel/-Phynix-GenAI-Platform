"""
Custom User Model for Phynix
Replaces Supabase user_credentials table
"""

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """
    Custom user model extending Django's AbstractUser
    """
    email = models.EmailField(unique=True)
    display_name = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    profile_image = models.CharField(
        max_length=255,
        default='images/profiles/profile1.png'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_verified = models.BooleanField(default=False)
    
    # Use email as the username field
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    class Meta:
        db_table = 'users'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.email
    
    @property
    def name(self):
        """Return display name or username"""
        return self.display_name or self.username


class UserBio(models.Model):
    """
    User biography/description
    Replaces Supabase user_bio table
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bios')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'user_bio'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user.username}'s bio"
