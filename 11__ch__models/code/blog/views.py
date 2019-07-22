from django.shortcuts import render, get_object_or_404, redirect

from .models import Post
from .forms import CreatePostForm


# Home Page / List View
def home_page(request):
    # Retreive all the posts
    all_posts = Post.objects.all()
    context = {
        "posts": all_posts
    }
    return render(request, 'blog/index.html', context)


# Post Detail
def post_detail(request, pk):
    # Retreive the post or show a 404 page
    post = get_object_or_404(Post, pk=pk)
    context = {
        'post': post
    }
    return render(request, 'blog/post_detail.html', context)


# Create Post
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
