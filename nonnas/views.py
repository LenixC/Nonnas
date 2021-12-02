from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, authenticate, login

from .models import Post

def homepage(request):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=request.POST['post'])
        post.votes += 1
        post.save()
    post_list = Post.objects.all()
    context = {'post_list': post_list}
    return render(request, 'nonnas/homepage.html', context)

def post_detail(request, post_id):
    print(request.user)
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'nonnas/detail.html', {'post': post})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect("nonnas:homepage")
        else:
            print("Oopsy woopsy")

    form = UserCreationForm
    return render(request,
                  "nonnas/register.html",
                  {"form":form})
