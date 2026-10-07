from django import forms
from .models import Producto, Cliente


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'nombre',
            'categoria',
            'marca',
            'descripcion',
            'precio',
            'stock',
            'imagen',
            'ficha_tecnica',
            'activo',
        ]


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'rut',
            'nombres',
            'apellidos',
            'email',
            'telefono',
            'direccion',
            'activo',
        ]