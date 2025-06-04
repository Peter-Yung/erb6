"""
URL configuration for erb6 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls
# Add config libraries for django look at settings.py file
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [ # Inside [] are for public Always put the most popular scenario on top.
    path('', include('pages.urls', namespace='pages')),     # pages is an APPS level group
    path('listings/', include('listings.urls', namespace='listings')), 
    path('accounts/', include('accounts.urls', namespace='accounts')),  # Add account app url
    path('admin/', admin.site.urls),
    # For private urls, we will add ouside the []
    ] + debug_toolbar_urls() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
