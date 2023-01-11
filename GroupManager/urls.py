from django.urls import path
from manager import views
from django.contrib import admin
from django.views.generic import TemplateView
from manager.views import *
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", RegisterUser.as_view(), name='home'),
    path("main/", Groups.as_view(), name='main'),
    path("login/", LoginUser.as_view(), name = "login")
]