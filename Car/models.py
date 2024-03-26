from django.db import models

# Create your models here.

CATEGORY_CHOICES=(
    ('LM','Limousine'),
    ('SR', 'SUV Range'),
    ('HB', 'Hatchback'),
    ('CP', 'Coupes'),
    ('RS', 'Roadsters'),
)

class MBModel(models.Model):
    prod_code = models.IntegerField(default=50)
    body_type = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    description = models.TextField(
        default='Lorem, ipsum dolor sit amet consectetur adipisicing elit. Dolor corrupti numquam suscipit itaque voluptas non ea voluptatibus assumenda aspernatur at tempora deserunt, velit quam, ex asperiores provident nisi. Minus, unde!'
    )
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    mb_image = models.ImageField(
        upload_to='MBModel',
        default='https://emifreecar.com/images-new/offcer-coming-soon.jpg'
    )

    def __str__(self):
        return self.name
    

class MBOnline(models.Model):
    prodOnline_code = models.IntegerField(default=50)
    
    carbody = models.CharField(max_length=50)
    
    model_name = models.CharField(max_length=100)
    
    description = models.TextField(
        default = 'Lorem, ipsum dolor sit amet consectetur adipisicing elit. Dolor corrupti numquam suscipit itaque voluptas non ea voluptatibus assumenda aspernatur at tempora deserunt, velit quam, ex asperiores provident nisi. Minus, unde!'
    )
    
    fueltype = models.CharField(
        max_length=20,
        default = 'fuel'
    )
    
    kW = models.CharField(
        max_length = 10,
        default='1'
    )
    
    online_image = models.ImageField(
        upload_to='MBOnline',
        default='https://emifreecar.com/images-new/offcer-coming-soon.jpg'
    )
    
    Exterior = models.TextField(
        default='Ext'
    )
    
    Exterior_image = models.ImageField(
        upload_to='MBOnline',
        default='https://emifreecar.com/images-new/offcer-coming-soon.jpg'
    )
    
    Interior = models.TextField(
        default='Int'
    )
    
    Interior_image = models.ImageField(
        upload_to='MBOnline',
        default='https://emifreecar.com/images-new/offcer-coming-soon.jpg'
    )

    RadioCommunication = models.TextField(
        default='Navigation'
    )

    RadCom_image = models.ImageField(
        upload_to='MBOnline',
        default='https://emifreecar.com/images-new/offcer-coming-soon.jpg'
    )
    
    SecurityTech = models.TextField(
        default='Active Parking'
    )

    SecurityTech_image = models.ImageField(
        upload_to='MBOnline',
        default='https://emifreecar.com/images-new/offcer-coming-soon.jpg'
    )
    
    Price = models.IntegerField(
        default='1000'
    )

    def __str__(self):
        return self.model_name

class LatestModel(models.Model):
    prodlatMod_code = models.IntegerField(default=10)
    carbody = models.CharField(max_length=50)
    model_name = models.CharField(max_length=100)
    fueltype = models.CharField(
        max_length=20,
        default = 'fuel'
    )
    latestmodel_image = models.ImageField(
        upload_to='LatestModel',
        default='https://emifreecar.com/images-new/offcer-coming-soon.jpg'
    )
    Exterior = models.ImageField(
        upload_to='LatestModel',
        default='https://emifreecar.com/images-new/offcer-coming-soon.jpg'
    )
    Interior = models.ImageField(
        upload_to='LatestModel',
        default='https://emifreecar.com/images-new/offcer-coming-soon.jpg'
    )
    Price = models.IntegerField(
        default='1000'
    )

    def __str__(self):
        return self.model_name
    
class Service(models.Model):
    service_code = models.IntegerField(default=10)
    
    category_service = models.CharField(
        max_length = 250,
        default = 'category'
    )

    subcategory = models.CharField(
        max_length = 500,
        default = 'subcategory'
    )

    description = models.TextField(
        default = 'Lorem, ipsum dolor sit amet consectetur adipisicing elit. Eligendi fuga illum amet libero nihil deserunt eius rerum a. Dolorem sapiente id quidem consequuntur est dolore perferendis sunt nihil deleniti reprehenderit. Dolor, laudantiumeru as.'
    )

    image = models.ImageField(
        upload_to='Service',
        default='https://emifreecar.com/images-new/offcer-coming-soon.jpg'
    )

    def __str__(self):
        return self.category_service
    
class Brand(models.Model):
    brand_code = models.IntegerField(default=10)

    category_brand = models.CharField(
        max_length = 250,
        default = 'Mercedes Brand'
    )

    description = models.TextField(
        default = 'Lorem, ipsum dolor sit amet consectetur adipisicing elit. Eligendi fuga illum amet libero nihil deserunt eius rerum a. Dolorem sapiente id quidem consequuntur est dolore perferendis sunt nihil deleniti reprehenderit. Dolor, laudantiumeru as.'
    )

    image = models.ImageField(
        upload_to='Brand',
        default='https://emifreecar.com/images-new/offcer-coming-soon.jpg'
    )

    def __str__(self):
        return self.category_brand