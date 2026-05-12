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
    program = models.OneToOneField(Program, on_delete=models.CASCADE, related_name="detail")
    page_title = models.CharField(max_length=255)
    intro = models.TextField(blank=True)

    section1_title = models.CharField(max_length=255, blank=True)
    section1_content = models.TextField(blank=True)

    section2_title = models.CharField(max_length=255, blank=True)
    section2_content = models.TextField(blank=True)

    section3_title = models.CharField(max_length=255, blank=True)
    section3_content = models.TextField(blank=True)

    media_file = models.FileField(upload_to="program_detail_media/", blank=True, null=True)
    revised_year = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.page_title

