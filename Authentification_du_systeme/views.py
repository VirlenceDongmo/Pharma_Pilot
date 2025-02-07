from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
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



def logout_view(request):
    logout(request)
    return render(request, 'welcome.html')


# verification de l'existance de l'adresse email

def email_checking(request):
    if request.method=="POST":
        email = request.POST.get('email')
        
        if not email:
            messages.error(request, "Please enter an valid email address.")
            return render(request,'emailChecking.html')
        
        user = User.objects.filter(email=email).first

        if user:
            return redirect('updatePassword', email=email)
        else :
            messages.error(request,"Please this email doesn't exit, try with another one or create an account.")
            return redirect('emailChecking.html')
        
    return render(request, 'emailChecking.html')



# changement de mot de pass

def update_password(request, email):
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        messages.error(request, "User doesn't exists, try with another email address or create an account.")
        return redirect('emailChecking')
    
    if request.method=="POST":
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        if password != password_confirm:
            messages.error(request, "passwords are not the same, please try again !")
            return redirect('sign_up')

        if len(password) < 8 or not re.search(r'[A-Za-z]', password) or not re.search(r'\d', password) or not re.search(r'[!@#$%^&*(),-_+=<>?/;"\'\`~:{}[\]|]', password):
            messages.error(request,"The password must contains at least 8 characters, including letters, numbers and specials characters")
            return render('sign_up')
        
        user.set_password(password)
        user.save()
        messages.success(request, "Your password was updated successfully. You can sign in.")

        return redirect('login')
    
    context={'email': email}

    return render(request, 'updatePassword.html', context)
