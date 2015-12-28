from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Server(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(User)
    path = models.CharField(max_length=200)
    type = models.CharField(max_length=100)
    params = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.name


class ServerInstance(models.Model):
    server = models.ForeignKey(Server)
    pid = models.IntegerField()
    start = models.DateTimeField()
