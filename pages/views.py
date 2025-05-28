from django.shortcuts import render
# This library is for later implementation
from django.urls import reverse
# Following library is for testing initialization
#from django.http import HttpResponse

# Create your views here.
def index(request):
    pages_url = reverse('pages:index')
    #   return HttpResponse("<h1>Hello World</h1>") # Run on servew ok
    return render(request,'pages/index.html') # Accesss index.html in templates folder

def about(request):
    about_url = reverse('pages:about')
    return render(request,'pages/about.html') # Accesss about.html in templates folder
