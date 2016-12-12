from django.contrib import admin
from .models import *
from django.db.models.functions import Lower
from django.utils.text import slugify
import itertools


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    #TODO: Show more columns id:16
    #TODO: "Publish" option for post id:17
    pass
