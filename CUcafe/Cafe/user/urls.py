from django.urls import path
from . import views

urlpatterns = [
    path('signup',views.signup),
    path('signup',views.login),
    path('signup',views.logout),
    
]