from django.db import models
from django.contrib.auth.models import User
# Create your models here.


#  model post
    # title
    # image
    # shortdesc
    # desc
    # tag
    # like
    # comment
    # category
    # author
    # created_on
    # updated_on
    # location


class Post(models.Model):
    # id = ?
    PUB = 'pub'
    DRF = 'drf'
    DEL = 'del'
    NOT = 'not'
    
    STATUS_CHOICES = [
        (PUB,'publish'),
        (DRF,'draft'),
        (DEL,'delete'),
        (NOT,'notset'),
    ]
    title = models.CharField('title post' ,max_length=255)
    shortdesc = models.CharField( 'short description',max_length=255,null=True,blank=True)
    desc = models.TextField()
    location_lat = models.DecimalField(max_digits=5, decimal_places=2)
    location_lng =  models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='uploads')
    like = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    # status  4 publish , 3 draft , 2 delete , 1 notset
    # step1
    # status = models.CharField(max_length=7,default='noset')
    # step2
    # status = models.IntegerField(default=1)
    # step3.
    status = models.CharField(
        max_length=3,
        choices=STATUS_CHOICES,
        default=PUB,
    )
    # tag
    tag = models.ManyToManyField('Tag')
    # comment
    # comment = models.ForeignKey('comment',on_delete=models.CASCADE) 
    # category
    category = models.ManyToManyField('Category')
    # owner
    owner = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='post owner')


    def __str__(self):
        return self.title



class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    title = models.CharField('title post' ,max_length=255)
    desc = models.TextField()   
    like = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title

class Category(models.Model):
    
    parent = models.ForeignKey('self',on_delete=models.CASCADE,blank=True,null=True)
    title = models.CharField('title category' ,max_length=255)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



class Tag(models.Model):
    title = models.CharField('title' ,max_length=255)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    



