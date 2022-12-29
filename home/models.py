from django.db import models
from django.contrib.auth.models import User
from django.urls.base import reverse
#from django.urls import reverse
#from datetime import datetime

# Create your models here.

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=False)
    status = models.IntegerField(choices=STATUS, default=0)
    objects = models.Manager()
    #image = models.ImageField(upload_to='post-detail/', blank=True, null=True)
    published_date = models.DateTimeField(auto_now_add=False,
                                          blank=False, null=False)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    class Meta:
        ordering = ['-created_on']

    # def save(self, *args, **kwargs):
    #     # Set publish date to the date post is published, reset if unpublished
    #     if self.published and self.created_on is None:
    #         self.created_on = datetime.now()
    #     elif not self.published and self.created_on is not None:
    #         self.created_on = None
    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.title + ' | ' + str(self.author) + ' | ' + str(self.published_date)

    # def get_absolute_url(self):
    #     return reverse('post-detail', args=(str(self.id)))



class Contact(models.Model):
    name    = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField(max_length=350)

    def __str__(self):
        return f"{self.name} - {self.email} - {self.message}"
