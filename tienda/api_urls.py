from rest_framework.routers import DefaultRouter

from .api_views import (
    ClienteViewSet,
    ProductoViewSet,
    VentaViewSet,
)


router = DefaultRouter()

router.register(
    r'clientes',
    ClienteViewSet,
    basename='cliente'
)

router.register(
    r'productos',
    ProductoViewSet,
    basename='producto'
)

router.register(
    r'ventas',
    VentaViewSet,
    basename='venta'
)


urlpatterns = router.urls