from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout
from django.core.mail import send_mail
from .models import News, Category
from .forms import NewsForm, UserRegisterForm, UserLoginForm, ContactForm
from .utils import MyMixin


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # user = form.save()
            # login(request, user)
            messages.success(request, 'Duq hajoghutyamb grancveciq.')
            # return redirect('home')
            return redirect('login')
        else:
            messages.error(request, 'Grancman skhal ka.')
    else:
        form = UserRegisterForm()
    context = {
        'form': form,
    }
    return render(request, 'news/register.html', context)


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()

    return render(request, 'news/login.html', {"form": form})


def user_logout(request):
    logout(request)
    return redirect('login')


def email_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['content'],
                             'yeva.hovnanyan.im.itc@gmail.com', ['yeva@yopmail.com'], fail_silently=True)
            if mail:
                messages.success(request, 'Haghordagrutyuny ugharkvec')
                return redirect('email')
            else:
                messages.error(request, 'Haghordagrutyan ugharkvelu skhal ka')
        else:
            messages.error(request, 'Grancman skhal ka.')
    else:
        form = ContactForm()
    return render(request, 'news/email.html', {"form": form})

    # objects = ['name1', 'name2', 'name3', 'name4', 'name5', 'name5', 'name7', 'name8']
    # paginator = Paginator(objects, 2)
    # page_num = request.GET.get('page', 1)
    # page_objects = paginator.get_page(page_num)
    # return render(request, 'news/email.html', {'page_obj': page_objects})


class HomeNews(MyMixin, ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    # extra_context = {'title': 'Glkhavor'}
    mixin_prop = 'Helloooo'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper('Glkhavor')
        context['mixin_prop'] = self.get_prop()
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)


class NewsByCategory(MyMixin, ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    allow_empty = False
    paginate_by = 2

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper(Category.objects.get(pk=self.kwargs['category_id']))
        return context


class ViewNews(DetailView):
    model = News
    context_object_name = 'news_item'
    # pk_url_kwarg = 'news_id'
    # template_name = 'news/news_detail.html'


class CreateNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    # success_url = reverse_lazy('home')
    # raise_exception = True
    login_url = '/admin/'

# def index(request):
#     news = News.objects.all()
#     context = {
#         'news': news,
#         'title': 'Norutyunneri cank'
#     }
#     return render(request, template_name='news/index.html', context=context)

#
# def get_category(request, category_id):
#     news = News.objects.filter(category_id=category_id)
#     category = Category.objects.get(pk=category_id)
#     context = {
#         'news': news,
#         'category': category
#     }
#     return render(request, template_name='news/category.html', context=context)


# def view_news(request, news_id):
#     # news_item = News.objects.get(pk=news_id)
#     news_item = get_object_or_404(News, pk=news_id)
#     return render(request, 'news/view_news.html', {"news_item": news_item})


# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         # print('----------------------->', request.POST)
#
#         if form.is_valid():
#             # print('-----------------------<',form.cleaned_data)
#             news = News.objects.create(**form.cleaned_data)
#             return redirect(news)
#     else:
#         form = NewsForm()
#     return render(request, 'news/add_news.html', {'form': form})
