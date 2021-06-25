from django.shortcuts import render, redirect, reverse
from app.web.forms import NewsForm
from app.api.models import News


# Create your views here.

def home(request):
    return render(request, 'pages/list.html', {})


def add_news(request):
    mi_form = NewsForm()
    # Validacmos el formulario
    if request.method == 'POST':
        mi_form = NewsForm(request.POST)
        # Muestro los errores
        if mi_form.is_valid():
            mi_news_new = News()
            mi_news_new.title = mi_form.cleaned_data['title']
            mi_news_new.url = mi_form.cleaned_data['url']
            # Guardo
            mi_news_new.save()
            # Redirección
            return redirect(reverse('list'))
    return render(request, 'pages/add-news.html', {
        "news_form": mi_form,
    })
