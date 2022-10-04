from django.urls import path
from .views import  home, about, contact_list, contact_details 
#from . import views

urlpatterns = [
    path("", home, name="index"),
    path("about/", about, name="about"),
    path("Contacts/", contact_list, name="Contacts"),
    path('Contacts/<int:id>/', contact_details, name="details"),
       
]
