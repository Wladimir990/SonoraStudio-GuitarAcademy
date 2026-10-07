from django.db import models


class Cliente(models.Model):
    rut = models.CharField(max_length=12, unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.CharField(max_length=200, blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"


class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    categoria = models.CharField(max_length=100)
    marca = models.CharField(max_length=100, blank=True)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    imagen = models.ImageField(
        upload_to='productos/',
        blank=True,
        null=True
    )
    ficha_tecnica = models.FileField(
        upload_to='documentos/',
        blank=True,
        null=True
    )
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Venta(models.Model):
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.PROTECT,
        related_name='ventas'
    )
    producto = models.ForeignKey(
        Producto,
        on_delete=models.PROTECT,
        related_name='ventas',
        blank=True,
        null=True
    )
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    total = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(
        max_length=50,
        default='Completada'
    )

    def __str__(self):
        return f"Venta #{self.id} - {self.cliente}"