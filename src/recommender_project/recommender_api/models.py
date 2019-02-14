from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class UserProfileManager(BaseUserManager):
    """Helps Django work with our custom user model."""

    def create_user(self, email, name, password=None):
        """Creates a new user profile object."""

        if not email:
            raise ValueError('User must have an email address.')

        email = self.normalize_email(email)
        user = self.model(email=email, name = name,)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Creates and saves a new superuser with given details."""

        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Respents a "user profile" inside our system."""

    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Used to get a users full name."""

        return self.name

    def get_short_name(self):
        """Used to get a users short name."""

        return self.name

    def __str__(self):
        """Django uses this when it need to convernt an object to a string."""

        return self.email


class FeedMenueplan(models.Model):
    transaction_id = models.CharField(max_length=255,default="none")
    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    date = models.DateField(default="1900-01-01", null=True, blank=True)
    menueline = models.CharField(max_length=255,default="none",null=True, blank=True)
    component = models.CharField(max_length=255,default="none",null=True, blank=True)
    PLU = models.IntegerField(default=0,null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)


class UploadSubstitutes(models.Model):
    user_profile = models.ForeignKey('UserProfile', default=None,on_delete=models.CASCADE)
    PLU = models.CharField(max_length=255,default=None,null=True, blank=True)
    top1 = models.CharField(max_length=255,default=None,null=True, blank=True)
    top2 = models.CharField(max_length=255,default=None,null=True, blank=True)
    top3 = models.CharField(max_length=255,default=None,null=True, blank=True)
    top4 = models.CharField(max_length=255,default=None,null=True, blank=True)
    top5 = models.CharField(max_length=255,default=None,null=True, blank=True)
    top6 = models.CharField(max_length=255,default=None,null=True, blank=True)
    top7 = models.CharField(max_length=255,default=None,null=True, blank=True)
    top8 = models.CharField(max_length=255,default=None,null=True, blank=True)
    top9 = models.CharField(max_length=255,default=None,null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
