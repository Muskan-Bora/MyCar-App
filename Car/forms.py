from django import forms
from car.models import MBModel
from car.models import MBOnline
from car.models import LatestModel
from car.models import Service
from car.models import Brand

class MBModelForm(forms.ModelForm):
    class Meta:
        model = MBModel
        fields = ['prod_code', 'body_type', 'name', 'description', 'category', 'mb_image']

class MBOnlineForm(forms.ModelForm):
    class Meta:
        model = MBOnline
        fields = ['prodOnline_code', 'carbody', 'model_name', 'description', 'fueltype', 'kW', 'online_image', 'Exterior', 'Exterior_image', 'Interior', 'Interior_image', 'RadioCommunication', 'RadCom_image', 'SecurityTech', 'SecurityTech_image', 'Price']

class LatestModelForm(forms.ModelForm):
    class Meta:
        model = LatestModel
        fields = ['prodlatMod_code', 'carbody', 'model_name', 'fueltype', 'latestmodel_image', 'Exterior', 'Interior', 'Price']

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['service_code', 'category_service', 'subcategory', 'description', 'image']

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['brand_code', 'category_brand', 'description', 'image']