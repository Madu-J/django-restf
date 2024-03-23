from rest_framework import generics, permissions
from .models import Follower
from .serializers import FollowerSerializer
from django_restf.permissions import IsOwnerOrReadOnly


class FollowerList(generics.ListCreateAPIView):
    """
    List all followers, i.e.. all instances of a 
    user following another user.
    Create a follower, i.e.. follow a user if logged in.
    Perform_class: associate the current logged in user with a follower.
    """
    serializer_class = FollowerSerializer
    queryset = Follower.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class FollowerDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a follower.
    No update view, as we either follow or unfollow users.
    Destroy a follower, i.e.. unfollow someone if owner.
    """
    serializer_class = FollowerSerializer
    queryset = Follower.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
