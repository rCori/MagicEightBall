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
		
"""
class UserForm(forms.ModelForm):
	class Meta:
		model = settings.AUTH_USER_MODEL
		fields = [
			"username",
			"password",
			"email",
		]
"""