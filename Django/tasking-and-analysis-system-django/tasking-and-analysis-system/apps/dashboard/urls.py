from django.urls import path, re_path

from . import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path("view_more/", views.view_more, name='view_more'),

    # Matches any html file
    re_path(r'^.*\.*/', views.pages, name='error404'),
    re_path(r'^.*\.*/', views.error403, name='error403'),
]
