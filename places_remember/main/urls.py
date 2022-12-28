from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.index, name = 'index'),
  path('add_post', views.add_post, name = 'add_post'),
  path('create_post', views.add_post, name = 'create_post'),
]