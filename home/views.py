from itertools import product
from django.shortcuts import render
from .models import productDetailsVehicles

# Create your views here.
def home(request):
    return render (request, 'home.html', context={})

def vehicles(request):
    product= productDetailsVehicles.objects.all()
   
    return render(request, 'vehicles.html', context={'product':product})