# api/models.py
from django.db import models

class Admin(models.Model):
    account = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    sex = models.CharField(max_length=10)
    birthday = models.DateField()
    desc = models.TextField()

class Buyer(models.Model):
    account = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    sex = models.CharField(max_length=10)
    birthday = models.DateField()
    desc = models.TextField()

class Seller(models.Model):
    account = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    sex = models.CharField(max_length=10)
    birthday = models.DateField()
    desc = models.TextField()

class Good(models.Model):
    goodName = models.CharField(max_length=100)
    goodId = models.CharField(max_length=100, unique=True)
    goodPic = models.ImageField(upload_to='goods/')
    goodPrice = models.DecimalField(max_digits=10, decimal_places=2)
    goodPromotion = models.CharField(max_length=100)
    goodServe = models.CharField(max_length=100)
    goodBySellerId = models.CharField(max_length=100)

class Discuss(models.Model):
    discussId = models.CharField(max_length=100, unique=True)
    discussTitle = models.CharField(max_length=200)
    discussTime = models.DateField()
    discussBy = models.CharField(max_length=100)
    discussByType = models.CharField(max_length=50)
    discussContent = models.TextField()

class Post(models.Model):
    postId = models.CharField(max_length=100, unique=True)
    postTime = models.DateField()
    postBy = models.CharField(max_length=100)
    postByType = models.CharField(max_length=50)
    postContent = models.TextField()
    postByDiscussId = models.CharField(max_length=100)

class Comment(models.Model):
    commentId = models.CharField(max_length=100, unique=True)
    commentById = models.CharField(max_length=100)
    commentTime = models.DateField()
    commentContent = models.TextField()
    commentScore = models.IntegerField()
    goodId = models.CharField(max_length=100)
    
class Order(models.Model):
    orderId = models.CharField(max_length=100, unique=True)
    orderBy = models.CharField(max_length=100)
    orderGoodId = models.CharField(max_length=100)
    orderDate = models.DateField()
    orderNum = models.IntegerField()
    orderPrice = models.FloatField()
    orderPos = models.CharField(max_length=100)
    orderName = models.CharField(max_length=100)
    
