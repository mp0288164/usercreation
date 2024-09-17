from django.db import models

# Create your models here.
class UserRegistration(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=10)
    confirm_password = models.CharField(max_length=10)
    
    def __str__(self):
        return self.username
