from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from .models import*
from .forms import*

#def main(request):
    #if request.method == 'POST':
    #    form = AddgroupForm(request.POST)
    #    if form.is_valid():
    #        form.save()    
    #        return redirect("main")           
    #else:
    #    form = AddgroupForm()
    #r = request.user.id
    #groups = Group.objects.filter(user_id = 1)
    #data = {"title": "Менеджер групп", "groups": groups, "form": form}

    #return render(request, "main.html", data)

def home(request):
    return render(request, "home.html")

class Groups(ListView):
    model = Group
    template_name = "main.html"
    context_object_name = "groups"

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Менеджер групп'
        context['form'] = AddgroupForm()
        return context
    
    def get_queryset(self):
        return Group.objects.filter(user_id = self.request.user.id )

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'home.html'
    success_url = reverse_lazy('login')    

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Менеджер групп: Регистрация'
        return context

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    
    def get_success_url(self):
        return reverse_lazy('main')

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Менеджер групп: Вход'
        return context


