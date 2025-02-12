from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,unique=True)
    published = models.BooleanField(max_length=False)

    def __str__(self):
        return self.title