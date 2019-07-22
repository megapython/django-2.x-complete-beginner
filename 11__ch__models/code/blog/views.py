from django.shortcuts import render, get_object_or_404

from .models import Post


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
