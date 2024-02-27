from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import password_validation

# Create your forms here.

class NewUserForm(UserCreationForm):
	
	email = forms.EmailField(
		required=True,
		label="",
		widget=forms.EmailInput(attrs={
			'class' : 'form-control',
			'placeholder' : 'Email',
			
		})
	)
	password1 = forms.CharField(
		label="",
		widget=forms.PasswordInput(attrs={
			'class' : 'form-control',
			'placeholder' : 'Password',
		}),
		help_text=password_validation.password_validators_help_text_html(),
	)
	password2 = forms.CharField(
		label="",
		widget=forms.PasswordInput(attrs={
			'class' : 'form-control',
			'placeholder' : 'Retype Password',
		})	
	)
	username = forms.CharField(
		label="",
		widget=forms.TextInput(attrs={
			'class' : 'form-control',
			'placeholder' : 'Username'
		})
	)
	
	class Meta:

		model = User
		fields = ("first_name", "last_name", "username", "email", "password1", "password2")
		
		labels = {
			'first_name' : _(''),
			'last_name' : _(''),
		}

		widgets = {
			'first_name' : forms.TextInput(attrs={
				'class' : 'form-control',
				'placeholder' : 'First Name',
			}),
			'last_name' : forms.TextInput(attrs={
				'class' : 'form-control',
				'placeholder' : 'Last Name',
			}),
		}

	def get_credentials(self):

		return {
			# 'first_name' : self.cleaned_data['first_name'],
			# 'last_name' : self.cleaned_data['last_name'],
			# 'email' : self.cleaned_data['email'],
			'username' : self.cleaned_data['username'],
			'password' : self.cleaned_data['password1']
		}

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class LoginForm(forms.Form):
	pass