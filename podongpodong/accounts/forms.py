from django.contrib.auth.models import User
from django import forms
from django.db import models
from .models import UserProfile

class SignupForm(forms.Form):
    class Meta:
        model = User
    
    name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder':''}), label="이름")
    phone = forms.IntegerField(widget=forms.TextInput(attrs={'placehoder':''}), label="전화번호")
    
    def signup(self, request, user):
        userProfile = UserProfile()
        userProfile.user = user
        userProfile.name = self.cleaned_data[('name')]
        userProfile.email = user.email
        userProfile.phone = self.cleaned_data[('phone')]
        userProfile.save()
        user.save()
        return user