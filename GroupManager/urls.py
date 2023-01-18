from django.urls import path
from manager import views
from django.contrib import admin
from django.views.generic import TemplateView
from manager.views import*
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name='home'),
    path("main/", views.main, name='main'),
    path("login/", LoginUser.as_view(), name = "login"),
    path("create_group/", AddGroup.as_view(), name="create_group"),
    path("reg/", RegisterUser.as_view(), name="reg"),
    path("logout/", logout_user, name = "logout"),
    path('change/<int:pk>',ChangeGroup.as_view(), name = 'change')
]