from rest_framework import serializers
from . import models

from django.db.models import Count, Avg, Sum, Max


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


class FeedMenueplanSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FeedMenueplan
        fields = ('transaction_id',
                    'id',
                    'user_profile',
                    'title',
                    'pub_date')
        extra_kwargs = {'user_profile':{'read_only': True}}


class RecommenderSerializer(serializers.ModelSerializer):
    #recommendations =  serializers.SerializerMethodField()
    #norm_founders =  serializers.SerializerMethodField()

    class Meta:
        model = models.FeedMenueplan
        fields = (
        'id',
        'title'
        )
    #def get_recommendations(self, obj):
    #    #recommendations = obj.title
    #    recommendations = len(obj.transaction_id)
    #    return str(recommendations)
#filter(status='survived#
