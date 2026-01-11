from django.core.cache import cache
from .models import Property
import logging
from django_redis import get_redis_connection


logger = logging.getLogger(__name__)



def get_all_properties():
    cache_key = "all_queryset"

    queryset = cache.get(cache_key)

    if queryset is None:
        queryset = Property.objects.all()
        cache.set(cache_key, queryset, 3600)

    return queryset




def get_redis_cache_metrics():
    """
    Retrieve Redis cache hit/miss metrics and calculate hit ratio
    """
    try:
        redis_conn = get_redis_connection("default")
        info = redis_conn.info()

        hits = info.get("keyspace_hits", 0)
        misses = info.get("keyspace_misses", 0)

        total_requests = hits + misses
        hit_ratio = hits / total_requests if total_requests > 0 else 0

        metrics = {
            "keyspace_hits": hits,
            "keyspace_misses": misses,
            "hit_ratio": hit_ratio,
        }

        logger.info(
            "Redis Cache Metrics | Hits: %s | Misses: %s | Hit Ratio: %s",
            hits,
            misses,
            hit_ratio,
        )

        return metrics

    except Exception as e:
        logger.error("Failed to retrieve Redis cache metrics: %s", e)
        return {
            "keyspace_hits": 0,
            "keyspace_misses": 0,
            "hit_ratio": 0,
        }
