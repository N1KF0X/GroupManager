from django.shortcuts import render
from .models import*

def main(request):
    group = Group.objects.get(id = 1)
    groupData = []   
    groupData += [group.name, group.course, f"{group.minAge} - {group.maxAge}", f"0/{group.capacity}"]
    data = {"title": "Менеджер групп", "groupData": groupData}
    return render(request, "main.html", data)

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")