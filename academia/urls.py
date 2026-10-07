from django.urls import path
from . import views

app_name = 'academia'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('clases/', views.clases, name='clases'),
]