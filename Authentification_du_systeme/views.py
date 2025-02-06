from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
import re
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User



def sign_up_view(request):
    if request.method=="POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        if password != password_confirm:
            messages.error(request, "passwords are not the same, please try again !")
            return redirect('sign_up')

        if len(password) < 8 or not re.search(r'[A-Za-z]', password) or not re.search(r'\d', password) or not re.search(r'[!@#$%^&*(),-_+=<>?/;"\'\`~:{}[\]|]', password):
            messages.error(request,"The password must contains at least 8 characters, including letters, numbers and specials characters")
            return render('sign_up')
        
        try :
            validate_email(email)
        except ValidationError:
            messages.error(request, "Your email address is invalid, please try again.")
            return render('sign_up')
        
        if User.objects.filter(username=username).exists():
            messages.error=(request,"This username already exists on this app, please try again whith another one.")
            return render('sign_up')
        
        if User.objects.filter(email=email).exists():
            messages.error=(request,"This email address already exists on this app, please try again whith another one.")
            return render('sign_up')
        
        User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, "Account created successfully ! Now you can login")

        return redirect('login')
    return render(request, 'sign_up.html')





def login_view(request):

    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('welcome')
        else:
            messages.error(request, "Invalid username or password !")

            return redirect('login')
    return render(request, 'login.html')
