from django.shortcuts import render, get_object_or_404, redirect, reverse

from .models import Post
from .forms import CreatePostForm, UpdatePostForm


# Home Page / List View
def home_page(request):
    # Retreive all the posts
    all_posts = Post.objects.all()
    context = {
        "posts": all_posts
    }
    return render(request, 'blog/index.html', context)


# Post Detail / Detail View
def post_detail(request, pk):
    # Retreive the post or show a 404 page
    post = get_object_or_404(Post, pk=pk)
    context = {
        'post': post
    }
    return render(request, 'blog/post_detail.html', context)


# Create Post / Create View
def create_post(request):
    # If request is of type POST
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            # Save form only if valid
            form.save()
            return redirect('home')
    else:
        # Otherwise request is of type GET
        form = CreatePostForm()
    # Create our context variable and assign our form
    context = {
        'form': form
    }
    return render(request, 'blog/create_post.html', context)


# Update Post / Update View
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = UpdatePostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=pk)
    else:
        form = UpdatePostForm(instance=post)
    context = {
        'form': form
    }
    return render(request, 'blog/post_update.html', context)


# Delete Post Confirmation
def post_delete_confirm(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {
        'post': post
    }
    return render(request, 'blog/post_delete_confirm.html', context)


# Delete Post / Delete View
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('home')
