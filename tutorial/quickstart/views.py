from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UsersSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UsersSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
        somewhere over the rainbow
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
