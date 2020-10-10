from django.urls import path, include
from . import views
urlpatterns = [
    path('news_all/', views.ShowNewsAllView.as_view(), name='news-all'), # Страница со всеми статьями
    path('', views.ShowNewsView.as_view(), name='main'),# Главная
    path('contact/', views.contact, name='contact'),# Контакты
    path('history_creat/', views.history_creat, name='history_creat'),# history_creat
    path('recent_events/', views.recent_events, name='recent_events'),# recent_events
    path('new/<int:pk>/', views.NewsDetailView.as_view(), name='news-detail'), # Страница-развертывание статей
]
