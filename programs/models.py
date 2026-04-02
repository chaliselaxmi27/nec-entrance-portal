from django.db import models
from django.utils.text import slugify


class Program(models.Model):

    name = models.CharField(max_length=200)

    slug = models.SlugField(unique=True, blank=True)

    short_description = models.TextField()

    seats = models.PositiveIntegerField(default=0)

    shift = models.CharField(max_length=50, blank=True)

    duration = models.CharField(max_length=100, blank=True)

    image = models.ImageField(upload_to="programs/", blank=True, null=True)

    display_order = models.PositiveIntegerField(default=0)

    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['display_order']

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class ProgramDetail(models.Model):

    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name="details")

    section_title = models.CharField(max_length=255)

    content = models.TextField()

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.program.name} - {self.section_title}"