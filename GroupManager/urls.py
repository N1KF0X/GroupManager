from django.urls import path
from manager import views
from django.views.generic import TemplateView
 
urlpatterns = [
    path("", TemplateView.as_view(template_name="about.html")),
]