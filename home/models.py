from django.db import models

# Create your models here.
class Contact(models.Model):
    email = models.CharField(max_length=122)
    password =models.CharField(max_length=122)
    address =models.CharField(max_length=122)
    city =models.CharField(max_length=122)
    state =models.CharField(max_length=122)
    zip =models.IntegerField()
    date=models.DateField()

    def __str__(self):
        return self.email
    