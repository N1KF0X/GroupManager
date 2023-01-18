from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from .models import*
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import*
from django.http.response import HttpResponse

def home(request):
    data = {'title':'Добро пожаловать'}
    return render(request, "home.html", context=data)

def logout_user(request):
    logout(request)
    return redirect('login')

def main(request):
    groups = Group.objects.filter(user_id = request.user.id )
    form1 = OrderingForm(request.GET)
    form2 = DeleteForm(request.POST)

    if 'delete' in request.POST:
        if form2.is_valid():
            Group.objects.filter(name = form2.cleaned_data['deleteList'].name).delete()

    if 'sort' in request.GET:
        if form1.is_valid():
            if form1.cleaned_data['ordering'] == "age":
                groups = groups.order_by("minAge", "maxAge")
            else:
                groups = groups.order_by(form1.cleaned_data['ordering'])

    form2.queryset = groups

    data = {
        'groups': groups, 
        "form1": form1,
        "form2": form2,
        "title": "Группы"
    }

    return render(request, 'main.html', data)


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

class ChangeGroup(UpdateView):
    model = Group
    form_class = AddgroupForm
    template_name = 'create.html'
    success_url = reverse_lazy('main')

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Изменить группу'
        context['button_title'] = 'Изменить группу'
        return context

    def form_valid(self, form):
        return super().form_valid(form)

def pupa(request, pk):
    data = {'title':'Добро пожаловать'}
    return render(request, "create.html", context=data)

