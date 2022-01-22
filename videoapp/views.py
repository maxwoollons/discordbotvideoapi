from django.shortcuts import render
from django.contrib.auth.models import User, Group
from videoapp.models import videos
from rest_framework import viewsets
from rest_framework import permissions
from videoapp.serializers import UserSerializer, GroupSerializer, VideoSerializer
import random
from rest_framework.views import APIView


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class VideosViewSet(viewsets.ModelViewSet):
 
    
    queryset = videos.objects.all().order_by("?")[:1]
    serializer_class = VideoSerializer
    
