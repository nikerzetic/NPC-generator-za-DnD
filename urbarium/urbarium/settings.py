"""
Django settings for urbarium project.
Generated by 'django-admin startproject' using Django 3.0.4.
For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

FORCE_SCRIPT_NAME = os.environ.get('DJANGO_URL', None)
DB_PORT = os.environ.get('POSTGRES_PORT', 5432)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'k3uo#rq82ppb^4bc_x%j@p#wvpr95)ct_&1!(ig!_qv1y$c78k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'character.apps.CharacterConfig',
    'settlement.apps.SettlementConfig',
    'political_formation.apps.PoliticalFormationConfig',
    'governing_body.apps.GoverningBodyConfig',
    'title.apps.TitleConfig',
    'users.apps.UsersConfig',
    'crispy_forms',
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

ROOT_URLCONF = 'urbarium.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),],
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

WSGI_APPLICATION = 'urbarium.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# PostgreSQL
if os.path.isfile('user-credentials.txt'):
    with open('user-credentials.txt', 'r') as file:
        username, password = file.readline().split(',')
else:
    with open('public-credentials.txt', 'r') as file:
        username, password = file.readline().split(',')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'NAME': 'sem2020_nike',
        'USER': username,
        'PASSWORD': password,
        'HOST': 'baza.fmf.uni-lj.si',
        'PORT': DB_PORT,
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Ljubljana'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

if FORCE_SCRIPT_NAME:
    STATIC_URL = FORCE_SCRIPT_NAME + 'static/'
    LOGIN_REDIRECT_URL = FORCE_SCRIPT_NAME + 'user/profile'
    LOGOUT_REDIRECT_URL = FORCE_SCRIPT_NAME + 'user/logout'
else:
    STATIC_URL = 'static/'
    LOGIN_REDIRECT_URL = '/user/profile'
    LOGOUT_REDIRECT_URL = '/user/logout'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]

CRISPY_TEMPLATE_PACK = 'bootstrap4'
