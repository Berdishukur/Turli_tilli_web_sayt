from django.db import models
from django.utils import timezone
# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=100,blank=True,null=True)
    age=models.SmallIntegerField()
    def __str__(self):
        return self.name
class Genre(models.Model):
    name =models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Post(models.Model):
    title=models.CharField(max_length=255)
    content=models.TextField()
    author=models.ForeignKey(Author,null=True,on_delete=models.CASCADE)
    publish=models.DateTimeField(timezone.now)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
# class Book(models.Model):
#     name=models.CharField(max_length=100)
#     author=models.ForeignKey(Author,null=True,on_delete=models.CASCADE)
#     genre=models.ForeignKey(Genre,null=True,on_delete=models.SET_NULL)
#     # SET_NULL kitobni Authori bazadan o'chib ketsa kitob o'chmaydi va authorni o'rniga null qo'yib qo'yadi
#     # CACECADE da kitobni authori bazadan o'chib ketsa kitoblari ham o'chib ketadi
#     def __str__(self):
#         return self.name




