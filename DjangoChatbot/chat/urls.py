# chat/urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.chat_home, name='chat_home'),
    path('login/', views.login_view, name='login'),
]

STATIC_URL = '/static/'

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
