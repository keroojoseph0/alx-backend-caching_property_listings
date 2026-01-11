from django.core.cache import cache
from .models import Property

def get_all_properties():
    cache_key = "all_queryset"

    queryset = cache.get(cache_key)

    if queryset is None:
        print("❌ CACHE MISS")
        queryset = list(Property.objects.values())
        cache.set(cache_key, queryset, 3600)
    else:
        print("✅ CACHE HIT")

    return queryset
