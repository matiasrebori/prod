
"""
Todas las URLS de la APP login

"""

from django.urls import path

from.import views

urlpatterns = [
    path('', views.login, name='login'),
]