from django.http import HttpResponse

from .models import News


def index(request):
    # print(dir(request))
    news = News.objects.all()
    res = '<h1>NORUTYUNNER</h1>'
    for it in news:
        res += f'<div><p>{it.title}</p><p>{it.content}</p></div><hr>'
    return HttpResponse(res)


def test(request):
    return HttpResponse('<h1>TESTTTT</h1>')
