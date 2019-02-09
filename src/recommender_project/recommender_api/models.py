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



class ProfileFeedItem(models.Model):
    """Feed for startup data."""

    BUDGET_CHOICES = (
        ('verysmall', "<10k"),
        ('small', "10k-50k"),
        ('medium', "50k-100k"),
        ('big', "100k-500k"),
        ('verybig', ">500k"),
    )

    BUSINESS_FOCUS_CHOICES = (
            ('B2B', "B2B"),
            ('B2C', "B2C"),
        )

    YESNO_CHOICES= (
            (1, "YES"),
            (0, "NO"),
        )

    STATUS_CHOICES= (
            ("living", "living"),
            ("survived", "survived"),
            ("dead", "dead"),
        )

    INDUSTRY_CHOICES= (
            ("MedHealthTech", "MedHealthTech"),
            ('ICT App', 'ICT App'),
            ('AgriFoodTech', 'AgriFoodTech'),
            ('FinInsureTech', 'FinInsureTech'),
            ('HighTech', 'HighTech'),
            ('AdRetailTech', 'AdRetailTech'),
            ('CleanGreenTech', 'CleanGreenTech'),
            ('Consumer Goods', 'Consumer Goods'),
            ('PropTech', 'PropTech'),
            ('Consumer Goods', 'Consumer Goods'),
            ('RegLegalTech', 'RegLegalTech'),
            ('BioTech', 'BioTech'),
            ('MobilityTravelTech', 'MobilityTravelTech'),
            ('Other', 'Other'),
    )

    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    startup_name = models.CharField(max_length=255,null=True, blank=True,)
    management_experience = models.PositiveIntegerField(null=True, blank=True,validators=[MaxValueValidator(500), MinValueValidator(0)])
    technical_experience = models.PositiveIntegerField(null=True, blank=True,validators=[MaxValueValidator(500), MinValueValidator(0)])
    startup_experience = models.PositiveIntegerField(null=True, blank=True,validators=[MaxValueValidator(500), MinValueValidator(0)])
    founders = models.PositiveIntegerField(null=True, blank=True,validators=[MaxValueValidator(10), MinValueValidator(0)])
    advisors = models.PositiveIntegerField(null=True, blank=True,validators=[MaxValueValidator(100), MinValueValidator(0)])
    employees = models.PositiveIntegerField(null=True, blank=True, validators=[MaxValueValidator(500), MinValueValidator(0)])
    budget = models.CharField(null=True, blank=True, max_length=10,choices=BUDGET_CHOICES,default='verysmall')
    funding_rounds = models.PositiveIntegerField(null=True, blank=True,validators=[MaxValueValidator(100), MinValueValidator(0)])
    focus = models.CharField(max_length=10,choices=BUSINESS_FOCUS_CHOICES,default='B2C', null=True, blank=True)
    founding_date = models.DateField(default="1900-01-01", null=True, blank=True)
    revenue = models.IntegerField(null=True, blank=True)
    hightech = models.CharField(max_length=255,choices=YESNO_CHOICES,null=True, blank=True)
    industry = models.CharField(max_length=255,choices=INDUSTRY_CHOICES,null=True, blank=True)
    hotspot = models.CharField(max_length=255,choices=YESNO_CHOICES,null=True, blank=True)
    status = models.CharField(max_length=255,choices=STATUS_CHOICES,null=True, blank=True, default='living')
    created_on = models.DateTimeField(auto_now_add=True)

#    def get_count_founders(self):
#        return self.founders.count()


    def __str__(self):
        """return the model as a string. """

        return self.startup_name
        #return "success"
