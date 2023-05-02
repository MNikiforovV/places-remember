from .models import Post
from auth.models import UserProfile


# Methods for working with DB.
def get_posts_by_user(user):
    return Post.objects.filter(user=user)


def get_post_by_id(id):
    return Post.objects.get(id=id)


def get_user_profile(user):
    return UserProfile.objects.get(user=user)
