from django import forms
from .models import QuesModel

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password']

class addQuestionForm(forms.ModelForm):
    class Meta:
        model = QuesModel
        fields = '__all__'