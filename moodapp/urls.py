from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('mood/<str:mood_name>/', views.mood_detail, name='mood_detail'),
]