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

class Comment(models.Model):
    user = models.CharField(max_length=200)
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
