from unicodedata import name
from django.db import models

# Create your models here.


class PhoneBookModel(models.Model):
    name = models.CharField(max_length=225)
    mobile = models.CharField(max_length=225)
    image = models.ImageField(upload_to='image/pro', null=True, blank=True)

    def __str__(self):
        return self.name
