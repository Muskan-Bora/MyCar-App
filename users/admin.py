from django.contrib import admin
from users.models import Profile
from users.models import Car
from users.models import Cust_TestDrive
from users.models import Financing
from users.models import EmiModels
from users.models import ShopOnline
from users.models import shop_testdrive
from users.models import BuyNow
from users.models import Location
from users.models import Feedback
from users.models import Feedback_satisfied

# Register your models here.

admin.site.register(Profile)
admin.site.register(Car)
admin.site.register(Cust_TestDrive)
admin.site.register(Financing)
admin.site.register(EmiModels)
admin.site.register(ShopOnline)
admin.site.register(shop_testdrive)
admin.site.register(BuyNow)
admin.site.register(Location)
admin.site.register(Feedback)
admin.site.register(Feedback_satisfied)