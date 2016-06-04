from django import forms
from django.contrib.auth.models import User
from .models import Question
from django.conf import settings
from django.contrib.auth.views import login
from django.utils.translation import ugettext_lazy

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
	

class RegistrationForm(forms.Form):
 
    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=ugettext_lazy("Username"), error_messages={ 'invalid': ugettext_lazy("This value must contain only letters, numbers and underscores.") })
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=ugettext_lazy("Email address"))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=ugettext_lazy("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=ugettext_lazy("Password (again)"))
 
    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(ugettext_lazy("The username already exists. Please try another one."))
 
    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(ugettext_lazy("The two password fields did not match."))
        return self.cleaned_data

		
class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=ugettext_lazy("Username"))
	password = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=ugettext_lazy("Password"))