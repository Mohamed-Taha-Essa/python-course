#fat model thin views

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.
#user.author_posts.all()  # all posts by this user

#custom manager type 1
class PostManager(models.Manager):
    def published(self):
        return self.filter(status =Post.Status.PUBLISHED)

    def draft(self):
        return self.filter(status = Post.Status.DRAFT)


#custom manager type 2 
class PublishedManager(models.Manager):
    def get_queryset(self):
        query =  super().get_queryset()
        return query.filter(status = Post.Status.PUBLISHED)

class Post(models.Model):
    author =models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_posts')

    class Status(models.TextChoices):
        DRAFT = 'draft', 'Draft'
        PUBLISHED = 'published', 'Published'

    title = models.CharField(max_length=200)
    body = models.TextField()
    slug = models.SlugField(max_length=200, unique=True ,null =True ,blank=True)

    publish = models.DateTimeField(default = timezone.now)
    created = models.DateTimeField(auto_now_add = True ,null = True)
    updated = models.DateTimeField(auto_now = True ,null= True)

    status = models.CharField(max_length=10, choices=Status, default=Status.DRAFT)

    objects = models.Manager() # the default manager (all objects)
    published =PublishedManager()   # our custom manager 


    class Meta:
        # ordering=['-publish']
        # ordering=['publish']
        ordering=['publish' ,'title'] # first apply date of publishe asc by title
        verbose_name = 'blog posts'
        indexes = [
            # models.Index(fields=['publish'])
            models.Index(fields=['-publish' ])
        ]
 

    def save(self , *args ,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args ,**kwargs)

    def get_absolute_url(self):

        return reverse('blog:post_detail' ,args = [self.slug])

    def __str__(self):
        return self.title

# post.comments.all()
class Comment(models.Model):
    post =models.ForeignKey(Post ,related_name='comments' ,on_delete=models.CASCADE)

    name = models.CharField(max_length = 100)
    email = models.EmailField()
    body = models.TextField()

    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    active = models.BooleanField(default = True)

    def __str__(self):
        return f'Comment by {self.name}'