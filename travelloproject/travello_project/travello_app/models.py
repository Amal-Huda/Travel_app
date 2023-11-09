from django.db import models

# Create your models here.
class destinations(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='travello_pics')
    desc=models.TextField()
    def __str__(self):
        self.dname
class people(models.Model):
    name1=models.CharField(max_length=250)
    img1=models.ImageField(upload_to='travello_pics')
    desc1=models.TextField()
    def __str__(self):
        self.pname
class mydestination(models.Model):
    dname=models.CharField(max_length=250)
    dimg=models.ImageField(upload_to='travello_pics')
    ddesc=models.TextField()
class mypeople(models.Model):
    pname=models.CharField(max_length=250)
    pimg=models.ImageField(upload_to='travello_pics')
    pdesc=models.TextField()





