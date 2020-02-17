
from django.shortcuts import render
from bikes.models import Bike

# Create your views here.

def hello_view(request):
	return render(request, 'hello_django.html', {
		'data': "NCTU CS",
	})

def list_all(request):
	bikes = Bike.objects.all().order_by('idn')
	
	return render(request, 'listall.html', locals())

def post(request):
	if request.method == "POST":
		mess = request.POST
	else
		mess = "Not send yet."

	return render(request, "post.html", locals())
