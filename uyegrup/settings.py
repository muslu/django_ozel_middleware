# -*- coding: utf-8 -*-
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(qpp@a@imtf3vq0%@p1kf&5t++tb(vi0h$(-#58-!xu7e)y9p6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1',]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'uyeler', 'kayit'
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'uyeler.ozel_islemler.IPKontrolMiddleware'
]

ROOT_URLCONF = 'uyegrup.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'uyegrup.wsgi.application'


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


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

# MEDIA_ROOT                                      =       BASE_DIR + '/media/'
# MEDIA_URL                                       =       '/media/'

# STATIC_ROOT                                     =       BASE_DIR + "/static/"
STATIC_URL                                      =       '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]


# ADMIN_MEDIA_PREFIX                              =       '/media/admin/'

# STATICFILES_FINDERS                             =       ('django.contrib.staticfiles.finders.AppDirectoriesFinder', 'django.contrib.staticfiles.finders.FileSystemFinder',)
ADMINS                                          =       (('Muslu', 'musluyuksektepe@gmail.com'),)

LANGUAGE_CODE                                   =       'tr_TR'
TIME_ZONE                                       =       'Europe/Istanbul'
USE_I18N                                        =       True
USE_L10N                                        =       False
USE_TZ                                          =       False