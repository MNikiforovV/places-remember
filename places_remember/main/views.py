from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import PostForm
from . import database as db


# Main page view method. Renders index.html and sends posts by user
# and user profile if user logged in.
def index(request):
    context = {}
    if request.user.is_authenticated:
        posts = db.get_posts_by_user(request.user)
        profile = db.get_user_profile(request.user)

        context = {
            'posts': posts,
            'profile': profile,
        }
    return render(request, 'index.html', context=context)


# Add post view method. If request is Post receives PostForm from
# HTML page and saves it to DB.
# If request method is Get creates PostForm and sends it to HTML page.
# Renders post.html template.
@login_required
def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('index')
    form = PostForm()
    profile = db.get_user_profile(request.user)
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'post.html', context=context)


# View post by user method. Gets object of user post from DB.
# View post and add post methods share the same template and is_view
# variable used at post.html template to disable some HTML blocks.
@login_required
def view_post(request, post_id):
    obj = db.get_post_by_id(post_id)
    form = PostForm(instance=obj)
    profile = db.get_user_profile(request.user)
    context = {
        'is_view': True,
        'form': form,
        'profile': profile,
    }
    return render(request, 'post.html', context=context)
