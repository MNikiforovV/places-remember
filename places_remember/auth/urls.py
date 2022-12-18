from django.conf import settings
from django.contrib.auth.views import logout
from django.urls import path, include

urlpatterns = [
  path('', include('social_django.urls', namespace='social')),
  path('logout/', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
  
]