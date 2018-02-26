from django.db import models

# Create your models here.
class Board(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=120)
    def __str__(self):
        return self.nombre
class Post(models.Model):
    board = models.ForeignKey('board.Board',on_delete=models.CASCADE, related_name='Board')
    autor = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    text = models.TextField()
    image = models.ImageField(upload_to='static')
    def __str__(self):
        return self.text
class Comment(models.Model):
    post = models.ForeignKey('board.Post',on_delete=models.CASCADE,related_name = 'Post')
    autor = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    text = models.TextField()
    image = models.ImageField(upload_to='static')
    def __str__(self):
        return self.text
