from django.urls import path, re_path
from manager import views
from django.contrib import admin
from django.views.generic import TemplateView
from manager.views import*
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name='home'),
    path("main/", main, name='main'),
    path("login/", LoginUser.as_view(), name = "login"),
    path("create_group/", AddGroup.as_view(), name="create_group"),
    path("reg/", RegisterUser.as_view(), name="reg"),
    path("logout/", logout_user, name = "logout"),
    path('change/<int:pk>', ChangeGroup.as_view(), name = 'change'),
    path('group/<int:group_id>', group, name = 'group'),
    path("add_group/", add_member, name="add_member"),
    path('change_member/<int:member_id>', change_member, name='change_member')
]