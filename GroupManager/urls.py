from django.urls import path
from manager import views
from django.contrib import admin
from django.views.generic import TemplateView
from manager.views import *
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home),
    path("main/", Groups.as_view(), name='main'),
    path("about/", views.about),
    #path("register/", RegisterUser.as_view(), name = "register")
]