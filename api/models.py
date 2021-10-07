from django.db import models
from django.utils import timezone

class InstaBlogger(models.Model):
    blogger_name = models.CharField(max_length=100)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.blogger_name

    class Meta:
        ordering = ['blogger_name']

class InstaUser(models.Model):
    user_follower =  models.ForeignKey(InstaBlogger, on_delete=models.CASCADE)
    user_id = models.CharField(max_length=100)
    user_login = models.CharField(max_length=100)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_id

    class Meta:
        ordering = ['user_follower']
