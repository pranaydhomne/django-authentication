from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages



def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']
        email = request.POST['email']

        # Check if the passwords match
        if password != confirm_password:
            messages.warning(request,'passward not match')
            return render(request, 'signup.html', {'error_message': error_message})

        # Check if the username is already taken
        if User.objects.filter(username=username).exists():
            error_message = "Username is already taken."
            return render(request, 'signup.html', {'error_message': error_message})

        # Check if the email is already registered
        if User.objects.filter(email=email).exists():
            error_message = "Email is already registered."
            return render(request, 'signup.html', {'error_message': error_message})

        # Create a new user
        user = User.objects.create_user(username=username, password=password, email=email)
        messages.success(request,'signup successfully')
        # Redirect to a success page or login page
        # print(username , password,email)
        return redirect('login')

    return render(request, 'signup.html')




def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate the user
        user = authenticate(username=username, password=password)

        if user is not None:
            # User credentials are valid, log in the user
            login(request,user)
            messages.success(request,'login successfully')
            return redirect('/')  # Redirect to the dashboard or any other page
        else:
            # User credentials are invalid, show an error message
            error_message = "Invalid username or password."
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')


@login_required(login_url='/login/')
def home(request):

    return render(request,"index.html")

def user_logout(request):
    logout(request)
    messages.success(request,'logout successfully')
    return redirect('/login')
