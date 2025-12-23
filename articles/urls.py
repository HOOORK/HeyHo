from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Главная страница
    path('list/', views.article_list, name='article_list'),  # Измените URL на list/
    path('create/', views.article_create, name='article_create'),
    path('<int:id>/edit/', views.article_edit, name='article_edit'),
]