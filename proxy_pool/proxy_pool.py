import random
from proxy_pool.free_proxy import fetch_free_proxies

_cached_proxies = []

def get_random_proxy():
    global _cached_proxies
    if not _cached_proxies:
        _cached_proxies = fetch_free_proxies()
    if not _cached_proxies:
        return None  # fallback
    return random.choice(_cached_proxies)
