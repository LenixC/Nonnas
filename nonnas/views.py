from django.shortcuts import get_object_or_404, render

from .models import Post

def homepage(request):
    post_list = Post.objects.all()
    context = {'post_list': post_list}
    return render(request, 'nonnas/homepage.html', context)

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'nonnas/detail.html', {'post': post})
