from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView
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

def about(request):
    return render(request, "about.html")

class Groups(ListView):
    model = Group
    template_name = "main.html"
    context_object_name = "groups"

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Менеджер групп'
        context['form'] = AddgroupForm()
        return context


