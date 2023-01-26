from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from .models import*
from django.contrib.auth import logout
from .forms import*
from django.shortcuts import get_object_or_404
from django.db.models import F

# Страница на которой происходит вход/авторизация
def welcome(request):
    data = {'title':'Добро пожаловать'}
    return render(request, "welcome.html", context=data)

# Функция для выхода из аккаунта 
def logout_user(request):
    logout(request)
    return redirect('login')

# Страница для регистрации
class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'reg.html'
    success_url = reverse_lazy('login')    

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        context['button_title'] = 'Создать аккаунт'
        return context

# Страница для авторизации
class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    
    def get_success_url(self):
        return reverse_lazy('groups')

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Вход'
        context['button_title'] = 'Войти'
        return context

# Страница на которой отобращаются все группы,
# на ней можно так же отсортировать список 
# или удалить выбранную группу
def groups(request):
    user_id = request.user.id
    ordering_form = GroupsOrderingForm(request.GET)
    deletion_form = GroupDeletionForm(request.user, request.POST) 

    groups = Group.objects.filter(user_id = user_id)

    data = {
        'groups': groups, 
        "ordering_form": ordering_form,
        "deletion_form": deletion_form,
        "title": "Группы",
        "sort_button_title": "Сортировать",
        "deletion_button_title": "Удалить",
    }
    
    if 'delete' in request.POST:
        if deletion_form.is_valid():
            Group.objects.filter(id = deletion_form.cleaned_data['group_list'].id).delete()
            Group.objects.filter(id = deletion_form.cleaned_data['group_list'].id).update(members_amount = F("members_amount") - 1)
            return render(request, 'groups.html', data)
   
    if 'sort' in request.GET:
        if ordering_form.is_valid():
            if ordering_form.cleaned_data['ordering'] == "age":
                groups = groups.order_by("minAge", "maxAge")
            else:
                groups = groups.order_by(ordering_form.cleaned_data['ordering'])      

    return render(request, 'groups.html', data)

# Страницца для создания группы
class AddGroup(CreateView):
    form_class = AddGroupForm
    template_name = 'add.html'
    success_url = reverse_lazy('groups') 

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создать группу'
        context['button_title'] = 'Подтвердить'
        return context

    def form_valid(self, form):
        fields = form.save(commit=False)
        fields.user = self.request.user
        fields.members_amount = 0
        fields.save()
        return super().form_valid(form)

# Страница для изменения группы
class ChangeGroup(UpdateView):
    model = Group
    form_class = AddGroupForm
    template_name = 'change.html'
    success_url = reverse_lazy('groups')
    context_object_name = 'group'

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Изменить группу'
        context['button_title'] = 'Подтвердить'
        return context

# Страница на которой отобращаются все члены группы,
# на ней можно так же отсортировать список 
# или удалить выбранного члена группы
def group_members(request, group_id):
    # user_id = request.user.id
    ordering_form = MembersOrderingForm(request.GET)
    deletion_form = MemberDeletionForm(group_id, request.POST) 
    group = Group.objects.get(id = group_id)
    group_members = GroupMember.objects.filter(group_id=group_id)

    data = {
        'group': group,
        'group_members': group_members, 
        "ordering_form": ordering_form,
        "deletion_form": deletion_form,
        "title": group.name,
        "sort_button_title": "Сортировать",
        "deletion_button_title": "Удалить",
    }
    
    if 'delete' in request.POST:
        if deletion_form.is_valid():
            GroupMember.objects.filter(id = deletion_form.cleaned_data['members_list'].id).delete()
            return render(request, 'group_members.html', data)
   
    if 'sort' in request.GET:
        if ordering_form.is_valid():            
            group_members = group_members.order_by(ordering_form.cleaned_data['ordering'])         

    return render(request, 'group_members.html', data)

# Страницца для создания члена группы 
def add_group_member(request):
    form = AddGroupMemberForm(request.user.id, request.POST)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            Group.objects.filter(id = form.cleaned_data['group'].id).update(members_amount = F("members_amount") + 1)

            return redirect ('groups')

    data = {
        "form":form,
        "button_title":"Подтвердить"
    }
    return render(request, 'add.html', data)

# Страница для изменения члена группы
def change_group_member(request, member_id):
    instance = get_object_or_404(GroupMember, id=member_id)
    form = AddGroupMemberForm(user_id=request.user.id, instance=instance)                                                               

    if request.method == "POST":
        form = AddGroupMemberForm(request.user.id, request.POST, instance=instance)
        if form.is_valid():
            form.save()        
            return redirect ('groups') 

    data = {
        "title":"Изменить члена группы",
        "form":form,
        "button_title":"Подтвердить"
    }
    return render(request, 'add.html', data)

# Страница, на которую попадёт пользователь,
# если попытаеся посмотреть группу, 
# которая ему не принадлежит
def not_your_group(request):
    data = {
        "title":"Ошибка",
    }
    return render(request, 'not_your_group.html', data)
