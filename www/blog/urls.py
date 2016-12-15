from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'(?P<slug>[^/]+)?/?$', views.one_post, name='one_post'),
]
