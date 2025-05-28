from django.urls import path
from . import views

app_name='listings' # Django 5.2 new function
urlpatterns = [
    # Define 3 end points of listings on website
    # path function meanings (type in url,function,clicked endpoint)
    path('', views.index, name='listings'), # endpoint
    path('<int:listing_id>', views.listing, name='listing'), # Database endpoint
    path('search', views.search, name='search'), # search endpoint
]