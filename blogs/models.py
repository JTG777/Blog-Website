from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=60)
    slug=models.SlugField(unique=True,) 

    class Meta:
        verbose_name_plural='Categories' 

    def __str__(self):
        return self.name





class Tag(models.Model):
    name=models.CharField(max_length=30)    
    slug=models.SlugField(unique=True,)

    def __str__(self):
        return self.name.title()
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.name)
        super().save(*args,**kwargs)


class Post(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField(unique=True,max_length=100)
    content=models.TextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,related_name='posts')
    tag=models.ManyToManyField(Tag,blank=True)
    image=models.ImageField(upload_to='images/',default="No_Image_Available.jpg")

    def __str__(self):
        return self.title
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        super().save(*args,**kwargs)




class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comments")
    text=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
        return f"Comment by {self.author} on post {self.post}"
    
class Like(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name="likes")
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} likes {self.post}"

