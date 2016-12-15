from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.utils import timezone
from .models import Post
from django_markdown.utils import markdown
from collections import Counter

def published_posts():
    """ Return a list of posts, most recent first """
    return Post.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')[::-1]

def post_list(request):
    """ List of published blog posts, most recent first """
    #TODO: "Read More" link (page fold) id:12 gh:13
    posts = published_posts()
    return render(request, 'post_list.html', {'posts': posts})

def one_post(request, slug):
    """ Get a single post by slug """
    if slug is None:
        return post_list(request)

    post = get_object_or_404(Post, slug=slug)
    if post.publish_date <= timezone.now():
        post.views += 1
        post.save()
        return render(request, 'one_post.html', {'post': post, 'info': post.title})

    raise Http404

#WIP: Handle tags id:11 gh:12
def tag_list(request):
    tags = Counter(tag for post in published_posts() for tag in post.taglist)
    return render(request, 'tag_list.html', {'tags': tags.most_common(), 'info': 'All tags'})

def by_tags(request, tags):
    """ View posts with all of the given tags (tags should be +-delimited) """
    if tags is None:
        return tag_list(request)

    tags_l = tags.split('+')

    posts = []

    for post in published_posts():
        if all([tag in post.taglist for tag in tags_l]):
            posts.append(post)

    return render(request, 'post_list.html', {'posts': posts, 'info': 'Posts tagged "{tags}"'.format(tags=tags)})
