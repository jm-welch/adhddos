from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'tags/(?P<tags>[^/]+)?$', views.by_tags, name='by_tags'),
    url(r'(?P<slug>[^/]+)?/?$', views.one_post, name='one_post'),
]
