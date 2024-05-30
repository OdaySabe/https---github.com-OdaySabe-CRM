from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

def login_user(request):
    if request.method=='GET':
        return render(request,"login.html",{"pagename":"loginpage"})
    elif request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse("home_app:home"))
        else:
            return render(request, "login.html", {"pagename": "loginpage","Error_message":"Invalid username or password"})


def logout_user(request):
    logout(request)
    return redirect(reverse('login:login'))
    
    # elif request.method=='POST':
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
    #     try:
    #         user = User.objects.get(username=username)
    #         if check_password(password, user.password):
    #             request.session['user'] = user.id
    #             return redirect('/home')
    #         else:
    #             raise User.DoesNotExist
    #     except User.DoesNotExist:
    #         return render(request, "login.html", {"pagename": "loginpage","Error_message":"Invalid username or password"})


        
