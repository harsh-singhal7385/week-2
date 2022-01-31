from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from user_auth.models import UserData
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

session = {}
session['check_in'] = False

def loginUser(request):
    print("in /login page")
    if request.method == "POST":
        data_email = request.POST['email']
        data_password = request.POST['password']
        user = authenticate(username = data_email, password = data_password)
        
        if user == None:
            print("Invalid credentials")
            return render(request, 'user_auth/login.html')
        else:
            login(request,user)
            return redirect('/blog/')
         
    return render(request, 'user_auth/login.html')


def signupUser(request):
    print("in /signup page")
    if request.method == "POST":
        firstname_data = request.POST['fname']
        lastname_data = request.POST['lname']
        email_data = request.POST['email']
        mobile_data = request.POST['mobile']
        password_data = request.POST['password']

        
        myobj = User.objects.create_user(username=email_data,email = email_data, password = password_data)
        myobj.first_name = firstname_data
        myobj.last_name = lastname_data
        myobj.mobile = mobile_data
        
        myobj.save()
        
        return redirect('/user_auth/accounts/login/')
    
    return render(request, 'user_auth/signup.html')  

def logoutUser(request):
    logout(request)
    print("logout")
    return redirect('/')
