from django.db import models
from django.contrib.auth.models import User


PROJECT_STAGES = (
    ('CONCEPT', 'Concept'),
    ('DEV', 'In Development'),
    ('BETA', 'In Beta'),
    ('LAUNCHED', 'Launched')
)


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    bio = models.TextField(default='', blank=True)


class Project(models.Model):
    owner = models.ForeignKey(User)
    created_on = models.DateTimeField(auto_now_add=True)
    stage = models.CharField(choices=PROJECT_STAGES, max_length=30)
    name = models.CharField(max_length=255)
    description = models.TextField()
    collaborators = models.ManyToManyField(User, related_name='Collaborators')
