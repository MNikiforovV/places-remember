from .models import UserProfile

# Pipeline for getting profile picture from Google
# and saving it to UserProfile.


def save_profile(backend, user, response, is_new=False, *args, **kwargs):
    if backend.name == 'google-oauth2':
        if response.get('picture'):
            pic = response['picture']
            UserProfile.objects.filter(user=user).update(imageUrl=pic)
