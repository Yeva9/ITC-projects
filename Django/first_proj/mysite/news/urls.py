from django.urls import path

# from .views import index, get_category, view_news, add_news,
from .views import HomeNews, NewsByCategory, ViewNews, CreateNews, test, register, user_login, user_logout

urlpatterns = [
    # path('', index, name='home'),

    # path('category/<int:category_id>/', get_category, name='category'),
    # path('category/<int:category_id>/', NewsByCategory.as_view(extra_context=
    #                                     {'title': 'CATEGORIES'}), name='category'),
    # path('news/<int:news_id>/', view_news, name='view_news'),
    # path('news/add_news/', add_news, name='add_news'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),

    path('test/', test, name='test'),
    path('', HomeNews.as_view(), name='home'),
    path('category/<int:category_id>/', NewsByCategory.as_view(), name='category'),
    path('news/<int:pk>/', ViewNews.as_view(), name='view_news'),
    path('news/add_news/', CreateNews.as_view(), name='add_news'),
]
