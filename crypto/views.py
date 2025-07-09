from django.shortcuts import render
from .forms import LoginForm, RegistrationForm
from .models import LoginFormModel, RegistrationModel
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from .utils import calculate_file_hash
import os
import cv2 as cv
import hashlib


# Create your views here.


#registration view

def register(request):
    saved = False

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            model = RegistrationModel()
            model.firstname = form.cleaned_data['FirstName']
            model.lastname = form.cleaned_data['LastName']
            model.email = form.cleaned_data['email']
            model.password = form.cleaned_data['password']
            model.save()
            saved = True
            return redirect(reverse("share"))
        
        else:
            messages.error(request, "invalid characters entered, please double check")
    else:
        form = RegistrationForm()
    return render(request, "registration.html")



def login(request,):
    current_dir = os.path.dirname(__file__)
    company_share_path = os.path.join(current_dir, 'company_share.png')

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        users_share = request.FILES['share']
        company_share_hash = calculate_file_hash(company_share_path)  # Assuming the company's share image is stored as 'company_share.png'
        # Calculate the hash of the user's share image
       
        
        def calculate_file_hash_from_image(users_share):
            # Calculate the hash of the uploaded image
            file_hash = hashlib.md5(users_share.read()).hexdigest()
            users_share.seek(0)
            return file_hash
        users_share_hash = calculate_file_hash_from_image(users_share)
        
        register = RegistrationModel.objects.filter(email=email,password=password).first()

        if register:
            if (company_share_hash == users_share_hash):
                    messages.success(request, "Your encrypted image was validated successfully, Welcome!")
                    return redirect(reverse("dashboard"))
            else:
                    messages.error(request, "Your share image dosen't match ours, visual decryption failed!")
        else:
                 messages.error(request, "You entered a wrong password or email, Please retry!")
       

    else:
        login = LoginForm()
    return render(request, "login.html")


def dashboard(request):
    return render(request, "dashboard.html")

def share(request):
    return render(request, "user_share_image.html")



def home(request):
    return render(request, "home.html")



     


                





        


















