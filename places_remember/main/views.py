from django.shortcuts import render, redirect
from .models import Post, UserProfile
from .forms import PostForm

def index(request):
    context = {}
    if request.user.is_authenticated:
        posts = Post.objects.filter(user=request.user)
        profile = UserProfile.objects.get(user=request.user)

        context = { 
        'posts': posts,
        'profile': profile, 
        }
    return render(request, 'index.html', context=context)

def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('index')

    form = PostForm()
    context = {
        'form': form,
        'profile': UserProfile.objects.get(user=request.user),
    }
    return render(request, 'post.html', context=context)

def view_post(request, post_id):
    obj = Post.objects.get(id=post_id)
    form = PostForm(instance=obj)
    context = {
        'is_view': True,
        'form': form,
        'profile': UserProfile.objects.get(user=request.user),
    }
    return render(request, 'post.html', context=context)