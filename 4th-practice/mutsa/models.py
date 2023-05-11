from django.db import models

# Create your models here.
class User(models.Model):
    userid = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField()
    username = models.CharField(max_length=20)

class Post(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField()
    liked = models.IntegerField()
    image = models.ImageField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    comment_content = models.TextField()
    created_at = models.IntegerField()
    liked = models.IntegerField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)

