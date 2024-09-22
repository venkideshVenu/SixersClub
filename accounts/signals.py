from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser

@receiver(post_save, sender=CustomUser)
def create_player_id(sender, instance, created, **kwargs):
    if created and instance.is_player:
        instance.player_id = f'PLYR-{instance.id:04d}'
        instance.save()
