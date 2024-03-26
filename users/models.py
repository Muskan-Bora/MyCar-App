from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profilepic.png', upload_to='profile_pictures')
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
    
class Car(models.Model):
    carmodels = models.CharField(
        max_length=100,
        default='Mercedes Limousine A200'
    )

    def __str__(self):
        return self.carmodels
    
    
class Cust_TestDrive(models.Model):

    car_model = models.CharField(
        max_length = 100,
        default = 'Model Name'
    )

    Salutation = models.CharField(
        max_length=50,
        default='Mr/Mrs./Ms.'
    )

    FirstName = models.CharField(
        max_length=100,
        default='First Name'
    )

    LastName = models.CharField(
        max_length=200,
        default='Last Name'
    )

    EmailID = models.CharField(
        max_length=100,
        default='Email Id'
    )
    
    MobileNo = models.CharField(
        max_length=100,
        default='Mobile Number'
    )

    PreferredCity = models.CharField(
        max_length=500,
        default='Preferred City'
    )

    def __str__(self):
        return str(
            (
                self.car_model,
                self.Salutation,
                self.FirstName,
                self.LastName,
                self.EmailID,
                self.MobileNo,
                self.PreferredCity
            )
        )

class Financing(models.Model):

    Salutation = models.CharField(
        max_length=50,
        default='Mr/Mrs./Ms.'
    )

    FirstName = models.CharField(
        max_length=100,
        default='First Name'
    )

    LastName = models.CharField(
        max_length=200,
        default='Last Name'
    )

    EmailID = models.CharField(
        max_length=100,
        default='Email Id'
    )
    
    MobileNo = models.CharField(
        max_length=100,
        default='Mobile Number'
    )

    def __str__(self):
        return str(
            (
                self.Salutation,
                self.FirstName,
                self.LastName,
                self.EmailID,
                self.MobileNo
            )
        )


CATEGORYCHOICES = (
    ('LA','Limousine A200'),
    ('SGLA', 'SUV GLA220d 4Matic'),
    ('LC', 'Limousine C200'),
    ('SGLB', 'SUV GLB'),
    ('SEQB', 'SUV EQB350 4Matic'),
    ('LE', 'Limousine E220d'),
    ('SGLC', 'SUV GLC300 4Matic'),
    ('AMG', 'AMG SL55 4Matic + Roadster'),
    ('LM', 'Limousine Maybach S680 4Matic'),
    ('LEQS', 'Limousine EQS580 4Matic'),
    ('SM', 'SUV Maybach GLS600 4Matic'),
    ('SGLE', 'SUV GLE300d 4Matic'),
    ('SGLS', 'SUV GLS450 4Matic'),
    ('SEQE', 'SUV EQE500 4Matic'),
    ('LS', 'Limousine S350d '),
    ('AMGC', 'AMG C 43 4Matic')
)

class EmiModels(models.Model):
    prodcode = models.IntegerField(
        default = '50'
    )
    bodytype = models.CharField(max_length = 100)
    model_name = models.CharField(max_length = 100)
    category = models.CharField(choices=CATEGORYCHOICES, max_length=4)
    car_price = models.IntegerField(
        default = '1000'
    )
    down_payment = models.IntegerField(
        default = '1000'
    )
    fin_amount = models.IntegerField(
        default = '1000'
    )
    interest_rate = models.IntegerField(
        default = '5'
    )
    tenure_years = models.IntegerField(
        default='5'
    )
    emi = models.IntegerField(
        default = '1000'
    )
    image = models.ImageField(
        upload_to='EmiModels',
        default='https://emifreecar.com/images-new/offcer-coming-soon.jpg'
    )

    def __str__(self):
        return self.model_name

class ShopOnline(models.Model):
    prodshop_code = models.IntegerField(
        default='80'
    )

    car_body = models.CharField(
        max_length = 100,
        default = 'CarBody'
    )

    modelname = models.CharField(max_length=100)
    
    description = models.TextField(
        default = 'Lorem, ipsum dolor sit amet consectetur adipisicing elit. Dolor corrupti numquam suscipit itaque voluptas non ea voluptatibus assumenda aspernatur at tempora deserunt, velit quam, ex asperiores provident nisi. Minus, unde!'
    )
    
    fuel_type = models.CharField(
        max_length=20,
        default = 'fuel'
    )
    
    kW = models.CharField(
        max_length = 10,
        default='1'
    )
    
    image = models.ImageField(
        upload_to='ShopOnline',
        default='https://emifreecar.com/images-new/offcer-coming-soon.jpg'
    )

    price = models.IntegerField(
        default='1000'
    )

    monthly_emi = models.IntegerField(
        default='1000'
    )

    down_payment = models.IntegerField(
        default = '1000'
    )

    fin_amount = models.IntegerField(
        default = '1000'
    )

    tenure_months = models.IntegerField(
        default='48'
    )

    def __str__(self):
        return self.modelname

class shop_testdrive(models.Model):
    carmodel = models.CharField(
        max_length = 300,
        default = 'Mercedes Limousine A200'
    )

    salutation = models.CharField(
        max_length=50,
        default='Mr/Mrs./Ms.'
    )

    firstname = models.CharField(
        max_length=200,
        default = 'First Name'
    )

    lastname = models.CharField(
        max_length=200,
        default = 'Last Name'
    )

    email = models.EmailField(
        max_length = 300,
        default = 'Email'
    )

    MobileNo = models.IntegerField(
        default = '1234'
    )

    def __str__(self):
        return str(
            (
                self.carmodel,
                self.salutation,
                self.firstname,
                self.lastname,
                self.email,
                self.MobileNo,
            )
        )

class BuyNow(models.Model):
    carmodel = models.CharField(
        max_length = 300,
        default = 'Mercedes Limousine A200'
    )

    salutation = models.CharField(
        max_length=50,
        default='Mr/Mrs./Ms.'
    )

    firstname = models.CharField(
        max_length=200,
        default = 'First Name'
    )

    lastname = models.CharField(
        max_length=200,
        default = 'Last Name'
    )

    email = models.EmailField(
        max_length = 300,
        default = 'Email'
    )

    MobileNo = models.IntegerField(
        default = '1234'
    )

    def __str__(self):
        return str(
            (
                self.carmodel,
                self.salutation,
                self.firstname,
                self.lastname,
                self.email,
                self.MobileNo,
            )
        )
    
class Location(models.Model):
    name = models.CharField(
        max_length = 200,
        default = 'name'
    )

    state = models.CharField(
        max_length = 100,
        default = 'state'
    )

    city = models.CharField(
        max_length = 200,
        default = 'city'
    )
    pincode = models.IntegerField(
        default='000000'
    )

    def __str__(self):
        return str(
            (
                self.name,
                self.state,
                self.city,
                self.pincode
            )
        )

class Feedback(models.Model):
    name = models.CharField(
        max_length = 200,
        default = 'name'
    )

    satisfied = models.CharField(
        max_length = 200,
        default = 'satisfied'
    )

    recommend = models.CharField(
        max_length = 200,
        default = 'recommend'
    )

    def __str__(self):
        return str(
            (
                self.name,
                self.satisfied,
                self.recommend
            )
        )
    
class Feedback_satisfied(models.Model):
    Satisfied = models.CharField(
        max_length = 200,
        default = 'satisfied'
    )

    def __str__(self):
        return self.Satisfied