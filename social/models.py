from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.
from django.db.models import CASCADE


class Profile(models.Model):
    name=models.CharField(max_length=50)
    user=models.OneToOneField(to=User,on_delete=CASCADE)
    age=models.IntegerField(default=16,validators=[MaxValueValidator(100),MinValueValidator(0)])
    ProfilePic=models.ImageField(upload_to='images//',null=True)
    CoverPics=models.ImageField(upload_to='images//',null=True)
    desc=models.TextField(null=True,blank=True)
    status=models.CharField(max_length=30,choices=(("married","married"),("single","single")),default="single")



class MyPost(models.Model):
    pic=models.ImageField(upload_to="images//")
    cr_date=models.DateTimeField(auto_now_add=True)
    uploaded_by=models.ForeignKey(to=Profile,on_delete=CASCADE,null=True,blank=True)
    subject=models.CharField(max_length=200,null=True)
