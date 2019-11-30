from django.urls import path
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('auth/', views.auth, name='auth')
]