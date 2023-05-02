from django.contrib.auth.views import LogoutView
from django.urls import path, include

urlpatterns = [
  path('', include('social_django.urls', namespace='social')),
  path('logout/', LogoutView.as_view(), name='logout'),
]
