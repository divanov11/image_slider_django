from django.shortcuts import render
from .models import *

# Create your views here.

def slider(request):
	product = Product.objects.first()
	context = {'product':product}
	return render(request, 'products/index.html', context)
