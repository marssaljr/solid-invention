from django.db import models
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)


class Post(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=120)
    tags = models.ManyToManyField(Tag, related_name="tags")
    img = models.TextField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = (
            "-updated_at",
            "-created_at",
        )
