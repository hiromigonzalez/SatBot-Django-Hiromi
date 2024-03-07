# chat/views.py

from django.shortcuts import render, redirect

def chat_home(request):
    return render(request, 'chat/chatbot.html')

def redirect_to_chat(request):
    return redirect('chat/')

def login_view(request):
    return render(request, 'chat/login.html')