# DjangoChatbot/urls.py

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
from chat.views import redirect_to_chat  # Assuming you have this for post-login redirection

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(template_name='registration/login.html'), name='root'),  # Using Django's LoginView for the root
    path('chat/', include(('chat.urls', 'chat'))),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),  # Using Django's LoginView
]
