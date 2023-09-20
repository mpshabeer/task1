from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='pics')
    desc=models.CharField(max_length=100)


class Team(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='pics')
    desc=models.CharField(max_length=100)