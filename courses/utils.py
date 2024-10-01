from django.core.cache import cache
import requests
from bs4 import BeautifulSoup

def fetch_course_image(url):
    # Try fetching the image from cache first
    cached_image = cache.get(url)
    if cached_image:
        return cached_image
    
    # If not cached, fetch from the external URL
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        meta_image_tag = soup.find('meta', property='og:image')
        if meta_image_tag:
            image_url = meta_image_tag['content']
            # Cache the image URL with the course link as the key
            cache.set(url, image_url, timeout=60 * 60 * 24)  # Cache for 1 day (adjust timeout as needed)
            return image_url
    
    return "https://via.placeholder.com/300x200"