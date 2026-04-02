from django.db import models
from django.utils.text import slugify


class Notice(models.Model):

    title = models.CharField(max_length=255)

    slug = models.SlugField(unique=True, blank=True)

    published_date = models.DateField()

    description = models.TextField(blank=True)

    file = models.FileField(upload_to="notices/", blank=True, null=True)

    is_featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['-published_date']

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Requirement(models.Model):

    title = models.CharField(max_length=255)

    description = models.TextField()

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class Scholarship(models.Model):

    title = models.CharField(max_length=255)

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title
    

class Download(models.Model):

    title = models.CharField(max_length=255)

    file = models.FileField(upload_to="downloads/")

    category = models.CharField(max_length=100, default="Important")

    order = models.IntegerField(default=0)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title