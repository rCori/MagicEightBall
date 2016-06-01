from django import forms
from .models import Question
from django.conf import settings
from django.contrib.auth.views import login

class QuestionForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = [
			"title",
			"totalAnswers",
		]
		
	
class UserForm(forms.Form):
	username = forms.CharField(label='Username', max_length=100)
	email = forms.CharField(label='Email', max_length=100)
	password = forms.CharField(label='Password', max_length=100)