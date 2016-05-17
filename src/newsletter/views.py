from django.shortcuts import render

from .forms import SignUpForm


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
	

	return render(request, "home.html", context)
