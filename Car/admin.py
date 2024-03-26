from django.contrib import admin
from car.models import MBModel
from car.models import MBOnline
from car.models import LatestModel
from car.models import Service
from car.models import Brand

# Register your models here.

admin.site.register(MBModel)
admin.site.register(MBOnline)
admin.site.register(LatestModel)
admin.site.register(Service)
admin.site.register(Brand)