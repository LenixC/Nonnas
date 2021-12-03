from django.db import models
from django.forms import ModelForm

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    votes = models.IntegerField(default=1, editable=False)

    def __str__(self):
        return self.title

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
