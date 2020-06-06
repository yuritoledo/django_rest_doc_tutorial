from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UsersSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
