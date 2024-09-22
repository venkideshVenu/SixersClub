from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _

import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    USER_TYPES = (
        ('team_manager', 'Team Manager'),
        ('player', 'Player'),
        ('fan', 'Fan'),
    )

    user_type = models.CharField(max_length=20, choices=USER_TYPES, default='fan')
    email = models.EmailField(unique=True)

    # Fields for Team Managers and Players
    experience_level = models.CharField(max_length=50, blank=True, null=True)
    role = models.CharField(max_length=30, blank=True, null=True)  # e.g., Batsman, Bowler
    player_id = models.CharField(max_length=10, blank=True, null=True, unique=True)

    groups = models.ManyToManyField(Group, related_name='customuser_groups', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_user_permissions', blank=True)

    def save(self, *args, **kwargs):
        # Generate a unique player_id for players if it's not already set
        if self.user_type == 'player' and not self.player_id:
            self.player_id = self.generate_player_id()
        super(CustomUser, self).save(*args, **kwargs)

    def generate_player_id(self):
        """
        Generate a unique player_id for the user using a UUID.
        """
        return str(uuid.uuid4())[:8]  # Generate a short 8-character unique ID

    def __str__(self):
        return self.username

    @property
    def is_team_manager(self):
        return self.user_type == 'team_manager'

    @property
    def is_player(self):
        return self.user_type == 'player'

    @property
    def is_fan(self):
        return self.user_type == 'fan'
