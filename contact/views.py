from email import message

from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from .models import Contact

def home(request):
    message = "hello friends!"
    context = {'message' : message}
    return render(request, "page/index.html", context) 

def about(request):
    return render(request, "page/about.html")

def contact_list(request):
    Contacts = Contact.objects.all()
    return render(request, "Contacts/contact_list.html", {"Contacts": Contacts})

def contact_details(request, id):
    contact = get_object_or_404(Contact, id=id)
    
    return render(request, "Contacts/contact_details.html", {"contact": contact})