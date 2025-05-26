from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #   return HttpResponse("<h1>Hello World</h1>") # Run on servew ok
    return render(request,'pages/index.html') # Accesss index.html in templates folder

def about(request):
    return render(request,'pages/about.html') # Accesss about.html in templates folder
