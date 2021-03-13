from django.contrib.auth.models import AbstractUser
from django.db import models

ADMIN = 1
CLIENT = 2

user_types = (
    (ADMIN, 'ADMIN'),
    (CLIENT, 'CLIENT'),
)

class User(AbstractUser):
    phone = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)
    role = models.IntegerField(choices=user_types, default=ADMIN)