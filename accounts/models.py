from django.db import models

# Create your models here.
class Registration(models.Model):
    first_name=models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    cpassword = models.CharField(max_length=10)

    def __str__(self):
        return '{}'.format(self.first_name)
