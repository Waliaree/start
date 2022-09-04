from concurrent.futures.process import _python_exit
from email.headerregistry import Address
from statistics import mode
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class Employees(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    address = models.TextField()
    phone = models.IntegerField()

    def __str__(self):
        return self.name