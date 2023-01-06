from django.urls import path, include
from . import views
from board import urls
from user import urls

app_name = 'cafe'

urlpatterns = [
    path('user/', include('user.urls')),
    path('board/', include('board.urls')),
]