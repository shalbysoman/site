from django.db import models
from datetime import datetime


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Movie(models.Model):
    image = models.ImageField(null=False, blank=False)
    title = models.CharField(max_length=200, null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=False, null=True)
    date = models.TextField()
    actors = models.TextField()
    description = models.TextField()
    trailer = models.URLField()
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    username = models.CharField(max_length=200)


    def __str__(self):
        return self.title

        #return '%s - %s' % (self.title, self.commenter_name)


class Comment(models.Model):
    product = models.ForeignKey(Movie, related_name="comments", on_delete=models.CASCADE)
    commenter_name = models.CharField(max_length=200)
    comment_body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.product.name, self.commenter_name)


