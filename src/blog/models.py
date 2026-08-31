from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
#user.author_posts.all()  # all posts by this user

class Post(models.Model):
    author =models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_posts')

    class Status(models.TextChoices):
        DRAFT = 'draft', 'Draft'
        PUBLISHED = 'published', 'Published'

    title = models.CharField(max_length=200)
    body = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)

    publish = models.DateTimeField(default = timezone.now)
    created = models.DateTimeField(auto_now_add = True ,null = True)
    updated = models.DateTimeField(auto_now = True ,null= True)

    status = models.CharField(max_length=10, choices=Status, default=Status.DRAFT)

    def __str__(self):
        return self.title