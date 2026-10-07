from django.shortcuts import render, get_object_or_404, redirect

from .models import Producto, Cliente, Venta
from .forms import ProductoForm, ClienteForm


# ============================================================
# INICIO
# ============================================================

def inicio(request):
    nombre_tienda = "SonoraStudio"
    eslogan = "Todo el sonido que necesitas, en un solo lugar"
    anio_fundacion = 2015
    anio_actual = 2026
    anios_trayectoria = anio_actual - anio_fundacion

    contexto = {
        'nombre_tienda': nombre_tienda,
        'eslogan': eslogan,
        'anios_trayectoria': anios_trayectoria,
    }

    return render(
        request,
        'tienda/inicio.html',
        contexto
    )


# ============================================================
# CATÁLOGO
# ============================================================

def catalogo(request):
    productos = Producto.objects.all()

    total_productos = productos.count()

    disponibles = productos.filter(
        activo=True,
        stock__gt=0
    )

    total_disponibles = disponibles.count()

    contexto = {
        'productos': productos,
        'total_productos': total_productos,
        'total_disponibles': total_disponibles,
    }

    return render(
        request,
        'tienda/catalogo.html',
        contexto
    )


# ============================================================
# CRUD PRODUCTO
# ============================================================

def producto_lista(request):
    productos = Producto.objects.all()

    return render(
        request,
        'tienda/producto_lista.html',
        {
            'productos': productos
        }
    )


def producto_crear(request):
    if request.method == 'POST':

        form = ProductoForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            producto = form.save()

            return redirect(
                'tienda:producto_detalle',
                pk=producto.pk
            )

    else:
        form = ProductoForm()

    return render(
        request,
        'tienda/producto_form.html',
        {
            'form': form,
            'titulo': 'Nuevo producto'
        }
    )


def producto_detalle(request, pk):
    producto = get_object_or_404(
        Producto,
        pk=pk
    )

    return render(
        request,
        'tienda/producto_detalle.html',
        {
            'producto': producto
        }
    )


def producto_editar(request, pk):
    producto = get_object_or_404(
        Producto,
        pk=pk
    )

    if request.method == 'POST':

        form = ProductoForm(
            request.POST,
            request.FILES,
            instance=producto
        )

        if form.is_valid():
            producto = form.save()

            return redirect(
                'tienda:producto_detalle',
                pk=producto.pk
            )

    else:
        form = ProductoForm(
            instance=producto
        )

    return render(
        request,
        'tienda/producto_form.html',
        {
            'form': form,
            'producto': producto,
            'titulo': 'Editar producto'
        }
    )


def producto_eliminar(request, pk):
    producto = get_object_or_404(
        Producto,
        pk=pk
    )

    if request.method == 'POST':
        producto.delete()

        return redirect(
            'tienda:producto_lista'
        )

    return render(
        request,
        'tienda/producto_eliminar.html',
        {
            'producto': producto
        }
    )


# ============================================================
# CRUD CLIENTE
# ============================================================

def cliente_lista(request):
    clientes = Cliente.objects.all()

    return render(
        request,
        'tienda/cliente_lista.html',
        {
            'clientes': clientes
        }
    )


def cliente_crear(request):
    if request.method == 'POST':

        form = ClienteForm(
            request.POST
        )

        if form.is_valid():
            cliente = form.save()

            return redirect(
                'tienda:cliente_detalle',
                pk=cliente.pk
            )

    else:
        form = ClienteForm()

    return render(
        request,
        'tienda/cliente_form.html',
        {
            'form': form,
            'titulo': 'Nuevo cliente'
        }
    )


def cliente_detalle(request, pk):
    cliente = get_object_or_404(
        Cliente,
        pk=pk
    )

    return render(
        request,
        'tienda/cliente_detalle.html',
        {
            'cliente': cliente
        }
    )


def cliente_editar(request, pk):
    cliente = get_object_or_404(
        Cliente,
        pk=pk
    )

    if request.method == 'POST':

        form = ClienteForm(
            request.POST,
            instance=cliente
        )

        if form.is_valid():
            cliente = form.save()

            return redirect(
                'tienda:cliente_detalle',
                pk=cliente.pk
            )

    else:
        form = ClienteForm(
            instance=cliente
        )

    return render(
        request,
        'tienda/cliente_form.html',
        {
            'form': form,
            'cliente': cliente,
            'titulo': 'Editar cliente'
        }
    )


def cliente_eliminar(request, pk):
    cliente = get_object_or_404(
        Cliente,
        pk=pk
    )

    if request.method == 'POST':
        cliente.delete()

        return redirect(
            'tienda:cliente_lista'
        )

    return render(
        request,
        'tienda/cliente_eliminar.html',
        {
            'cliente': cliente
        }
    )