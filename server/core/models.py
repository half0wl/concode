from django.db import models
from django.db.models import signals
from django.contrib.auth.models import User


PROJECT_STAGES = (
    ('CONCEPT', 'Concept'),
    ('DEV', 'In Development'),
    ('BETA', 'In Beta'),
    ('LAUNCHED', 'Launched')
)


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    bio = models.TextField(default='', blank=True)

    def __str__(self):
        return self.user.username

    def create_profile(sender, **kwargs):
        user = kwargs['instance']
        if kwargs['created']:
            user_profile = UserProfile(user=user, bio='Hello!')
            user_profile.save()

    signals.post_save.connect(create_profile, sender=User)


class Project(models.Model):
    owner = models.ForeignKey(User)
    created_on = models.DateTimeField(auto_now_add=True)
    stage = models.CharField(choices=PROJECT_STAGES, max_length=30)
    name = models.CharField(max_length=255)
    description = models.TextField()
    collaborators = models.ManyToManyField(User, related_name='Collaborators')
