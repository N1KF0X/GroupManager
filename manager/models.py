from django.db import models

class User():
    login = models.CharFiels(max_length = 20)
    password = models.CharFiels(max_length = 20)


class Group():
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharFiels(max_length = 20)
    course = models.CharFiels(max_length = 20)
    minAge = models.PositiveIntegerField()
    maxAge = models.PositiveIntegerField()
    m


