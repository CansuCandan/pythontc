# -*- coding: utf-8 -*-

import logging
import os
import sys


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG                   = True
APPEND_SLASH            = True

INSTALLED_APPS          =   [
                            'django.contrib.admin',
                            'django.contrib.auth',
                            'django.contrib.contenttypes',
                            'django.contrib.sessions',
                            'django.contrib.messages',
                            'django.contrib.staticfiles',
                            'blog', 'kullanicilar'
                            ]

MIDDLEWARE              =   [
                                'django.middleware.security.SecurityMiddleware',
                                'django.contrib.sessions.middleware.SessionMiddleware',
                                'django.middleware.common.CommonMiddleware',
                                'django.middleware.csrf.CsrfViewMiddleware',
                                'django.contrib.auth.middleware.AuthenticationMiddleware',
                                'django.contrib.messages.middleware.MessageMiddleware',
                            ]

TEMPLATES               =   [
                                {
                                    'BACKEND': 'django.template.backends.django.DjangoTemplates',
                                    'DIRS': [BASE_DIR + "/templates"],
                                    'APP_DIRS': True,
                                    'OPTIONS': {
                                        'debug': DEBUG,
                                        'context_processors': [
                                            "django.contrib.auth.context_processors.auth",
                                            "django.template.context_processors.debug",
                                            "django.template.context_processors.i18n",
                                            "django.template.context_processors.media",
                                            "django.template.context_processors.static",
                                            "django.template.context_processors.request",
                                        ],
                                    },
                                },
                            ]


DATABASES               =   {
                                'default': {
                                    'NAME': 'pythontcDB',
                                    'ENGINE': 'django.db.backends.mysql',
                                    'USER': 'root',
                                    'PASSWORD': 'R2dxkf22',
                                    'HOST': 'localhost',
                                    'PORT': '3309',
                                },
                            }

ALLOWED_HOSTS           = ["pythontc.katoptrik.com", ]
ADMINS                  = (('Muslu', 'muslu.yuksektepe@makdos.com'),)
MANAGERS                = ADMINS
LANGUAGE_CODE           = 'tr_TR'
TIME_ZONE               = 'Europe/Istanbul'
USE_I18N                = True
USE_L10N                = False
USE_TZ                  = False
WSGI_APPLICATION        = 'pythontc.wsgi.application'

STATIC_URL              = '/static/'
# STATIC_ROOT                                     =       BASE_DIR + "/static/"
STATICFILES_DIRS        = (os.path.join(BASE_DIR, "static"),)

SECRET_KEY              = '9=y%o0io74up&jd_!qq_1f=6))asu$j5#h8iasdasdasascdasda6&sx2tep7tejt)'
ROOT_URLCONF            = 'pythontc.urls'

logging.basicConfig(level=logging.INFO, format='%(message)s', filename='/home/muslu/django/djangoLog.log', )
LOGGING                 =   {
                                'version': 1,
                                'disable_existing_loggers': False,
                                'handlers': {
                                    'log_to_stdout': {
                                        'level': 'DEBUG',
                                        'class': 'logging.StreamHandler',
                                        'stream': sys.stdout,
                                    },
                                },
                                'loggers': {
                                    'main': {
                                        'handlers': ['log_to_stdout'],
                                        'level': 'DEBUG',
                                        'propagate': True,
                                    }
                                }
                            }
