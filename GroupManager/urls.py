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

    path("groups/", Groups.as_view(), name='groups'),
    path("add_group/", AddGroup.as_view(), name="add_group"), 
    path('change_group/<int:pk>', ChangeGroup.as_view(), name = 'change'),

    path('group_members/<int:group_id>', GroupMembers.as_view(), name = 'group'),
    path("add_group_members/", AddGroupMember.as_view(), name="add_group_member"),
    path('change_group_members/<int:member_id>', ChangeGroupMemder.as_view(), name='change_member')
]