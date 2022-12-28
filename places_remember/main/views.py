from django.shortcuts import render
from .models import Post, UserProfile
def index(request):
    context = {}
    if request.user.is_authenticated:
        context = { 'posts': get_all_posts(request.user) }
    return render(request, 'index.html')

def add_post(request):
    return render(request, 'add_post.html')

def create_post(request):
    if request.method == "POST":
        post = request

async def get_all_posts(user):
    Post.objects.get(user=user)