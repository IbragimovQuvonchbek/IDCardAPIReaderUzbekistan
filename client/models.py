from django.db import models


# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    date_of_birth = models.CharField(max_length=8)
    expiration_date = models.CharField(max_length=8)
    gender = models.CharField(max_length=1)
    personal_number = models.CharField(max_length=14, unique=True)
    card_number = models.CharField(max_length=9, unique=True)
    nationality = models.CharField(max_length=8)

    def __str__(self):
        return self.personal_number
