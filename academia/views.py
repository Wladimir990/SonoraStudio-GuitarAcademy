import json
import os
from django.shortcuts import render
from django.conf import settings


def inicio(request):
    nombre_academia = "Guitar Academy"
    modalidades = ["Acústica", "Eléctrica"]
    cantidad_modalidades = len(modalidades)

    if cantidad_modalidades > 1:
        mensaje = "Ofrecemos más de una modalidad de guitarra"
    else:
        mensaje = "Ofrecemos una modalidad de guitarra"

    contexto = {
        'nombre_academia': nombre_academia,
        'modalidades': modalidades,
        'mensaje': mensaje,
    }
    return render(request, 'academia/inicio.html', contexto)


def clases(request):
    ruta_json = os.path.join(settings.BASE_DIR, 'academia', 'data', 'clases.json')

    with open(ruta_json, 'r', encoding='utf-8') as archivo:
        lista_clases = json.load(archivo)

    total_clases = len(lista_clases)
    con_cupos = []
    for clase in lista_clases:
        if clase['cupos_disponibles'] > 0:
            con_cupos.append(clase)
    total_con_cupos = len(con_cupos)

    contexto = {
        'clases': lista_clases,
        'total_clases': total_clases,
        'total_con_cupos': total_con_cupos,
    }
    return render(request, 'academia/clases.html', contexto)