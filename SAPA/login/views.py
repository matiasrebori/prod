"""
login/views.py
======================================================
Simples Views para probar la funcionalidad de esta app
"""

from django.shortcuts import render
from django.shortcuts import redirect
# Create your views here.



def login(request):

    """Si el usuario no esta logeado renderea la pantalla de inicio de sesion, si el usuario ya esta logeado lo redirecciona al dashboard
	https://docs.djangoproject.com/en/3.2/topics/auth/default/#authentication-in-web-requests
	https://docs.djangoproject.com/en/3.2/topics/http/shortcuts/#examples
    Args:
        request: request del usuario

    Returns:
        redirect
    """
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    else:
        return render(request,"login-template.html")