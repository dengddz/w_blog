from django.db import models


class MyUser(models.Model):
    username = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'myuser'


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    icon = models.ImageField(upload_to='article', null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'article'
    
    
