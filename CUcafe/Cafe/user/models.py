from django.db import models




class User(models.Model):
    username = models.CharField(max_length=10, blank=False)
    password = models.CharField(max_length=10, blank=False)
    grade = 0

class Master(User):
    def __init__(self):
        super().__init__(self)

class Manager(User):
    def __init__(self):
        super().__init__(self)

