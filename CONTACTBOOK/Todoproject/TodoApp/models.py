from django.db import models


# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=30)
    phone=models.IntegerField()
    email=models.CharField(max_length=25)
    address=models.CharField(max_length=50)
    image=models.ImageField(upload_to='todoimage')

    
    def __str__(self):
        return self.name