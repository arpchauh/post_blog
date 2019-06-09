from django.shortcuts import render


posts=[

    {
        'author': 'Arpit',
        'title': 'Blog Post1',
        'Content': 'First Post Content',
        'date_posted': 'June 8, 2019'
    },
    {
        'author': 'Mickey',
        'title': 'Blog Post2',
        'Content': 'second Post Content',
        'date_posted': 'June 9, 2019'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blogs/home.html', context)


def about(request):
    return render(request, 'blogs/about.html', {'title': 'About'})
