from django.shortcuts import render, get_object_or_404
from listings.models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here. It's 2 level design so these are end points.
def index(request):
    # Step 3: Query the DB
    listings = Listing.objects.all()    # From backend: Pass DB Table object into a group
    paginator = Paginator(listings,3)   # Classify each page contain 3 records only
    page = request.GET.get('page')      # From frontend: Use Get method to retrive frontend data.
    paged_listings = paginator.get_page(page)   # Organize objects and pass page no. to the context.
    context = {"listings" : paged_listings} 
    # Pass dictionaries from new DB object into a variable
    # context = {"listings":listings} # Old code

    # original: return render(request,'listings/listings.html')
    # Step 1: One variable: Pass dictionary of data to the listings
    # return render(request,'listings/listings.html',{'name' : 'something'})
    # Step 2: Multi-variables: will define a variable in function to handle this.
    # context = {"name" : "something"}
    return render(request,'listings/listings.html',context) # Pass variable to render templates

def listing(request,listing_id):    # listing_id is resolved by urls.py
    # query set short cut of 1 house by listing_id, need "or_404" because real time house data might be deleted.
    listing = get_object_or_404(Listing,pk=listing_id)
    context = {"listing" : listing}
    return render(request,'listings/listing.html', context)

def search(request):
    return render(request,'listings/search.html')
