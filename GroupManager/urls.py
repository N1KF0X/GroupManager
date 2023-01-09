from django.urls import path
from manager import views
from django.contrib import admin
from django.views.generic import TemplateView
 
urlpatterns = [
    path("", TemplateView.as_view(template_name="about.html")),
    path('admin/', admin.site.urls),
]