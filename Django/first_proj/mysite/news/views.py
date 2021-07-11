from django.shortcuts import render

from .models import News


def index(request):
    # print(dir(request))
    # res = '<h1>NORUTYUNNER</h1>'
    # for it in news:
    #     res += f'<div><p>{it.title}</p><p>{it.content}</p></div><hr>'
    # return HttpResponse(res)

    news = News.objects.order_by("-created_at")

    context = {
        'news': news,
        'title': 'Norutyunneri cank'
    }

    return render(request, 'news/index.html', context)

#
# def test(request):
#     return HttpResponse('<h1>TESTTTT</h1>')
