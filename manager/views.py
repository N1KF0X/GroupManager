from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from .models import*
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import*

def home(request):
    data = {'title':'Добро пожаловать'}
    return render(request, "home.html", context=data)

def logout_user(request):
    logout(request)
    return redirect('login')

class Groups(ListView):
    model = Group
    template_name = "main.html"
    context_object_name = "groups"

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Менеджер групп'
        return context
    
    def get_queryset(self):
        return Group.objects.filter(user_id = self.request.user.id )

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'reg.html'
    success_url = reverse_lazy('login')    

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        context['button_title'] = 'Создать аккаунт'
        return context

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    
    def get_success_url(self):
        return reverse_lazy('main')

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Вход'
        context['button_title'] = 'Войти'
        return context

class AddGroup(CreateView):
    form_class = AddgroupForm
    template_name = 'create.html'
    context_object_name = 'form'
    success_url = reverse_lazy('main') 

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создать группу'
        context['button_title'] = 'Создать группу'
        return context

    def form_valid(self, form):
        fields = form.save(commit=False)
        fields.user = self.request.user
        fields.save()
        return super().form_valid(form)
