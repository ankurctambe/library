from django.contrib.auth.models import User
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import login as auth_login,logout,authenticate
#from .views import*
from .models import*

# Create your views here.
def home(request):
    return render(request,"home.html")

def login(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(username=username,password=password)
        print(user)
        return redirect("library1")
    return render(request,"Login.html")

def register(request):
    if request.method=="POST":
        first_name=request.POST.get("fname",None)
        last_name=request.POST.get("lname",None)
        email=request.POST.get("email",None)
        password=request.POST.get("password",None)
        user=User.objects.create_user(username=email,email=email,first_name=first_name,last_name=last_name,password=password)
        print(user)
        return redirect("home")
    return render(request,"register.html")

def library1(request):
    if request.method=="POST":
        book=request.POST.get("book",None)
        quantity=request.POST.get("quantity",None)
        buyer=request.POST.get("buyer",None)
        dt=request.POST.get("dt",None)
        dr=request.POST.get("dr",None)
        
    #     counter=request.POST.get("count")
    # for i in range(int(counter)):
    #     book=request.POST.get("book"+str(i+1))
    #     quantity=request.POST.get("quantity"+str(i+1))
    #     buyer=request.POST.get("buyer"+str(i+1))
    #     dt=request.POST.get("dt"+str(i+1))
    #     dr=request.POST.get("dr"+str(i+1))

        Invoice.objects.create(book=book,quantity=quantity,buyer=buyer,dt=dt,dr=dr,user=request.user)
        return redirect("home")
    return render(request,"library1.html")


