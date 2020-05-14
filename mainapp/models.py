from django.db import models
from django.contrib.auth.models import User

#We can make abstract user model
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(default='example@gmail.com')
    phone = models.CharField(max_length=10)
    name = models.CharField(max_length=100)             # Fullname
    que = models.IntegerField(default=0)        # no of questions asked
    ans = models.IntegerField(default=0)        # no of replies/answers given


class Post(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    statement = models.CharField(max_length=5000)
    category = models.IntegerField(default=0)         # which category web/AI
    upvotes = models.IntegerField(default=0)          # if voting system
    downvotes = models.IntegerField(default=0)
    #views = models.IntegerField(default=0)          # if total no of views wanna show
    time = models.TimeField(default='00:00')        # at what time it is asked


class Comment(models.Model):
    que = models.ForeignKey(Post, on_delete=models.CASCADE)
    usr = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    statement = models.CharField(max_length=5000)
    check = models.BooleanField(default=False)          # verified by seniors correct or not
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    replies = models.IntegerField(default=0)
    time = models.TimeField(default='00:00')            # at what time it is replied, so that we can sort


class Reply(models.Model):
    ans = models.ForeignKey(Comment, on_delete=models.CASCADE)
    usr = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    statement = models.CharField(max_length=5000)
    upvotes = models.IntegerField(default=0)
    check = models.BooleanField(default=False)  # verified by seniors correct or not
    time = models.TimeField(default='00:00')
