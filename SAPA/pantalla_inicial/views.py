"""
pantalla_inicial/views.py
======================================================
Simples Views para probar la funcionalidad de esta app
"""

from django.http import HttpResponse
from django.shortcuts import render

def saludo(request):
    """Retorna un saludo de bienvenida si el usuario logró iniciar sesión

    Args:
        request: request del usuario

    Returns:
        Un  saludo, incluyendo su nombre si es que está logueado
    """

    return HttpResponse('Bienvenido ' + str(request.user.username) + '. Sesión iniciada correctamente')


def para_pytest(request=''):
    """Utilizado sólo para ver el comportamiento del pytest

    Args:
        request: no utilizado

    Returns:
        True
    """
    return True


def dashboard(request):
    """Retorna la pantalla inicial una vez iniciada la sesión

    Returns:
        Devuelve el dashboard
    """

    return render(request, "dashboard.html", {'user': request.user})


def devuelve_todo(request, pagina):
    """Retorna cualquier html solicitado en esta app

        Returns:
            Devuelve el html pasado como parámetro
    """

    return render(request, pagina, {'user': request.user})
