from django.urls import path

from .views import login_view, forgot_password, reset_password, test
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login', login_view, name='login'),
    path('register/<str:hash>/', reset_password, name='register'),
    path('reset-password/<str:hash>/', reset_password, name='reset-password'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('forgot-password/', forgot_password, name='forgot-password'),
    path('test', test),
]
