from django.db import models
from django.contrib.auth.models import User


class profile(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(
        upload_to='pictures', blank=True)

    def __str__(self):
        return self.name
