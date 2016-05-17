from django import forms
from .models import SignUp

# Legt die Felder in der Admin fest.
class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ['full_name', 'email']

	def clean_email(self): # WICHTIG: das hier muss so aussehen: clean_<field_name>(self):
		email = self.cleaned_data.get('email') # Holt sich email nachdem es die django-eigene Vlidation durchlaufen hat
		email_base, provider = email.split('@') # teilt email beim @
		host, domain = provider.split('.') # teilt alles hinterm @ in vor und nach dem punkt
		if not "moritz" in host:
			raise forms.ValidationError("Ey, du brauchst eine Email-Adresse mit ...@moritz drin!")
		return email

	def clean_full_name(self):
		full_name = self.cleaned_data.get('full_name')
		if not "Moritz" in full_name:
			raise forms.ValidationError("Tja, wir nehmen hier nur Leute, die Moritz heißen.")
		return full_name