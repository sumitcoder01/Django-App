from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        # Do something for not authenticated users.
        return redirect("/login")
    
    return render(request,'index.html')

def loginUser(request):
    if request.method =="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        #Check if user entered correct credentials
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")
        
    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")