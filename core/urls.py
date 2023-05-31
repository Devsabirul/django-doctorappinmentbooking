from django.urls import path
from .views import *
urlpatterns = [
    path('', Home.as_view(template_name="home/index.html"), name="Home"),
    path('search-doctor', Searchdoctor.as_view(template_name="home/searchdr.html"),
         name="searchDoctor"),
]
