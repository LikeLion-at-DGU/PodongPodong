from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Board(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=2000)
    cafeteria = models.CharField(max_length=2000)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()
    body = models.TextField()
    
    def __str__(self):
        return self.title