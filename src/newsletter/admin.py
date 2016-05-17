from django.contrib import admin

# Register your models here.
from .forms import SignUpForm
from .models import SignUp

class SignUpAdmin(admin.ModelAdmin):
	list_display = ["__str__", "full_name", "timestamp", "updated"]
	form = SignUpForm # Import von forms.py
	# Alternativ und uncustomized geht das auch so, (alle Felder von models.py werden importiert):
	# class Meta:
		# model = SignUp



admin.site.register(SignUp, SignUpAdmin)