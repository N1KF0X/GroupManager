from django.urls import path, re_path
from manager import views
from django.contrib import admin
from django.views.generic import TemplateView
from manager.views import*
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", welcome, name='welcome'),
    path("logout/", logout_user, name = "logout"),
    path("login/", LoginUser.as_view(), name = "login"),
    path("reg/", RegisterUser.as_view(), name="reg"),

    path("groups/", groups, name='groups'),
    path("add_group/", AddGroup.as_view(), name="add_group"), 
    path('change_group/<int:pk>', ChangeGroup.as_view(), name = 'change'),

    path('group_members/<int:group_id>', group_members, name = 'group_members'),
    path("add_group_member/", add_group_member, name="add_group_member"),
    path('change_group_members/<int:member_id>', change_group_member, name='change_member'),
    path('not_your_group/', not_your_group, name='not_your_group'),
]