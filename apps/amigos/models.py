from django.db import models
from django.contrib.auth.models import User
class Amigo(models.Model):
	usuario = models.ForeignKey('auth.User',on_delete=models.CASCADE)
	friend = models.ForeignKey(User,on_delete=models.CASCADE,related_name = "friend_set")
	def __str__(self):
		return str(self.usuario)+" amigo de "+str(self.friend)

# Create your models here.
