from django.urls import path, include
from .views import main_views, login_views


app_name = 'cafe'

urlpatterns = [
    #main_views.py
    path('', main_views.index, name="main_index")
    #login_views.py
    
]