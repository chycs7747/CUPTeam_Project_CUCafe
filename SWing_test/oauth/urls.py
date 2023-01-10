from django.urls import path

from . import views

app_name = 'oauth'

urlpatterns = [
    path('', views.HtmlView.index, name = 'index'),
    #path('login', views.AuthManager.user_login, name = 'login'),
    #path('signup', views.AuthManager.user_signup, name = 'signup'),
    path('login/google/', views.OauthLogin.google_login, name='google-login'),
    path('login/google/callback/', views.OauthLogin.google_callback, name='google-callback'),
    path('success/', views.HtmlView.success, name = 'success'),
]