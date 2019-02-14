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

class Recommender(viewsets.ModelViewSet):
    http_method_names = ['get']
    queryset = models.FeedMenueplan.objects.all()

    serializer_class = serializers.RecommenderSerializer
    permission_classes = (permissions.PostOwnStatus, IsAuthenticated)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        data = self.queryset.filter(user_profile=self.request.user)
        last_transaction_id = data.order_by("-pub_date").values('transaction_id')[:1]
        data = data.filter(transaction_id=last_transaction_id[0].get("transaction_id"))
        return data


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

class FeedMenueplanViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = models.FeedMenueplan.objects.all()
    serializer_class = serializers.FeedMenueplanSerializer
    permission_classes = (permissions.PostOwnStatus, IsAuthenticated)

    #def get_serializer(self, *args, **kwargs):
    #    if "data" in kwargs:
    #        data = kwargs["data"]
    #
    #    # check if many is required
    #        if isinstance(data, list):
    #            kwargs["many"] = True
    #        return super(FeedMenueplanViewSet, self).get_serializer(*args, **kwargs)

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user."""
        serializer.save(user_profile=self.request.user)

    def get_queryset(self):

        return self.queryset.filter(user_profile=self.request.user).order_by('-pub_date')[:1]
        #return self.queryset.all(many=True)


class UploadSubstitutesViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = models.UploadSubstitutes.objects.all()
    serializer_class = serializers.UploadSubstitutesSerializer
    permission_classes = (permissions.PostOwnStatus, IsAuthenticated)

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user."""
        serializer.save(user_profile=self.request.user)
