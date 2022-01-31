from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/' , views.loginUser, name="loginUser"),
    path('accounts/signup/' , views.signupUser, name="signupUser"),
    path('accounts/logout/' , views.logoutUser, name="logoutUser"),
]
