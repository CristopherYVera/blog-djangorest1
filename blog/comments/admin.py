from django.contrib import admin
from comments.models import Comment
# Register your models here.
@admin.register(Comment)
class CommentAdjunt(admin.ModelAdmin):
    list_display = ['content','user','post','create_at']