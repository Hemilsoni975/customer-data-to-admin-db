from django.shortcuts import render , HttpResponse
from datetime import datetime
from soni.models import Contact
from django.contrib import messages
# Create your views here.

def home(request):
     return render(request,'home.html')

def aboutus(request):
     return render(request,'about.html')

def service(request):
     return render(request,'service.html')

def contact(request):
     if request.method == 'POST':
          name = request.POST.get('name')
          email = request.POST.get('email')
          phone = request.POST.get('phone')
          describe = request.POST.get('describe')
          contact = Contact(name = name , email = email , phone = phone , describe = describe , date = datetime.today())
          contact.save()
          messages.success(request, "YOUR MESSAGE HAS BEEN SEND SUCCESSFULLY!")
     return render(request,'contact.html')
