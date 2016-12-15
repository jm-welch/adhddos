from django.contrib import admin
from .models import *
from django.db.models.functions import Lower
from django.utils.text import slugify
import itertools

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    def PublishPost(self, request, queryset):
        for post in queryset:
            post.publish()
    PublishPost.short_description = "Publish post now"

    def UnPublishPost(self, request, queryset):
        for post in queryset:
            post.publish_date = ''
    UnPublishPost.short_description = "Unpublish post"

    list_display = ['title', 'publish_date', 'tags']
    #TODO: Find a better way to make the publish function quickly editable from the admin
    # list_editable = ['publish_date']
    search_fields = ['title', 'body', 'tags']
    actions = [PublishPost, UnPublishPost]

    #TODO: Find a way to filter by tags in taglist

    date_hierarchy = 'created_date'
