from django.shortcuts import render, get_object_or_404, redirect

from .models import News, Category
from .forms import NewsForm

def index(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'Norutyunneri cank'
    }
    return render(request, template_name='news/index.html', context=context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    context = {
        'news': news,
        'category': category
    }
    return render(request, template_name='news/category.html', context=context)


def view_news(request, news_id):
    # news_item = News.objects.get(pk=news_id)
    news_item = get_object_or_404(News, pk=news_id)
    return render(request, 'news/view_news.html', {"news_item": news_item})


def add_news(request):
    if request.method == 'POST':
        my_form = NewsForm(request.POST)
        print('----------------------->', request.POST)

        if my_form.is_valid():
            print('-----------------------<',my_form.cleaned_data)
            news = News.objects.create(**my_form.cleaned_data)
            return redirect(news)
    else:
        my_form = NewsForm()
    return render(request, 'news/add_news.html', {'my_form': my_form})
