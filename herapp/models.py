from django.db import models

# Create your models here.
class People(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=20)
    profileImg= models.ImageField(upload_to='images',blank=True, null=True)