from django import forms 
from .models import *
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm

class AddgroupForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = ['name', 'course', 'minAge', 'maxAge', 'capacity']
        #widgets = {
        #    'name': forms.TextInput(attrs={'class': 'form-input'}),
        #    'course': forms.TextInput(attrs={'class': 'form-input'}),
        #    'course': forms.IntegerField(attrs={'class': 'form-input'}),
        #    'course': forms.IntegerField(attrs={'class': 'form-input'}),
        #    'course': forms.IntegerField(attrs={'class': 'form-input'}),
        #}

    def clean_maxAge(self):
        minAge = self.cleaned_data['minAge']
        maxAge = self.cleaned_data['maxAge']
        if minAge > maxAge:
            raise ValidationError('Минимальный врзраст не может быть больше максимального')
        return maxAge

#class ChangeGroupForm(forms.Form):


    
class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Имя пользователя", widget = forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label="Пароль", widget = forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label="Подтверждение пароля", widget = forms.PasswordInput(attrs={'class': 'form-input'}))
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class OrderingForm(forms.Form):
    ordering = forms.ChoiceField(label = "Сортировать по", required=False, choices=[
        ["name", "По название"],
        ["course", "По направлению/курсу"],
        ["age" , "По возрасту"],
    ])

class DeleteForm(forms.Form):
    deleteList = forms.ModelChoiceField(label= 'Название группы', queryset=Group.objects.all())

   # name = forms.CharField(max_length=20, label="Имя группы", widget=forms.TextInput(attrs={'class': 'form-input'}))
   # course = forms.CharField(max_length=20, label="Направление/Курс")
   # minAge = forms.IntegerField(label="Минимальный возраст")
   # maxAge = forms.IntegerField(label="Максимальный возраст")
   # capacity = forms.IntegerField(label="Максимальное количество человек")


