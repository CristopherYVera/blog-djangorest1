from django.db import models
from users.models import User
from categories.models import Category
from django.db.models import SET_NULL
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.SlugField(max_length=255,unique=True)
    miniature = models.ImageField(upload_to='posts/img')
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    published = models.BooleanField(default=False)
    user = models.ForeignKey(User,on_delete=SET_NULL,null=True)
    category = models.ForeignKey(Category,on_delete=SET_NULL,null=True)

    def __str__(self):
        return self.title