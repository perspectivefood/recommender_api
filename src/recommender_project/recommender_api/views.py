from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count, Avg, Sum

from . import serializers
from . import models
from . import permissions

class TeamComparer(viewsets.ModelViewSet):
    http_method_names = ['get']
    queryset = models.ProfileFeedItem.objects.all()

    serializer_class = serializers.TeamComparerSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.PostOwnStatus, IsAuthenticated)

    def get_queryset(self):
        return self.queryset.filter(user_profile=self.request.user).order_by('-created_on')[:1]


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profiles."""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')

    def get_queryset(self):
        return self.queryset.filter(email=self.request.user)

class LoginViewSet(viewsets.ViewSet):
    """Checks email and password and returns an auth token."""

    serializer_class = AuthTokenSerializer

    def create(self,request):
        """Use the ObtainAuthToken to validate and create a token."""

        return ObtainAuthToken().post(request)

class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating feed items."""

    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (permissions.PostOwnStatus, IsAuthenticated)
    #http_method_names = ['post']

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user."""
        serializer.save(user_profile=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user_profile=self.request.user).order_by('-created_on')[:1]
