from django.shortcuts import render,HttpResponse
#from datetime import datetime
from newapp.models import Contact

# Create your views here.
def index(request):
    context={
        "variable":"this is sent"
    }
    return render(request,"index.htm",context)
    #return HttpResponse("this is the homepage")
def home(request):
    return render(request,"index.htm")
def about(request):
    return render(request,"about.htm")
    #return HttpResponse("this is the aboutpage")
def contact(request):
    if request.method=="POST":
        email=request.POST.get("email")
        query=request.POST.get("query")
        #notify=request.POST.get("notify")
        contact=Contact(email=email,query=query)
        #date=datetime.today()
        contact.save()

    return render(request,"contact.htm")
    #return HttpResponse("this is the contactpage")
def flavours(request):
    return render(request,"flavours.htm") 
    #return HttpResponse("this is the servicespage")
def helloworld(request):
    return HttpResponse("Hello World")
def connectwithus(request):
    return HttpResponse("connect with us")