from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.utils import timezone
from .models import Post
from django_markdown.utils import markdown

# Create your views here.
def post_list(request):
    """ List of published blog posts, most recent first """
    posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
    return render(request, 'post_list.html', {'posts': posts})

def one_post(request, slug):
    """ Get a single post by slug """
    if slug is None:
        return post_list(request)

    post = get_object_or_404(Post, slug=slug)
    if post.publish_date <= timezone.now():
        post.views += 1
        post.save()
        return render(request, 'one_post.html', {'post': post})

    raise Http404

def tag_list(request, tags):
    """ View posts with the given tags (tags should be +-delimited) """
    pass
