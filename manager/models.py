from django.db import models
from django.core.validators import RegexValidator

class User(models.Model):
    login = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)


class Group(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length = 20)
    course = models.CharField(max_length = 20)
    minAge = models.PositiveIntegerField()
    maxAge = models.PositiveIntegerField()
    capacity = models.PositiveIntegerField()

class GroupMember(models.Model):
    group = models.ForeignKey(Group, on_delete = models.CASCADE)
    name = models.CharField(max_length = 20)
    dateOfBirth = models.DateField()
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    phoneNumber = models.CharField(validators = [phoneNumberRegex], max_length = 16, unique = True)



