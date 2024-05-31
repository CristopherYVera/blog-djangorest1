from rest_framework import serializers
from comments.models import Comment

class CommnetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','content','create_at','user','post']