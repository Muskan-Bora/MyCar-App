from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from .models import Car, Cust_TestDrive
from .models import Financing
from.models import EmiModels
from .models import shop_testdrive
from .models import BuyNow
from .models import Location
from .models import Feedback_satisfied
from .models import Feedback


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class ProfForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'image', 'location']
        
class TestDriveForm(forms.Form):
    car_model = forms.ModelChoiceField(queryset=Car.objects.all(), empty_label="Mercedes Limousine A200")
    Salutation = forms.CharField(max_length=50)
    FirstName = forms.CharField(max_length=100)
    LastName = forms.CharField(max_length=200)
    EmailID = forms.CharField(max_length=100)
    MobileNo = forms.CharField(max_length=100)
    PreferredCity = forms.CharField(max_length=500)

    class Meta:
        model = Cust_TestDrive
        fields = ['Salutation', 'FirstName', 'LastName', 'EmailID', 'MobileNo', 'PreferredCity']

class FinancingForm(forms.Form):
    Salutation = forms.CharField(max_length=50)
    FirstName = forms.CharField(max_length=100)
    LastName = forms.CharField(max_length=200)
    EmailID = forms.CharField(max_length=100)
    MobileNo = forms.CharField(max_length=100)
    class Meta:
        model = Financing
        fields = ['Salutation', 'FirstName', 'LastName', 'EmailID', 'MobileNo']

class EmiModelForm(forms.Form):
    model_name = EmiModels.objects.all().values_list('id', 'model_name') 
    model_names = forms.ChoiceField(choices=model_name)
    class Meta:
        model = EmiModels
        fields = ['model_name']

class shoptestdriveform(forms.Form):
    carmodel = forms.CharField(max_length=300)
    salutation = forms.CharField(max_length=50)
    firstname = forms.CharField(max_length=200)
    lastname = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=300)
    MobileNo = forms.IntegerField()
    class Meta:
        model = shop_testdrive
        fields = ['carmodel', 'salutation', 'firstname', 'lastname', 'email', 'MobileNo']

class BuyNowform(forms.Form):
    carmodel = forms.CharField(max_length=300)
    salutation = forms.CharField(max_length=50)
    firstname = forms.CharField(max_length=200)
    lastname = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=300)
    MobileNo = forms.IntegerField()
    class Meta:
        model = BuyNow
        fields = ['carmodel', 'salutation', 'firstname', 'lastname', 'email', 'MobileNo']

class Locationform(forms.Form):
    name = forms.CharField(max_length=200)
    state = forms.CharField(max_length=100)
    city = forms.CharField(max_length=200)
    pincode = forms.IntegerField()
    class Meta:
        model = Location
        fields = ['name', 'state', 'city', 'pincode']

class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=200)
    Satisfied = forms.ModelChoiceField(queryset=Feedback_satisfied.objects.all(), empty_label="----- SELECT ----")
    recommend = forms.CharField(max_length=200)
    class Meta:
        model = Feedback
        fields = ['name', 'Satisfied', 'recommend']
    