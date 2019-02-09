from rest_framework import serializers
from . import models

from django.db.models import Count, Avg, Sum, Max



class TeamComparerSerializer(serializers.ModelSerializer):
    norm_indavg_management_experience =  serializers.SerializerMethodField()
    norm_indavg_technical_experience =  serializers.SerializerMethodField()
    norm_indavg_startup_experience =  serializers.SerializerMethodField()

    norm_management_experience =  serializers.SerializerMethodField()
    norm_technical_experience =  serializers.SerializerMethodField()
    norm_startup_experience =  serializers.SerializerMethodField()
    #norm_founders =  serializers.SerializerMethodField()

    class Meta:
        model = models.ProfileFeedItem
        fields = (
        'norm_management_experience',
        'norm_technical_experience',
        'norm_startup_experience',
        #'norm_founders',
        'norm_indavg_management_experience',
        'norm_indavg_technical_experience',
        'norm_indavg_startup_experience',
        'industry'
        #'max_management_experience'
        )

    def get_norm_management_experience(self, obj):
        normmanagementexperience = obj.management_experience
        max = models.ProfileFeedItem.objects.filter(industry=obj.industry).aggregate(max_management_experience=Max('management_experience'))
        return normmanagementexperience/max['max_management_experience']
    def get_norm_technical_experience(self, obj):
        normtechnicalexperience = obj.technical_experience
        max = models.ProfileFeedItem.objects.filter(industry=obj.industry).aggregate(max_technical_experience=Max('technical_experience'))
        return normtechnicalexperience/max['max_technical_experience']
    def get_norm_startup_experience(self, obj):
        normstartupexperience = obj.startup_experience
        max = models.ProfileFeedItem.objects.filter(industry=obj.industry).aggregate(max_startup_experience=Max('startup_experience'))
        return normstartupexperience/max['max_startup_experience']
#    def get_norm_founders(self, obj):
#        normfounders = obj.founders
#        max = models.ProfileFeedItem.objects.filter(industry=obj.industry).aggregate(max_founders=Max('founders'))
#        return normfounders/max['max_founders']


    def get_norm_indavg_management_experience(self, obj):
        avgmanagementexperience = models.ProfileFeedItem.objects.filter(industry=obj.industry)
        avgmanagementexperience = avgmanagementexperience.filter(status='survived')
        avgmanagementexperience = avgmanagementexperience.aggregate(avg_management_experience=Avg('management_experience'))
        max = models.ProfileFeedItem.objects.filter(industry=obj.industry).aggregate(max_management_experience=Max('management_experience'))
        return avgmanagementexperience["avg_management_experience"]/max['max_management_experience']
    def get_norm_indavg_technical_experience(self, obj):
        avgtechnicalexperience = models.ProfileFeedItem.objects.filter(industry=obj.industry)
        avgtechnicalexperience = avgtechnicalexperience.filter(status='survived')
        avgtechnicalexperience = avgtechnicalexperience.aggregate(avg_technical_experience=Avg('technical_experience'))
        max = models.ProfileFeedItem.objects.filter(industry=obj.industry).aggregate(max_technical_experience=Max('technical_experience'))
        return avgtechnicalexperience["avg_technical_experience"]/max['max_technical_experience']
    def get_norm_indavg_startup_experience(self, obj):
        avgstartupexperience = models.ProfileFeedItem.objects.filter(industry=obj.industry)
        avgstartupexperience = avgstartupexperience.filter(status='survived')
        avgstartupexperience = avgstartupexperience.aggregate(avg_startup_experience=Avg('startup_experience'))
        max = models.ProfileFeedItem.objects.filter(industry=obj.industry).aggregate(max_startup_experience=Max('startup_experience'))
        return avgstartupexperience["avg_startup_experience"]/max['max_startup_experience']


class UserProfileSerializer(serializers.ModelSerializer):
    """ A serializer for user profile objects."""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password','created_on')
        extra_kwargs = {'password':{'write_only':True}}

    def create(self, validated_data):
        """create and return a new user"""

        user = models.UserProfile(
            email=validated_data['email'],
            name=validated_data['name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """A serializer for profile feed items."""

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id',
        'user_profile',
        'startup_name',
        'management_experience',
        'technical_experience',
        'startup_experience',
        'founders',
        'employees',
        'advisors',
        'budget',
        'funding_rounds',
        'focus',
        'founding_date',
        'revenue',
        'hightech',
        'industry',
        'hotspot',
        'status',
        'created_on')
        extra_kwargs = {'user_profile':{'read_only': True}}
