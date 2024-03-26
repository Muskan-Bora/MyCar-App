from django.urls import path, include
from car import views

urlpatterns = [
    # Home Page -------------------------------------
    path('home/', views.index, name='index'),

    # LatestModels Details Page ----------------------
    path('detail_latmodel/<int:LatestModel_id>/', views.detail_latmodel, name='detail_latmodel'),

    # Category Page (All Models of Cars) ----------------------
    path('category/<slug:val>', views.CategoryView.as_view(), name='category'),

    # Details Page of Category ----------------------------
    path('detail_category/<int:pk>/', views.detail_category.as_view(), name='detail_category'),

    # Buy Online Page ----------------------------------
    path('online/', views.online, name='online'),

    # Details Page of Online ----------------------------
    path('detail_online/<int:MBOnline_id>/', views.detail_online, name='detail_online'),

    # Service Page --------------------------------------
    path('service/', views.Services, name='Services'),

    # Brand Page ----------------------------------
    path('brand/', views.Brands, name='Brands'),

    # To Add New Models ------------------------------
    path('addmodels/', views.create_MBModel, name='create_MBModel'),

    # To Add New Buy Online Models ---------------------
    path('addonline/', views.create_MBOnline, name='create_MBOnline'),

    # To Edit Models ------------------------------------
    path('updatemodel/<int:id>/', views.update_MBModel, name='update_MBModel'),

    # To Delete Models ----------------------------------
    path('deletemodel/<int:id>/', views.delete_MBModel, name='delete_MBModel'),

    # To Update Buy Online Models ----------------------------
    path('updateonline/<int:id>/', views.update_MBOnline, name='update_MBOnline'),

    # To Delete Buy Online Models ---------------------------
    path('deleteonline/<int:id>/', views.delete_MBOnline, name='delete_MBOnline'),

    # To Add Latest Models ------------------------------------
    path('addlatmodels/', views.create_latmodel, name='create_latmodel'),

    # To Edit Latest Models -------------------------------
    path('updatelatmodels/<int:id>/', views.update_latmodel, name='update_latmodel'),

    # To Delete Latest Models --------------------------
    path('deletelatmodel/<int:id>/', views.delete_latmodel, name='delete_latmodel'),

    # To Add Services ----------------------------
    path('addservice/', views.create_service, name='create_service'),

    # To Add Brand ------------------------------------------
    path('addbrand/', views.create_brand, name='create_brand'),
]