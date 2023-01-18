from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.urls import reverse


class Group(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length = 20, verbose_name="Название")
    course = models.CharField(max_length = 20, verbose_name="Курс/Направление")
    minAge = models.PositiveIntegerField(verbose_name="Минимальный возраст")
    maxAge = models.PositiveIntegerField(verbose_name="Максимальный возраст")
    capacity = models.PositiveIntegerField(verbose_name="Количество мест")

    def __str__(self):
        return self.name

    #def get_absolute_url(self):
        #return reverse('change', kwargs={'pk': self.pk})



class GroupMember(models.Model):
    group = models.ForeignKey(Group, on_delete = models.CASCADE)
    name = models.CharField(max_length = 20)
    dateOfBirth = models.DateField()
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    phoneNumber = models.CharField(validators = [phoneNumberRegex], max_length = 16, unique = True)



