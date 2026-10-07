"""
Django settings for sonorastudio project.
"""

from pathlib import Path
import os
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / '.env')


# ============================================================
# SEGURIDAD
# ============================================================

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

DEBUG = os.getenv('DJANGO_DEBUG', 'False').lower() == 'true'

ALLOWED_HOSTS = []


# ============================================================
# APLICACIONES
# ============================================================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # API REST
    'rest_framework',
    'drf_spectacular',

    # Aplicaciones
    'tienda',
    'academia',
]


# ============================================================
# MIDDLEWARE
# ============================================================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'sonorastudio.urls'


# ============================================================
# TEMPLATES
# ============================================================

TEMPLATES = [
    {
        'BACKEND':
            'django.template.backends.django.DjangoTemplates',

        'DIRS': [
            BASE_DIR / 'templates',
        ],

        'APP_DIRS': True,

        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'sonorastudio.wsgi.application'


# ============================================================
# BASE DE DATOS
# ============================================================

DATABASES = {
    'default': {
        'ENGINE':
            'django.db.backends.sqlite3',

        'NAME':
            BASE_DIR / 'db.sqlite3',
    }
}


# ============================================================
# CONTRASEÑAS
# ============================================================

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
            'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME':
            'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
            'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
            'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# ============================================================
# IDIOMA / ZONA HORARIA
# ============================================================

LANGUAGE_CODE = 'es-cl'

TIME_ZONE = 'America/Santiago'

USE_I18N = True

USE_TZ = True


# ============================================================
# STATIC
# ============================================================

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]


# ============================================================
# MEDIA
# ============================================================
#
# IMPORTANTE:
# Tus imágenes y PDF actuales están guardados directamente en:
#
# productos/
# documentos/
#
# Por eso usamos BASE_DIR para conservar los archivos
# existentes sin romper las rutas de la base de datos.
# ============================================================

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR


# ============================================================
# EMAIL
# ============================================================

EMAIL_BACKEND = (
    'django.core.mail.backends.console.EmailBackend'
)


# ============================================================
# REST FRAMEWORK
# ============================================================

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),

    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),

    'DEFAULT_SCHEMA_CLASS':
        'drf_spectacular.openapi.AutoSchema',
}


# ============================================================
# SWAGGER
# ============================================================

SPECTACULAR_SETTINGS = {
    'TITLE': 'SonoraStudio API',

    'DESCRIPTION':
        'API REST para gestión de clientes, productos y ventas.',

    'VERSION': '1.0.0',

    'SERVE_INCLUDE_SCHEMA': False,

    'COMPONENT_SPLIT_REQUEST': True,

    'SECURITY': [
        {
            'BearerAuth': []
        }
    ],

    'APPEND_COMPONENTS': {
        'securitySchemes': {
            'BearerAuth': {
                'type': 'http',
                'scheme': 'bearer',
                'bearerFormat': 'JWT',
            }
        }
    },
}


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'