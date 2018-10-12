from django import forms
from .models import Project,Profile, Comments
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['profile','posted_time','user']
        


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comments
#         exclude = ['project','user']

# class EditForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['bio','profile_pic']