from django.db import models

class User:
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30, unique=True)
    access_token = models.CharField(max_length=200)