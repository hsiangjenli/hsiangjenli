def is_abs_url(url, static_prefix):
    if url.startswith('http'):
        return url
    
    return f"{static_prefix}/{url}"
