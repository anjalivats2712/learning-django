from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,"index.htm")
    #return HttpResponse("this is the homepage")
def about(request):
    return HttpResponse("this is the aboutpage")
def contact(request):
    return HttpResponse("this is the contactpage")
def services(request):
    return HttpResponse("this is the servicespage")