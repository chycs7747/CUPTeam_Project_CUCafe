from django.urls import path
from . import views

app_name = 'oauth'

urlpatterns = [
    path('login/google/', views.main_index, name='main_index'),
    path('llogin/google/callback/', views.main_index, name='main_index'),
]