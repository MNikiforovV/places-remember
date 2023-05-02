import pytest
from django.urls import reverse
from . import views
from .models import Post, User
from auth.models import UserProfile


def test_index(client):
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200


def test_index_authorized(client, django_user_model):
    _ = create_user(client, django_user_model)
    url = reverse('index')
    response = client.get(url, follow=True)
    assert response.status_code == 200


def test_add_post_non_authorized(client):
    url = reverse('add_post')
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_add_post_authorized(client, django_user_model):
    _ = create_user(client, django_user_model)
    url = reverse('add_post')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_add_post_create(client, django_user_model):
    user = create_user(client, django_user_model)
    url = reverse('add_post')
    form = {
        "title": "test", "description": "test",
        "latitude": "50", "longitude": "90", "user": user
    }
    response = client.post(url, form)
    assert response.status_code == 302


@pytest.mark.django_db
def test_view_post(client, django_user_model):
    user = create_user(client, django_user_model)
    post = Post.objects.create(
        title="test", description="test",
        latitude="0", longitude="0", user=user
        )
    url = reverse('view_post', kwargs={"post_id": post.id})
    response = client.get(url)
    assert response.status_code == 200


# Testing helper methods
@pytest.mark.django_db
def test_get_posts_by_user(client):
    user = User.objects.create(username="test", password="1111")
    post = Post.objects.create(
        title="test", description="test",
        latitude="0", longitude="0", user=user
        )
    posts = views.get_posts_by_user(user=user)
    assert post in posts


@pytest.mark.django_db
def test_get_post_by_id(client):
    user = User.objects.create(username="test", password="1111")
    post = Post.objects.create(
        title="test", description="test",
        latitude="0", longitude="0", user=user
        )
    found_post = views.get_post_by_id(post.id)
    assert found_post.id == post.id


@pytest.mark.django_db
def test_get_profile_by_user(client):
    user = User.objects.create(username="test", password="1111")
    profile = UserProfile.objects.get(id=user.id)
    found_profile = views.get_user_profile(user=user)
    assert profile.id == found_profile.id


def create_user(client, django_user_model):
    username = "test"
    password = "1111"
    user = django_user_model.objects.create_user(
        username=username,
        password=password
        )
    client.login(username=username, password=password)
    return user
