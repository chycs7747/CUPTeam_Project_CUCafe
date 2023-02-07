from django.urls import path, include
from .views import main_views
from google_oauth.views import login_views as google_login
from github_oauth.views import login_views as github_login

app_name = 'cafe'

urlpatterns = [
    #main_views.py
    path('', main_views.index, name="main_index"),
    #Google
    path('login/google/', google_login.GoogleOauthLogin.google_login , name="google_login" ),
    path('login/google/callback', google_login.GoogleOauthLogin.google_callback, name="google_callback"),
    #Github
    path('login/github/', github_login.GithubOauthLogin.github_login , name="github_login" ),
    path('login/github/callback', github_login.GithubOauthLogin.github_callback, name="github_callback"),
]