from django.conf import settings
from django.db import models
from django.utils import timezone
import pytz
from django.contrib.auth import get_user_model  # model of current user
import uuid
from datetime import datetime
from django import template

register = template.Library()


@register.filter
def uuid_to_str(value):
    return str(value)

# Create your models here.


User = get_user_model()  # currently logged


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(
        upload_to='profile_images', default='blankbro.jpg')
    location = models.CharField(max_length=200, blank=True)

    def __str__(self):
        # it is so the at the admin we see username and not object1 2 ...
        return self.user.username


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images', default='white.jpg')
    caption = models.TextField(blank=True)
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user


class commentpost(models.Model):
    auther = models.CharField(max_length=50)
    post_id = models.CharField(max_length=50)
    com = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.auther


class Postcaption(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user


class LikePost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class joingroup(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class Likecap(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class CustomGroup(models.Model):
    name = models.CharField(max_length=50, unique=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    activity = models.CharField(max_length=300, blank=True)
    location = models.CharField(max_length=300, blank=True)
    caption = models.TextField()
    image = models.ImageField(upload_to='group_image', default="white.jpg")
    user = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=datetime.now)
    starts_at = models.DateTimeField(blank=True)
    finish_at = models.DateTimeField(blank=True)
    teammates = models.IntegerField(default=0)

    no_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class FollowersCount(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user


class form_request(models.Model):
    CHOICES1 = (
        ('Football', 'Football'),
        ('Volleyball', 'Volleyball'),
        ('Beach Tennis', 'Beach Tennis'),
        ('Diving', 'Diving'),
        ('Fishing', 'Fishing'),
        ('Camping', 'Camping'),
        ('Beach Yoga', 'Beach Yoga'),
        ('Beach clean up', 'Beach clean up'),
    )
    CHOICES2 = (
        ('Hassen beach', 'Hassen beach'),
        ('chatmemi beach', 'chatmemi beach'),
        ('Swisri beach', 'Swisri beach'),
        ('kef lasfer beach', 'kef lasfer beach'),
        ('Ain Mestir beach', 'Ain Mestir beach'),
        ('Rafraf beach', 'Rafraf beach'),
    )
    CHOICES3 = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    User = models.CharField(max_length=100)
    Email = models.EmailField(max_length=254, default='@gmail.com')
    Gender = models.CharField(default='Male', max_length=6, choices=CHOICES3)
    Age = models.IntegerField(default=18)
    Games = models.CharField(max_length=300, choices=CHOICES1)
    location = models.CharField(max_length=300, choices=CHOICES2)
    Disponibilité_date = models.DateField(default=timezone.now)
    requist_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.User
