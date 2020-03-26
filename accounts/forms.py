from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
# from story_cards.models import User
User = get_user_model()

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']