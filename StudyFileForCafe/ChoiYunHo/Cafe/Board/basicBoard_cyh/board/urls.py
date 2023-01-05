from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.main_index, name='main_index'),
    path('board/index/<str:board_name>/', views.board_index, name='board_index'),
    path('board/create/', views.board_create, name='board_create'),
    path('board/create/submit/', views.board_create_submit, name='board_create_submit'),
    path('board/delete/<str:board_name>', views.board_delete, name='board_delete'),

    path('post/index/<str:post_name>/', views.post_index, name='post_index'),
    path('post/modify/<str:post_name>', views.post_modify, name='post_modify'),
    path('post/modify/submit/<str:post_name>', views.post_modify_submit, name='post_modify_submit'),
    path('post/delete/<str:post_name>', views.post_delete, name='post_delete'),
    path('post/create/<str:board_name>', views.post_create, name='post_create'),
    path('post/create/submit/<str:board_name>', views.post_create_submit, name='post_create_submit'),

    path('comment/submit/<str:post_name>', views.post_comment_submit, name='post_comment_submit')
]