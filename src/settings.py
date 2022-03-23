"""
Django settings for src project.

Generated by 'django-admin startproject' using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2_+0cn0tm8)h+fwrk#prvw@#vvqb!no)@%d=fto8i-4_&h+^5g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'accounts',
    'storages',
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

ROOT_URLCONF = 'src.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'src.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
# 'default': {
# 'ENGINE': 'django.db.backends.mysql',
# 'NAME': 'instance_sizing_pricing_demo',
# 'HOST': 'database.ctedujo1muxe.eu-west-1.rds.amazonaws.com',
# 'USER': 'admin',
# 'PASSWORD': 'Admin123',
# 'PORT': '3306'
#     }
# }


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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')


#SES SMTP

# # EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_BACKEND = 'django_ses.SESBackend'
# AWS_ACCESS_KEY_ID = 'AKIAXE6NLMXXNOQQWPV7'
# AWS_SECRET_ACCESS_KEY = 'BFpUOa//9xtZguQYrw5jb/hxDl1HZmXC0KZPBtfYG2rd'
# EMAIL_HOST = 'email-smtp.us-west-2.amazonaws.com'
# EMAIL_PORT = 587 
# # EMAIL_HOST_USER = 'AKIAXE6NLMXXNOQQWPV7'
# # EMAIL_PASSWORD = 'BFpUOa//9xtZguQYrw5jb/hxDl1HZmXC0KZPBtfYG2rd'
# EMAIL_USE_TLS = True

# new smtp
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_BACKEND = 'django_ses.SESBackend'
# AWS_ACCESS_KEY_ID = 'AKIAXE6NLMXXNOQQWPV7'
# AWS_SECRET_ACCESS_KEY = 'BFpUOa//9xtZguQYrw5jb/hxDl1HZmXC0KZPBtfYG2rd'
# AWS_SES_REGION_NAME = 'us-west-2' #(ex: us-east-2)
# AWS_SES_REGION_ENDPOINT ='email-smtp.us-west-2.amazonaws.com' #(ex: email.us-east-2.amazonaws.com)

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'galibcodincity@gmail.com'
EMAIL_HOST_PASSWORD = 'Cry@#Code81624'

#S3 BUCKETS CONFIG
AWS_ACCESS_KEY_ID = 'AKIAXE6NLMXXBQO74UGX'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'instance-sizing-pricing-demo'
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'




# [Unit]
# Description=gunicorn daemon
# Requires=gunicorn.socket
# After=network.target

# [Service]
# User=ubuntu
# Group=www-data
# WorkingDirectory=/home/ubuntu/project/instanceapp
# ExecStart=/home/ubuntu/project/myprojectenv/bin/gunicorn \
#           --access-logfile - \
#           --workers 3 \
#           --bind unix:/run/gunicorn.sock \
#           src.wsgi:application

# [Install]
# WantedBy=multi-user.target

# server {
#     listen 80;
#     server_name 54.78.143.11;

#     location = /favicon.ico { access_log off; log_not_found off; }
    
#     location / {
#         include proxy_params;
#         proxy_pass http://unix:/run/gunicorn.sock;
#     }
# }



# [Unit]
# Description=gunicorn daemon
# Requires=gunicorn.socket
# After=network.target

# [Service]
# User=ubuntu
# Group=www-data
# WorkingDirectory=/home/ubuntu/project/instanceapp
# ExecStart=/home/ubuntu/.local/bin/gunicorn \
#           --access-logfile - \
#           --workers 3 \
#           --bind unix:/run/gunicorn.sock \
#           src.wsgi:application

# [Install]
# WantedBy=multi-user.target