from rest_framework import serializers
from django.contrib.auth.models import User
from core.models import UserProfile, Project


class UserSerializer(serializers.ModelSerializer):

    bio = serializers.CharField(source='profile.bio', allow_blank=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'bio')
