from django import forms 
from .models import *
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Имя пользователя", widget = forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label="Пароль", widget = forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label="Подтверждение пароля", widget = forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class AddGroupForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = ['name', 'course', 'minAge', 'maxAge', 'capacity']
        #widgets = {
        #    'name': forms.TextInput(attrs={'class': 'form-input'}),
        #    'course': forms.TextInput(attrs={'class': 'form-input'}),
        #    'course': forms.IntegerField(attrs={'class': 'form-input'}),
        #    'course': forms.IntegerField(attrs={'class': 'form-input'}),
        #    'course': forms.IntegerField(attrs={'class': 'form-input'}),
        #}DateField()

    def clean_maxAge(self):
        minAge = self.cleaned_data['minAge']
        maxAge = self.cleaned_data['maxAge']
        if minAge > maxAge:
            raise ValidationError('Минимальный врзраст не может быть больше максимального')
        return maxAge

class GroupsOrderingForm(forms.Form):
    
    ordering = forms.ChoiceField(label = "Сортировать по", required=False, choices=[
        ["name", "По название"],
        ["course", "По направлению/курсу"],
        ["age" , "По возрасту"]
    ])

class GroupDeletionForm(forms.Form):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['group_list'].queryset = Group.objects.filter(user_id = user.id).order_by('name')

    group_list = forms.ModelChoiceField(label= 'Удалить группу', queryset = None, empty_label='Выбрать')

class AddGroupMemberForm(forms.ModelForm):
    def __init__(self, user_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['group'].queryset = Group.objects.filter(user_id = user_id).order_by('name')
        self.fields['group'].empty_label=None

    class Meta:
        model = GroupMember
        fields = ['name', 'dateOfBirth', 'phoneNumber', 'group']
        widgets = {
            'dateOfBirth': forms.SelectDateWidget(),
        }

class MembersOrderingForm(forms.Form):
    ordering = forms.ChoiceField(label = "Сортировать по", required=False, choices=[
        ["name", "По Ф.И.О."],
        ["dateOfBirth", "По дате рождения"]
    ])

class MemberDeletionForm(forms.Form):
    def __init__(self, group_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['members_list'].queryset = GroupMember.objects.filter(group_id = group_id).order_by('name')

    members_list = forms.ModelChoiceField(label= 'Удалить из группы', queryset = None, empty_label='Выбрать')



