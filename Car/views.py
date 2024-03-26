from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import LatestModel
from .models import MBModel
from .models import MBOnline
from .models import Service
from .models import Brand
from car.forms import MBModelForm
from car.forms import MBOnlineForm
from car.forms import LatestModelForm
from car.forms import ServiceForm
from car.forms import BrandForm

# Create your views here.

# Index Page --------------------------------
def index(request):
    Model = LatestModel.objects.all()

    context = {
        'Model':Model
    }

    return render(request, 'car/index.html', context)


# Detail of Latest Models ------------------------
def detail_latmodel(request, LatestModel_id):

    detaillatmodel = LatestModel.objects.get(id=LatestModel_id)

    context = {
        'detaillatmodel':detaillatmodel
    }

    return render(request, 'car/detail_latmodel.html', context)


# Category Page -----------------------------------------    
class CategoryView(View):
    def get(self, request, val):
        
        CarModel = MBModel.objects.filter(category=val)
        
        return render(request, 'car/category.html', locals())
    

# Details of Category ------------------------------------    
class detail_category(View):
    def get(self, request, pk):

        CarModel = MBModel.objects.get(pk = pk)

        return render(request, 'car/detail_category.html', locals())


# Buy Online Page --------------------------------
def online(request):

    buyonline = MBOnline.objects.all()

    context = {
        'buyonline':buyonline
    }

    return render(request, 'car/online.html', context)


# Details of Buy Online Page -------------------------------------
def detail_online(request, MBOnline_id):

    detailonline = MBOnline.objects.get(id=MBOnline_id)

    context={
        'detailonline':detailonline
    }

    return render(request, 'car/detail_online.html', context)


# Service Page -----------------------------------------
def Services(request):

    SERVICES = Service.objects.all()

    context = {
        'SERVICES':SERVICES
    }

    return render(request, 'car/service.html', context)


# Brand Page ---------------------------------------------
def Brands(request):

    BRANDS = Brand.objects.all()

    context = {
        'BRANDS':BRANDS
    }

    return render(request, 'car/brand.html', context)


# Create All Models Page ----------------------------------------
def create_MBModel(request):
    form = MBModelForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('index')

    context = {
        'form':form
    }

    return render(request, 'car/model-form.html', context)


# Create Buy Online Models Page -----------------------------------
def create_MBOnline(request):
    form = MBOnlineForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('index')

    context = {
        'form':form
    }

    return render(request, 'car/online-form.html', context)


# To Update/Edit All Models Page -------------------------
def update_MBModel(request, id):

    mbmodel = MBModel.objects.get(pk=id)
    form = MBModelForm(request.POST or None, instance=MBModel)

    if form.is_valid():
        form.save()
        return redirect('index')

    context = {
        'form':form
    }
    
    return render(request, 'car/model-form.html', context)


# Delete All Models Page ----------------------------
def delete_MBModel(request, id):

    mbmodel = MBModel.objects.get(pk=id)

    if request.method == 'POST':
        mbmodel.delete()
        return redirect('index')

    context ={
        'mbmodel':mbmodel
    }

    return render(request, 'car/model-delete.html', context)


# Update/Edit Buy Online Page -----------------------------
def update_MBOnline(request, id):

    mbonline = MBOnline.objects.get(pk=id)
    form = MBOnlineForm(request.POST or None, instance=MBOnline)

    if form.is_valid():
        form.save()
        return redirect('index')

    context = {
        'form':form
    }

    return render(request, 'car/online-form.html', context)


# Delete Buy Online Page --------------------------------------- 
def delete_MBOnline(request, id):

    mbonline = MBOnline.objects.get(pk=id)

    if request.method == 'POST':
        mbonline.delete()
        return redirect('index')

    context = {
        'mbonline':mbonline
    }

    return render(request, 'car/online-delete.html', context)


# To Create Latest Models Page -------------------------------
def create_latmodel(request):

    form = LatestModelForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('index')

    context = {
        'form':form
    }

    return render (request, 'car/latestmodel-form.html', context)


# To Update Latest Models Page -------------------------------
def update_latmodel(request, id):

    updlatmodel = LatestModel.objects.get(pk=id)
    form = LatestModelForm(request.POST or None, instance=LatestModel)

    if form.is_valid():
        form.save()
        return redirect('index')

    context = {
        'form':form
    }

    return render(request, 'car/latestmodel-form.html', context)


# To Delete Latest Models Page -------------------------------
def delete_latmodel(request, id):

    latmodel = LatestModel.objects.get(pk=id)

    if request.method == 'POST':
        latmodel.delete()
        return redirect('index')

    context = {
        'latmodel':latmodel
    }

    return render(request, 'car/latmodel-delete.html', context)


# To Add New Services ---------------------------
def create_service(request):

    form = ServiceForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('index')

    context = {
        'form':form
    }

    return render (request, 'car/service-form.html', context)


# To Add New Brands ------------------------------------
def create_brand(request):

    form = BrandForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('index')

    context = {
        'form':form
    }

    return render (request, 'car/brand-form.html', context)

