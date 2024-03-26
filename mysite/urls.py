"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from users import views as userviews

urlpatterns = [
    # Admin Page ------------------------------
    path('admin/', admin.site.urls),

    # Car includes -------------------------------
    path('car/', include ('car.urls')),

    # Users Includes ----------------------------
    path('users/', include('users.urls')),

    # Register/Sign Up Page -----------------------
    path('register/', userviews.register, name='register'),

    # Login Page ------------------------------------
    path('login/', userviews.login_view, name='login'),

    # Logout Page --------------------------------------
    path('logout/', userviews.logout_view, name='logout'),

    # Profile Page ------------------------------------
    path('profile/', userviews.ProfilePage, name='profile'),

    # Profile Form Page -----------------------------------------
    path('profform/<int:prof_id>/', userviews.ProfileForm, name='profform'),
]

urlpatterns += [] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)