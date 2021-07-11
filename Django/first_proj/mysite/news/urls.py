from django.urls import path

from .views import index
# from .views import test

urlpatterns = [
    path('', index),
    # path('test/', test)
]
