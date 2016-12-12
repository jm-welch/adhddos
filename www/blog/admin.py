from django.contrib import admin
from .models import *
from django.db.models.functions import Lower
from django.utils.text import slugify
import itertools

# Register your models here.

# @admin.register(<model>)
# class <Model>Admin(admin.ModelAdmin):
#     pass

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
