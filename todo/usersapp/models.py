from django.contrib.auth.models import AbstractUser
from django.db import models


class TodoUser(AbstractUser):
    email = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f'{self.email}'
