from django.shortcuts import render

# Create your views here.

def home(request):
	title = "Willkommen!"
	if request.user.is_authenticated():
		title = """Hallo %s! %s, du bist echt cool!""" % (request.user, request.user)
	context = {
		"template_title":	title,
		"x":				3 + 4,
	}
	return render(request, "home.html", context)
