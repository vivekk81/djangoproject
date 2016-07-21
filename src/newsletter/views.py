from django.shortcuts import render

def home(request):
	title = "welcome"
	if request.user.is_authenticated():
		title="my title %s" %(request.user)

	context={
		"title":title,
	}
	return render(request,"home.html",context)
