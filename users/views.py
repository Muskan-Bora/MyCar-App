from django.shortcuts import render, redirect, reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from users.forms import RegisterForm, ProfForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from users.models import Profile
from .forms import TestDriveForm
from .models import Car, Cust_TestDrive
from .forms import FinancingForm
from .models import Financing
from .forms import EmiModelForm
from django.views import View
from .models import EmiModels
from .models import ShopOnline
from .forms import shoptestdriveform
from .models import shop_testdrive
from .forms import BuyNowform
from .models import BuyNow
from .forms import Locationform
from .models import Location
from .forms import FeedbackForm
from .models import Feedback
from .models import Feedback_satisfied


# Create your views here.

# Register/Sign Up Page --------------------------------
def register(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request,
                'Welcome {}, your account has been scuccessfully created. Now you may login below'.format(username)
            )
            return redirect('login')
    else:
        form = RegisterForm()
    
    context = {
        'form':form
    }

    return render(request, 'users/register.html', context)


# Login Page ------------------------------------
def login_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.success(
                request,
                'Invalid Login, try again'.format(user)
            )
            return redirect('login')

        elif user.is_superuser:
            login(request, user)
            messages.success(
                request, 
                'Welcome {} A SuperUser, you have been logged in successfully'.format(user)
            )
            return redirect('index')

        elif user is not None:
            login(request, user)
            messages.success(
                request,
                'Welcome {}, you have been logged in successfully'.format(user)
        )
        return redirect('index')
        
    return render(request, 'users/login.html')


# LogOut Page ----------------------------------------
def logout_view(request):

    if request.method == 'POST':
        user = request.user.username
        logout(request)
        messages.success(
            request,
            '{}, you have been logged out successfully'.format(user)
        )
        return redirect('index')
    
    return render(request, 'users/logout.html')


# Profile Page ---------------------------------------
def ProfilePage(request):
    prof = Profile.objects.get(id = request.user.id)

    if not request.user.is_authenticated:
        return redirect('login')
    
    context = {
        'prof':prof
    }

    return render(request, 'users/profile.html', context)


# Profile Form Page -------------------------------------
def ProfileForm(request, prof_id):
    prof = Profile.objects.get(id=prof_id)

    form = ProfForm(request.POST or None, request.FILES or None, instance=prof)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form':form
    }

    return render(request, 'users/profform.html', context)


# Test Drive Form --------------------------------------
def test_drive(request):

    if request.method == 'POST':
        form = TestDriveForm(request.POST)
        if form.is_valid():
            car_model = form.cleaned_data['car_model']
            Salutation = form.cleaned_data['salutation']
            FirstName = form.cleaned_data['FirstName']
            LastName = form.cleaned_data['LastName']
            EmailID = form.cleaned_data['EmailID']
            MobileNo = form.cleaned_data['MobileNo']
            PreferredCity = form.cleaned_data['PreferredCity']
            
            CustTestDrive = Cust_TestDrive.objects.create(
                car_model = car_model,
                Salutation = Salutation,
                FirstName = FirstName,
                LastName = LastName,
                EmailID = EmailID,
                MobileNo = MobileNo,
                PreferredCity = PreferredCity
            )
            messages.success(
                request,
                'Thank You!.. Your Test Drive has Booked Successfully. We will contact you Shortly..'
            )

            return redirect('index')
        
    else:
        form = TestDriveForm()

    context = {
        'form':form
    }

    return render(request, 'users/testdrive-form.html', context)


# Finance Form ---------------------------------------
def finance(request):
    return render(request, 'users/Finance.html')

def finance_form(request):

    if request.method == 'POST':
        form = FinancingForm(request.POST)
        if form.is_valid():

            Salutation = form.cleaned_data['Salutation']
            FirstName = form.cleaned_data['FirstName']
            LastName = form.cleaned_data['LastName']
            EmailID = form.cleaned_data['EmailID']
            MobileNo = form.cleaned_data['MobileNo']
            
            Finance = Financing.objects.create(
                Salutation = Salutation,
                FirstName = FirstName,
                LastName = LastName,
                EmailID = EmailID,
                MobileNo = MobileNo,
            )
            messages.success(
                request,
                'Thank You!.. We will contact you Shortly..'
            )

            return redirect('index')
        
    else:
        form = FinancingForm()

    context = {
        'form':form
    }

    return render(request, 'users/Finance-Form.html', context)


# EMI Models -------------------------------------
def emimodel(request):
    if request.method == 'POST':
        form = EmiModelForm(request.POST)
        if form.is_valid():
            model_names_id = form.cleaned_data['model_names']
            modelname_data = EmiModels.objects.get(id = model_names_id)
            
            return render(request, 'users/EMI.html', { 'modelname_data':modelname_data })
    
    else:
        form = EmiModelForm()
    

    context = {
        'form':form
    }

    return render(request, 'users/EMI.html', context)


# Shop Online ---------------------------------------
def shoponline(request):

    shop_online = ShopOnline.objects.all()

    context = {
        'shop_online':shop_online
    }

    return render(request, 'users/ShopOnline.html', context)


# Details of Shop Online ----------------------------
def detail_shop(request, ShopOnline_id):

    detailshop = ShopOnline.objects.get(id = ShopOnline_id)

    context = {
        'detailshop':detailshop
    }

    return render(request, 'users/detail_shop.html', context)


# Shop - TestDrive Form Page --------------------------------
def Shop_TestDrive(request):

    if request.method == 'POST':
        form = shoptestdriveform(request.POST)
        if form.is_valid():
            carmodel = form.cleaned_data['carmodel']
            salutation = form.cleaned_data['salutation']
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            email = form.cleaned_data['email']
            MobileNo = form.cleaned_data['MobileNo']
            
            shoptestdrive = shop_testdrive.objects.create(
                carmodel = carmodel,
                salutation = salutation,
                firstname = firstname,
                lastname = lastname,
                email = email,
                MobileNo = MobileNo,
            )
            messages.success(
                request,
                'Thank You!.. Your Test Drive has Booked Successfully. We will contact you Shortly..'
            )

            return redirect('index')
        
    else:
        form = shoptestdriveform()

    context = {
        'form':form
    }

    return render(request, 'users/shop_testdrive-form.html', context)


# Buy Now Form Page ---------------------------------------
def buy_now(request):

    if request.method == 'POST':
        form = BuyNowform(request.POST)
        if form.is_valid():
            carmodel = form.cleaned_data['carmodel']
            salutation = form.cleaned_data['salutation']
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            email = form.cleaned_data['email']
            MobileNo = form.cleaned_data['MobileNo']
            
            BUYNOW = BuyNow.objects.create(
                carmodel = carmodel,
                salutation = salutation,
                firstname = firstname,
                lastname = lastname,
                email = email,
                MobileNo = MobileNo,
            )
            messages.success(
                request,
                'Congratulations!.. Your Mercedes Benz has Booked Successfully. We will contact you soon. Thank You!..'
            )

            return redirect('index')
        
    else:
        form = BuyNowform()

    context = {
        'form':form
    }

    return render(request, 'users/buynow-form.html', context)


# Location -----------------------------------------
def location(request):

    if request.method == 'POST':
        form = Locationform(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            state = form.cleaned_data['state']
            city = form.cleaned_data['city']
            pincode = form.cleaned_data['pincode']

            loc = Location.objects.create(
                name = name,
                state = state,
                city = city,
                pincode = pincode
            )
            messages.success(
                request,
                'Your Location has Registered successfully'
            )

            return redirect('index')
        
    else:
        form = Locationform()

    context = {
        'form':form
    }

    return render(request, 'users/location-form.html', context)


# FeedBack Form ---------------------------------------
def feedback(request):

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            satisfied = form.cleaned_data['Satisfied']
            recommend = form.cleaned_data['recommend']
            
            feed = Feedback.objects.create(
                name = name,
                satisfied = satisfied,
                recommend = recommend
            )
            messages.success(
                request,
                'Thank You!.. For your Valuable Feedback..'
            )

            return redirect('index')
        
    else:
        form = FeedbackForm()

    context = {
        'form':form
    }

    return render(request, 'users/Feedback-form.html', context)
