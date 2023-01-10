from django.shortcuts import render, redirect

# Create your views here.

def mv_user_board(request):
    return redirect(request, '/board')