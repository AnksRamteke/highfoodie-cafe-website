from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')


def FoodItem(request):
    return render(request, 'FoodItem.html')

def contact(request):
    messages.error(request,'Welcome to the contact Page')
    if request.method =='post':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        content = request.POST.get('content')
        
        if len(name)<2 or len(email)<3 or len(content)<4:
            messege.error(request,'Please fill the form correctly')
         else:
            contact = Contact (name = name,email = email , phone = phone, date = datetime.today())
            contact.save()
            messages.success(request, 'Form is submitted successfully!.')
    return render(request, 'contact.html')

def about(search):
    return render(request, 'sesarch.html')
