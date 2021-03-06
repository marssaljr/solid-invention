from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=120)
    tags = models.ManyToManyField(Tag, related_name="tags")
    img = models.TextField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    """
    @property
    def tags_name(self):
        return [x.name for x in self.tags]
    """

    class Meta:
        ordering = (
            "-updated_at",
            "-created_at",
        )
