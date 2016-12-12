import itertools
from django.db import models
from django.utils import timezone
from django.utils.text import slugify

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey('auth.User')
    tags = models.CharField(max_length=200,
                            blank=True, null=True,
                            help_text="Comma-separated list")
    slug = models.SlugField(unique=True, blank=True, null=True,
                            help_text="Auto-generated from title. Must be unique. Clear field and save to generate new slug.")
    created_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(blank=True, null=True)
    views = models.IntegerField(default=0)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def make_slug(self):
        """ Set the slug to enforce uniqueness """
        slug = orig = slugify(self.title)

        for x in itertools.count(1):
            if not Post.objects.filter(slug=slug).exists():
                break
            slug = '{s}-{n}'.format(s=orig, n=x)

        return slug

    def save(self, *args, **kwargs):
        # Override the default .save() method to enforce a unique slug
        if not self.slug:
            self.slug = self.make_slug()
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
