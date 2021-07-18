from django.shortcuts import render

from .models import News, Category


def index(request):
    # print(dir(request))
    # res = '<h1>NORUTYUNNER</h1>'
    # for it in news:
    #     res += f'<div><p>{it.title}</p><p>{it.content}</p></div><hr>'
    # return HttpResponse(res)

    # news = News.objects.order_by("-created_at")
    news = News.objects.all()
    categories = Category.objects.all()
    context = {
        'news': news,
        'title': 'Norutyunneri cank',
        'categories': categories
    }

    return render(request, template_name='news/index.html', context=context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    context = {
        'news': news,
        'categories': categories,
        'category': category
    }
    return render(request, template_name='news/category.html', context=context)
