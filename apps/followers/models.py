from django.db import models
from django.contrib.auth.models import User
class Follower(models.Model):
    user = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    followed = models.ForeignKey(User,on_delete=models.CASCADE,related_name = "followed_set")
    def __str__(self):
        return str(self.user)+" seguidor de "+str(self.followed)
# Create your models here.
