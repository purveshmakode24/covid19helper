# covid19helper Main URL Configuration

from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    path('auth/', views.obtain_auth_token)
]
