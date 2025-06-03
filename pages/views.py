from django.shortcuts import render
# This library is for later implementation
from django.urls import reverse
# Following library is for testing initialization
#from django.http import HttpResponse
from pages.choices import price_choices, bedroom_choices, district_choices

# Import model for functions
from listings.models import Listing
from realtors.models import Realtor

# Create your views here.
def index(request):
    # pages_url = reverse('pages:index') # old testing code
    # Add boolean field control on the backend page.
    # .object. is BaseManager[Listing] preparing query sets until meeting with a list object before execute.
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {"listings":listings,
    "price_choices" : price_choices,
    "bedroom_choices" : bedroom_choices,
    "district_choices" : district_choices}
    #   return HttpResponse("<h1>Hello World</h1>") # Run on servew ok
    # return render(request,'pages/index.html') # Accesss index.html in templates folder (old testing code)
    return render(request,'pages/index.html',context) # Pass data from listings to context.

def about(request):
    realtors_base = Realtor.objects.all()
    realtors = realtors_base.order_by('-hire_date') # -ve means ascending order
    mvp_realtors = realtors_base.filter(is_mvp=True)
    context = {"realtors" : realtors, "mvp_realtors" : mvp_realtors}
    # about_url = reverse('pages:about') # old testing code
    # Accesss about.html in templates folder, then pass the context dictionary for render function to excute the sql
    return render(request,'pages/about.html',context)
