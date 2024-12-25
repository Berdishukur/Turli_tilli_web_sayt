from django.db import models

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=10,blank=True,null=True)
    age=models.SmallIntegerField(max_length=2,blank=True,null=True)
    def __init__(self):
        return self.name

