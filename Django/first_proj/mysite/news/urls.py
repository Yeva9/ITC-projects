from django.urls import path

# from .views import index, get_category
from .views import view_news, add_news, HomeNews, NewsByCategory, ViewNews

urlpatterns = [
    # path('', index, name='home'),

    # path('category/<int:category_id>/', get_category, name='category'),
    # path('category/<int:category_id>/', NewsByCategory.as_view(extra_context=
    #                                     {'title': 'CATEGORIES'}), name='category'),
    # path('news/<int:news_id>/', view_news, name='view_news'),
    path('', HomeNews.as_view(), name='home'),
    path('category/<int:category_id>/', NewsByCategory.as_view(), name='category'),
    path('news/<int:pk>/', ViewNews.as_view(), name='view_news'),
    path('news/add_news/', add_news, name='add_news'),
]
