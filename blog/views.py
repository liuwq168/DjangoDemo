from django.shortcuts import render


posts = [
    {
        'author': 'Andong',
        'title': 'Post One',
        'content': 'First post content',
        'date_posted': 'Jan, 2019'
    },
    {
        'author': 'Puppetect',
        'title': 'Post Two',
        'content': 'Second post content',
        'date_posted': 'Feb, 2019'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
