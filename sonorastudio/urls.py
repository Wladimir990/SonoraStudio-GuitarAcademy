from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import logout
from django.shortcuts import redirect

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)


# ============================================================
# LOGOUT PERSONALIZADO
# ============================================================

def cerrar_sesion(request):
    logout(request)
    return redirect('/admin/login/')


# ============================================================
# URLS
# ============================================================

urlpatterns = [

    # LOGOUT PERSONALIZADO
    # Debe ir ANTES que admin.site.urls
    path(
        'admin/logout/',
        cerrar_sesion,
        name='cerrar_sesion'
    ),

    # ADMIN
    path(
        'admin/',
        admin.site.urls
    ),

    # TIENDA
    path(
        'tienda/',
        include('tienda.urls')
    ),

    # ACADEMIA
    path(
        'academia/',
        include('academia.urls')
    ),

    # API REST
    path(
        'api/',
        include('tienda.api_urls')
    ),

    # JWT
    path(
        'api/token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),

    path(
        'api/token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),

    # OPENAPI
    path(
        'api/schema/',
        SpectacularAPIView.as_view(),
        name='schema'
    ),

    # SWAGGER
    path(
        'api/docs/',
        SpectacularSwaggerView.as_view(
            url_name='schema'
        ),
        name='swagger-ui'
    ),
]


# ============================================================
# MEDIA
# ============================================================

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )