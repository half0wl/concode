from rest_framework import serializers
from django.contrib.auth.models import User
from core.models import UserProfile, Project


class UserSerializer(serializers.ModelSerializer):

    bio = serializers.CharField(source='profile.bio', allow_blank=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'bio')
        read_only_fields = ('id', 'first_name', 'last_name', 'username')
        write_only_fields = ('bio')

    def update(self, instance, validated_data):
        '''
        Only save changes to `instance.profile`.
        '''
        instance.profile.bio = validated_data['profile']['bio']
        instance.profile.save()
        return instance


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('owner', 'created_on', 'stage', 'name', 'description',
                  'collaborators')
