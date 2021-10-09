from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, default='')
    email = models.EmailField(max_length=20,default='')
    phone = models.IntegerField(default='')


    class Meta:
        ordering = ['id']
        db_table = 'user_profile'

        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profile'

    def __str__(self):
        return self.name