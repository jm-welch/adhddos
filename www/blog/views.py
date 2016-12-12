from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
    """ List of published blog posts, most recent first """
    posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
    return render(request, 'post_list.html', {'posts': posts})
