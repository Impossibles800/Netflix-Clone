import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

AGE_CHOICES = (
    ('All', 'All'),
    ('Kids', 'Kids')
)
MOVIE_CHOICES = (
    ('Seasonal', 'Seasonal'),
    ('Single', 'Single')
)


class CustomUser(AbstractUser):
    profiles = models.ManyToManyField('Profile',  blank=True)


class Profile(models.Model):
    name = models.CharField(max_length=250)
    age_limit = models.CharField(max_length=10, choices=AGE_CHOICES)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)


class Movie(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4)
    type = models.CharField(max_length=15, choices=MOVIE_CHOICES)
    video = models.ManyToManyField('Video')
    flyer = models.ImageField(upload_to='flyers')
    age_limit = models.CharField(max_length=10, choices=AGE_CHOICES)


class Video(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    file = models.FileField(upload_to='videos')


