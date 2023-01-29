from django.shortcuts import render, redirect

def index(request):
    render(request, 'cafe/main_screen.html')