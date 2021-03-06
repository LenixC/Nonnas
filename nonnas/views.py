from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login

from .models import *

def homepage(request):
    if request.user.is_authenticated:
        user=request.user.username
    else:
        user="Not logged in."

    if request.method == 'POST':
        post = get_object_or_404(Post, pk=request.POST['post'])
        post.votes += 1
        post.save()
    
    post_list = list(Post.objects.all())
    post_list = sorted(post_list, key=lambda x: x.votes, reverse=True)

    context = {'post_list': post_list, 'user': user}
    return render(request, 'nonnas/homepage.html', context)

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comment_list = post.comment_set.all()
    return render(request, 'nonnas/detail.html', {'post': post,
                                  'comment_list': comment_list})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect("nonnas:homepage")
        else:
            print("An error has occured")

    form = UserCreationForm
    return render(request,
                  "nonnas/register.html",
                  {"form":form})

def logout_request(request):
    logout(request)
    return redirect("nonnas:homepage")

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("nonnas:homepage")

    form = AuthenticationForm()
    return render(request,
                  "nonnas/login.html",
                  {"form":form})

def new_post(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                content = form.cleaned_data['content']
                post = Post.objects.create(title = title,
                                           content = content,)
                return redirect("nonnas:homepage")
    else:
        print("You must log in to make a post")

    form = PostForm()
    return render(request,
                  "nonnas/new_post.html",
                  {"form":form})

def post_comment(request, post_id):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = CommentForm(request.POST)
            if form.is_valid():
                user = request.user.username
                content = form.cleaned_data['content']
                post = Post.objects.get(pk=post_id)
                comment = Comment.objects.create(user = user,
                                           content = content,
                                           post = post,)
                redirect_tag = "/nonnas/" + str(post_id) + "/"
                return redirect(redirect_tag)
    else:
        print("You must log in to make a post")

    form = CommentForm()
    return render(request,
                  "nonnas/post_comment.html",
                  {"form":form})
