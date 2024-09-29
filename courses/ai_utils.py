# courses/ai_utils.py
from sentence_transformers import SentenceTransformer
import requests
from bs4 import BeautifulSoup
# Load pre-trained sentence transformer model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

from django.core.cache import cache
import requests
from bs4 import BeautifulSoup

# Function to fetch and cache the course image
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


def get_vector(text):
    """
    This function computes the vector representation of a given text (course title).
    """
    return model.encode(text)

def recommend_courses(user_profile):
    """
    Recommend courses to the user by comparing the similarity of course vectors
    to the user profile's certifications/skills.
    """
    # Fetch all courses
    from courses.models import Course
    all_courses = Course.objects.all()

    # Get vector for user certifications or profile description
    user_vector = get_vector(user_profile.certifications)

    # List to store recommended courses
    recommendations = []

    for course in all_courses:
        # Get vector for each course title
        course.image_url = fetch_course_image(course.link)  # Dynamically assign the image URL
        course_vector = get_vector(course.name)

        # Compute cosine similarity between user profile and course
        similarity_score = cosine_similarity(user_vector, course_vector)

        # Add to recommendations if the similarity is above a threshold
        if similarity_score > 0.3:  # Adjust the threshold as needed
            recommendations.append(course)

    return recommendations

def cosine_similarity(vec1, vec2):
    """
    Compute the cosine similarity between two vectors.
    """
    from numpy import dot
    from numpy.linalg import norm
    return dot(vec1, vec2) / (norm(vec1) * norm(vec2))
