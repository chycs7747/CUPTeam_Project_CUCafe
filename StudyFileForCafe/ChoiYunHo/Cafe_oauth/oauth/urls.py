from django.urls import path
from . import views_login

app_name = 'oauth'

urlpatterns = [
    path('login/google/', views_login.OauthLogin.google_login, name='google-login'),
    path('login/google/callback/', views_login.OauthLogin.google_callback, name='google-callback'),
]