from django.urls import path
from manager import views
from django.contrib import admin
from django.views.generic import TemplateView
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home),
    path("main", views.main),
    path("about", views.about),
]