from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('add_post', views.add_post, name='add_post'),
  path('view_post/<int:post_id>/', views.view_post, name='view_post'),
]
