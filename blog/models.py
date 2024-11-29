from django.db import models

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=10,blank=True,null=True)
    age=models.SmallIntegerField(max_length=2,blank=False,null=False)

