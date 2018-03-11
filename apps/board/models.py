from django.db import models
from django.utils import timezone
# Create your models here.
class Board(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=120)
    def __str__(self):
        return self.name
class Post(models.Model):
    board = models.ForeignKey('board.Board',on_delete=models.CASCADE, related_name='Board')
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=50)
    text = models.TextField()
    image = models.ImageField(upload_to='static')
    def __str__(self):
        return self.title
class Comment(models.Model):
    post = models.ForeignKey('board.Post',on_delete=models.CASCADE,related_name = 'Post')
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    text = models.TextField()
    image = models.ImageField(upload_to='static')
    def __str__(self):
        return self.text
