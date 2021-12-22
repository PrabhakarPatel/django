from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    context = {
        "variable":"this is your text",
        "variable1":"this is your text1"
    }
    return render(request,"index.html",context)
    # return HttpResponse("this is homepage") 

def about(request):
    return render(request,"about.html")
def services(request):
    return render(request,"services.html",)
    # return HttpResponse("this is services page") 
def contact(request):
    if request.method == "POST":
        email =request.POST.get('email')
        password =request.POST.get('password')
        address =request.POST.get('address')
        city =request.POST.get('city')
        state =request.POST.get('state')
        zip =request.POST.get('zip')
        contact = Contact(email=email,password=password,address=address,city=city,state=state,zip=zip,date=datetime.today())
        contact.save()
        messages.success(request, 'your message has been sent')
    return render(request,"contact.html",)
    # return HttpResponse("this is contact page") 
