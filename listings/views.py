from django.shortcuts import render

# Create your views here. It's 2 level design so these are end points.
def index(request):
    return render(request,'listings/listings.html')

def listing(request,listing_id):
    return render(request,'listings/listing.html')

def search(request):
    return render(request,'listings/search.html')
