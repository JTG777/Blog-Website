from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    date_of_birth=models.DateField(null=True,blank=True)
    bio=models.TextField(blank=True)
    profile_picture=models.ImageField(upload_to='profile_pic/',default="No_Image_Available.jpg",blank=True,null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"