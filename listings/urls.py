from django.urls import path
from . import views

app_name='listings' # Django 5.2 new function
urlpatterns = [
    # Define 3 end points of listings on website

    # path function meanings (type in url,function,clicked endpoint)
    
    # Endpoint path
    path('', views.index, name='listings'), 
    # Database endpoint path define listing_id for function listing in view.py
    path('<int:listing_id>', views.listing, name='listing'),
    # search endpoint
    path('search', views.search, name='search'), 
]