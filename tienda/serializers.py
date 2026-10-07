from rest_framework import serializers
from .models import Cliente, Producto, Venta


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = [
            'id',
            'rut',
            'nombres',
            'apellidos',
            'email',
            'telefono',
            'direccion',
            'fecha_registro',
            'activo',
        ]
        read_only_fields = [
            'id',
            'fecha_registro',
        ]


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = [
            'id',
            'nombre',
            'categoria',
            'marca',
            'descripcion',
            'precio',
            'stock',
            'imagen',
            'ficha_tecnica',
            'activo',
            'fecha_creacion',
        ]
        read_only_fields = [
            'id',
            'fecha_creacion',
        ]


class VentaSerializer(serializers.ModelSerializer):
    cliente_nombre = serializers.CharField(
        source='cliente.__str__',
        read_only=True
    )

    producto_nombre = serializers.CharField(
        source='producto.nombre',
        read_only=True
    )

    class Meta:
        model = Venta
        fields = [
            'id',
            'cliente',
            'cliente_nombre',
            'producto',
            'producto_nombre',
            'cantidad',
            'precio_unitario',
            'total',
            'fecha',
            'estado',
        ]
        read_only_fields = [
            'id',
            'fecha',
        ]