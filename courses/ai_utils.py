# courses/ai_utils.py
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

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
