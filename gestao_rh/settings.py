import os
from decouple import config
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECRET_KEY = config('SECRET_KEY')
SECRET_KEY = 'qkai@zi3%&g(17x9zl81ewldm!tw3o0jb=98(v2%1me#e#d0wm'
DEBUG = config('DEBUG', default=False, cast=bool)
# DEBUG = True

ALLOWED_HOSTS = [
    '18.217.224.82',
    '127.0.0.1',
    '0.0.0.0'
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.empresas',
    'apps.colaboradores',
    'apps.departamentos',
    'apps.documentos',
    'apps.registro_hora_extra',
    'apps.core',
    'bootstrapform',
    'rest_framework',
    'rest_framework.authtoken',
    'drf_yasg',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'gestao_rh.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'gestao_rh.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Manaus'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "staticfiles"),
]

STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, "media")


# if DEBUG:
#         STATICFILES_DIRS = [
#             os.path.join(BASE_DIR, 'staticfiles'),
#        ]
# else:
#     STATIC_ROOT = os.path.join(BASE_DIR, 'static')

LOGIN_REDIRECT_URL = 'home'

LOGOUT_REDIRECT_URL = 'login'

# AUTHENTICATION_BACKENDS = ('apps.backends.CaseInsensitiveModelBackend', )
