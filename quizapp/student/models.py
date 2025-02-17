from django.db import models

# Create your models here.
class student(models.Model):
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20, blank=True,null=True)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50,unique=True)
    password = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    pincode = models.IntegerField(max_length=20)
    
    
    def __str__(self):
        return f"{self.first_name}{self.last_name}"
    