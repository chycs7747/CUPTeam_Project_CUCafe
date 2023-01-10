from django.urls import path, include
from . import views
from board import urls
from user import urls

app_name = 'cafe'

urlpatterns = [
    #user app
    path('user/', include('user.urls')),
    path('user/mv/board/', views.mv_user_board, name='mv_user_board'),

    #board app
    path('board/', include('board.urls', namespace='board')),
]