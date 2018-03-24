from django.db import models
from django.utils import timezone
from storages.backends.ftp import FTPStorage
import hashlib
import os
fs = FTPStorage()
def update_filename(instance, filename):
    path = "img"
    fileName, fileExtension = os.path.splitext(filename)
    filename = filename+str(timezone.now())
    name = hashlib.sha256((filename).encode()).hexdigest()+fileExtension
    path  = os.path.join(path, name)
    return path
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
    image = models.ImageField(upload_to=update_filename,storage=fs)
    def __str__(self):
        return self.title
class Comment(models.Model):
    post = models.ForeignKey('board.Post',on_delete=models.CASCADE,related_name = 'Post')
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    text = models.TextField()
    image = models.ImageField(upload_to='static')
    def __str__(self):
        return self.text
