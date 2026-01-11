from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from properties.models import Property
from django.core.cache import cache

@receiver(post_save, sender=Property)
@receiver(post_delete, sender=Property)
def clear_property_cache(sender, instance, **kwargs):
    cache.delete('all_properties')
