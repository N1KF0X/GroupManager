from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from .models import*
from django.contrib.auth import logout
from .forms import*
from django.shortcuts import get_object_or_404


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
class Groups(ListView):
    model = Group
    template_name = "groups.html"
    context_object_name = "groups"

    def get_context_data(self, *, object_list = None, **kwargs):
        #sort_form = GroupsOrderingForm(self.request.user, self.request.GET)
        #delete_form = GroupDelitionForm(self.request.user, self.request.POST)
        context = super().get_context_data(**kwargs)
        context['title'] = 'Группы'
        #context['sort_form'] = sort_form 
        #context['delete_form'] = delete_form 
        return context
    
    def get_queryset(self):
        return Group.objects.filter(user_id = self.request.user.id)


# Страницца для создания группы
class AddGroup(CreateView):
    form_class = AddgroupForm
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
        fields.save()
        return super().form_valid(form)

# Страница для изменения группы
class ChangeGroup(UpdateView):
    model = Group
    form_class = AddgroupForm
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
class GroupMembers(ListView):
    model = GroupMember
    template_name = "group_members.html"
    context_object_name = "group_members"

    def get_context_data(self, *, object_list = None, **kwargs):
        #group_id = "id группы" # здесь id должен быть получен из строки запроса
        context = super().get_context_data(**kwargs)
        #context['title'] = Group.objects.get(id = group_id).name
        #context['sort_form'] = GroupsOrderingForm()
        #context['delete_form'] = GroupDelitionForm()
        return context

        
    def get_queryset(self):
        return Group.objects.filter(user_id = self.request.user.id)


# Страницца для создания члена группы 
class AddGroupMember(CreateView):
    form_class = AddGroupMemberForm
    template_name = 'add.html'
    success_url = reverse_lazy('groups') 

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить члена группы'
        context['button_title'] = 'Подтвердить'
        return context

    def form_valid(self, form):
        fields = form.save(commit=False)
        fields.save()
        return super().form_valid(form)

# Страница для изменения члена группы
class ChangeGroupMemder(UpdateView):
    model = GroupMember
    form_class = AddGroupMemberForm
    template_name = 'change.html'
    success_url = reverse_lazy('groups')
    context_object_name = 'group_member'

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['group'] = self.object.group
        context['title'] = 'Изменить группу'
        context['button_title'] = 'Подтвердить'
        return context


