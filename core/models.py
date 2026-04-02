from django.db import models


class SiteSetting(models.Model):

    college_name = models.CharField(max_length=200, default="Nepal Engineering College")

    phone = models.CharField(max_length=50, blank=True)

    email = models.EmailField(blank=True)

    address = models.CharField(max_length=255, blank=True)

    logo = models.ImageField(upload_to="site/", blank=True, null=True)

    facebook = models.URLField(blank=True)

    linkedin = models.URLField(blank=True)

    youtube = models.URLField(blank=True)

    def __str__(self):
        return self.college_name


class HeroSlide(models.Model):

    title = models.CharField(max_length=255)

    subtitle = models.CharField(max_length=255, blank=True)

    button_text = models.CharField(max_length=100, blank=True)

    button_link = models.URLField(blank=True)

    background_image = models.ImageField(upload_to="hero/")

    is_active = models.BooleanField(default=True)

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title