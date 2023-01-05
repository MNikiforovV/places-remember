from .models import UserProfile

def save_profile(backend, user, response, is_new=False, *args, **kwargs):
    if is_new and backend.name == "facebook":
        # The main part is how to get the profile picture URL and then do what you need to do
        UserProfile.objects.filter(user=user).update(
            imageUrl='https://graph.facebook.com/{0}/picture/?type=large&access_token={1}'.format(response['id'],
                                                                                                  response[
                                                                                                      'access_token']))
    elif backend.name == 'google-oauth2':
        if response.get('picture'):
            UserProfile.objects.filter(user=user).update(imageUrl=response['picture'])