from django import forms
from .models import *
from django.core.exceptions import ValidationError

class AddgroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'course', 'minAge', 'maxAge', 'capacity']

    def clean_maxAge(self):
        minAge = self.cleaned_data['minAge']
        maxAge = self.cleaned_data['maxAge']
        if minAge > maxAge:
            raise ValidationError('Минимальный врзраст не может быть больше максимального')
        return maxAge



   # name = forms.CharField(max_length=20, label="Имя группы", widget=forms.TextInput(attrs={'class': 'form-input'}))
   # course = forms.CharField(max_length=20, label="Направление/Курс")
   # minAge = forms.IntegerField(label="Минимальный возраст")
   # maxAge = forms.IntegerField(label="Максимальный возраст")
   # capacity = forms.IntegerField(label="Максимальное количество человек")