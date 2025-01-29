from django import template
from urllib.parse import urlparse, parse_qs

register = template.Library()

@register.filter
def youtube_embed(url):
    """Convert a YouTube URL to an embeddable format."""
    query = urlparse(url)
    if query.hostname in ['www.youtube.com', 'youtube.com']:
        video_id = parse_qs(query.query).get('v', [None])[0]
        return f"https://www.youtube.com/embed/{video_id}"
    if query.hostname == 'youtu.be':
        return f"https://www.youtube.com/embed{query.path}"
    return url
