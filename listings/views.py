from django.shortcuts import render, get_object_or_404
from listings.models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Added choice lists functions
from pages.choices import price_choices, bedroom_choices, district_choices

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
    queryset_list = Listing.objects.order_by('-list_date')
    # Use .GET method to retrive data from data form, no need to encrypt.
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)
    if 'title' in request.GET:
        title = request.GET['title']
        if title:
            queryset_list = queryset_list.filter(title__icontains=title)
    if 'district' in request.GET:
        district = request.GET['district']
        if district:
            queryset_list = queryset_list.filter(district__iexact=district)
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)
    context = {
        "price_choices" : price_choices,
        "bedroom_choices" : bedroom_choices,
        "district_choices" : district_choices,
        "listings" : queryset_list,
        "values" : request.GET
    }
    return render(request,'listings/search.html',context)
