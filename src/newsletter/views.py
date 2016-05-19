from django.conf import settings ### !!!

from django.shortcuts import render
from django.core.mail import send_mail

from .forms import SignUpForm, ContactForm


def home(request):
	title = "Willkommen!"
	form = SignUpForm(request.POST or None)

	context = {
		"template_title":	title,
		"x":				3 + 4,
		"form":				form,
	}

	if form.is_valid():
		instance = form.save(commit=False) # This skips the saving in order to do custom stuff BEFORE saving it.
		instance.save()
		print (instance.email)
		print (instance.timestamp)
		context = { # Der Kontext wird hier verändert. Immer dran denken, das ist auch einfach nur ein variables Dictianary.
		"template_title":	"Das hat geklappt. Danke!",
		"x":				32 + 44,
		}

	if request.user.is_authenticated():
		title = """Hallo %s! %s, du bist echt cool!""" % (request.user, request.user)
	

	return render(request, "base.html", context)


def contact(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		# for key, value in form.cleaned_data.items(): # war iteritems() in python2
		# 	print (key,':', value)


		# Das hier drunter geht auch, aber es geht noch einfacher.
		# for key in form.cleaned_data:
			# print (key,"->", form.cleaned_data.get(key) + "\n")

		# Das hier drunter geht auch, ist aber umständlich. Jetzt aber gut, um die vars an send_email() zu übergeben.
		form_email = form.cleaned_data.get('email')
		form_full_name = form.cleaned_data.get('full_name')
		form_message = form.cleaned_data.get('message')
		print ("Name:", form_full_name, "Email:", form_email, "Message:", form_message)
		
		subject = "Mail von Contact Form"
		from_email = settings.EMAIL_HOST_USER # siehe settings.py für email Settings
		to_email = from_email
		contact_message = "%s schreibt uns via %s:\n\n %s" % (form_full_name, form_email, form_message)
		send_mail(subject,
			contact_message,
			from_email,
			[to_email], 
			fail_silently=False)

	context = {
		"form": 			form,
	}

	return render(request, "forms.html", context)