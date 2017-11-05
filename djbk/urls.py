"""djbk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from entities import views

urlpatterns = [
#    url(r'^admin/', admin.site.urls),
# Home page (action):
    url(r'^$', views.home_page, name='home'),
# New (action) listing of entities:
    url(r'^entities/new$', views.new_list, name='new_list'),
# A specific listing (no action):
# The captured name can be passed to the view as a second param.
    url(r'^entities/(.*)/$',  # Captures the name of the listing.
        views.view_list, name='view_list'),
]

# Convention being used:
# URLs without trailing slash are 'action URLs'
# - ones that modify the database.

