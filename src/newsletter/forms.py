from django import forms
from .models import SignUp

# Legt die Felder in der Admin fest.
class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ['full_name', 'email']