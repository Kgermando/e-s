"""
Django settings for es project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+f5fyu0r#w*n%$0mueny8x$jj#qk!dxwpk4v@e_1c&le3f&hr@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False    

ALLOWED_HOSTS = ['entrepreneuriat-solutions.com', 'www.entrepreneuriat-solutions.com', '138.197.210.173', '*']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    

    'tinymce',
    # 'newsletter',
    'rest_framework',
    'storages',
    # 'corsheaders',
    'google_analytics',

    'handlers',
    'app',
    'accounts',
    'documentations',
    'produits',
    'partenaires',
    'solutions',
    'dashboard',
]

SITE_ID = 1

CORS_ORIGIN_ALLOW_ALL = True

GOOGLE_ANALYTICS = {
    'google_analytics_id': 'G-4JCJ538Q72',
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'es.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'es.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

if DEBUG == True:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'es',
            'USER': 'es',
            'PASSWORD': 'gk0813530838',
            'HOST': 'localhost',
            'PORT': '',
        }
    }


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Kinshasa'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# config/settings.py
# DEFAULT_FROM_EMAIL = 'contact@entrepreneuriatsolutions.com'
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'mail.gandi.net'
# EMAIL_USE_TLS = True
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'contact@entrepreneuriatsolutions.com'
# EMAIL_HOST_PASSWORD = 'derick@1234'

# newsletter
NEWSLETTER_CONFIRM_EMAIL = False

# Using django-tinymce
TINYMCE_JS_URL = 'https://cdn.tiny.cloud/1/9uefa29mghxxv68ohq2qhnr7wz86r3mxche6tiotda03zpj0/tinymce/4/tinymce.min.js'
TINYMCE_COMPRESSOR = False
NEWSLETTER_RICHTEXT_WIDGET = "tinymce.widgets.TinyMCE"


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

if DEBUG == True:
    STATIC_URL = '/static/'

    STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
    STATIC_ROOT = os.path.join(BASE_DIR, "static-root")

    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media-root')

else:
    AWS_ACCESS_KEY_ID = 'HKW7WII6TR2PEA2RQN62'
    AWS_SECRET_ACCESS_KEY = '4fPeOoS4DAa9crC+rdG/mk6LGkIh1QjNxh6Eog1HWRg'
    AWS_STORAGE_BUCKET_NAME = 'entrepreneuriat-solutions'
    AWS_S3_ENDPOINT_URL = 'https://nyc3.digitaloceanspaces.com'
    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400',
    }
    AWS_LOCATION = 'entrepreneuriat-solutions-static'

    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static'),
    ]
    STATIC_URL = 'https://%s/%s/' % (AWS_S3_ENDPOINT_URL, AWS_LOCATION)
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'



# REST 
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}
