from django.shortcuts import render
from app.api.models import News


# Create your views here.

def home(request):
    return render(request, 'pages/list.html', {
        'news': News.objects.all()
    })


def add_news(request):
    return render(request, 'pages/add-news.html', {

    })
