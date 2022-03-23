from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *

# Create your views here.

def index(request):
    pots = Post.objects.all()
    return render(request, 'blog/post.html', {'posts' : pots})

def detail(request, pk):

    # from django.contrib.auth.models import User
    # user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    # user.last_name = 'Lennon'
    # user.save()

    from django.core.mail import send_mail

    # send_mail(
    #     'Subject here',
    #     'Привет гений',
    #     'from@example.com',
    #     ['inventor959@gmail.com'],
    #     fail_silently=False,
    # )


    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detail.html', {'post' : post})

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published = timezone.now()
            post.save()
            return redirect('index')
    else:
        form = PostForm()



    return render(request, 'blog/new.html', {'form': form})


def post_edit(request, pk):
    pass