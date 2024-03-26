from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    # Test Drive Form Page --------------------------------
    path('testdrive-form/', views.test_drive, name='test_drive'),

    # Finance Page ----------------------------------
    path('Finance/', views.finance, name='finance'),

    # Fianace-Form Page -----------------------------
    path('Finance-Form/', views.finance_form, name='finance_form'),

    # EMI page -------------------------------------
    path('EMI/', views.emimodel, name='emimodel'),

    # Shop Online Page --------------------------------
    path('ShopOnline/', views.shoponline, name='shoponline'),

    # Details of Shop Online Page -----------------------
    path('detail_shop/<int:ShopOnline_id>/', views.detail_shop, name='detail_shop'),

    # Shop-TestDrive Form --------------------------------
    path('shop_testdrive-form/', views.Shop_TestDrive, name='Shop_TestDrive'),

    # Buy Now Form ------------------------------
    path('buynow-form/', views.buy_now, name='buy_now'),

    # Location Form ----------------------------
    path('location-form/', views.location, name='location'),

    # Feedback Form --------------------------------
    path('Feedback-form/', views.feedback, name='feedback'),
]