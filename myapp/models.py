from django.db import models

class User_Table(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    birthdate = models.DateField()

    class Meta:
        db_table='user_table'

class Main_Crawling(models.Model):
    category = models.TextField(blank=True, primary_key=True)
    title = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    author = models.TextField(blank=True, null=True)
    subtopic = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    
    class Meta:
        db_table = 'main_crawling'
