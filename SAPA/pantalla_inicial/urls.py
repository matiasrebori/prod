from django.urls import path
from pantalla_inicial.views import dashboard, devuelve_todo
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('dashboard/', dashboard),
    path('dashboard/<str:pagina>', devuelve_todo),
    path('logout', LogoutView.as_view()),

]
