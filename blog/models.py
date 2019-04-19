from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    icon = models.ImageField(upload_to='uploads/blog', blank=True)
    description =  models.TextField()
    is_active = models.BooleanField(default=True)
    created_date = models.DateField(auto_now=False, auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name

class PostQueryset(models.query.QuerySet):
    def publish(self):
        return self.filter(status='publish', category__is_active=True)

class PostManager(models.Manager):
    def get_queryset(self):
        return PostQueryset(self.model, using=self._db)

    def publish(self):
        return self.get_queryset().publish()


class Post(models.Model):
    STATUS_POST = (
        ('draft', 'Draft'),
        ('publish', 'Publish')
        )
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='category')
    image = models.ImageField(upload_to='uploads/blog', blank=True)
    content = models.TextField()
    status = models.CharField(max_length=100, blank=False, choices=STATUS_POST, default='publish')
    seo_keywords = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    created_date = models.DateField(auto_now=False, auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True, auto_now_add=False)

    objects = PostManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:single", kwargs={'slug': self.slug})

    def get_comment_count(self):
        return Comment.objects.filter(post__id = self.id, status='publish').count()


class Comment(models.Model):
    STATUS_COMMENT = (
        ('spam', 'Spam'),
        ('publish', 'Publish')
        )
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post')
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=150)
    body = models.TextField()
    created_date = models.DateField(auto_now=False, auto_now_add=True)
    status = models.CharField(max_length=100, blank=False, choices=STATUS_COMMENT, default='publish')

    def __str__(self):
        return self.name

