from rest_framework import viewsets, permissions
from django.contrib.auth.models import User
from .models import UserProfile, Activity
from .serializers import UserSerializer, UserProfileSerializer, ActivitySerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.select_related('user').all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.select_related('user').all()
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated]
