"""
Django settings for hookupdesign project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'lz@7$^!s2(%@yx+)2kv-&f!t$qs1p=g0bp(+l7()g2tm2i4u5t'
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

INTERNAL_IPS = ("127.0.0.1", )
ALLOWED_HOSTS = ["fierce-savannah-6613.herokuapp.com", ]

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'twitter_bootstrap',
    'designweb',
    'rest_framework',
    'django_crontab',
    'storages',
)

# 12-30-2014 add for admin utility
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages"
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'hookupdesign.urls'

WSGI_APPLICATION = 'hookupdesign.wsgi.application'

if os.path.exists("/Users/zys"):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        },
    }
else:
    import dj_database_url
    DATABASES = {
        'default': dj_database_url.parse(
            'postgres://rluxmcyaxgesgz:LRqb2dNv1dKEtzy4aTB3o99h3q@ec2-50-19-249-214.compute-1.amazonaws.com:5432/d35kgnmou4uo7g')
    }

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# AWS S3 setup
USE_S3 = True
AWS_ACCESS_KEY = 'AKIAJAZ5UY6AQL3BLMWA'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'popdesign'
AWS_QUERYSTRING_AUTH = False
S3_STORAGE = 'https://%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
S3_URL = 'http://127.0.0.1:8000'   # initial with local for testing
IS_TEST = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
# STATIC_ROOT = os.path.join(BASE_DIR, '/static/')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

if USE_S3:
    S3_URL = S3_STORAGE
    if IS_TEST:
        S3_URL = S3_STORAGE + '/test'
    MEDIA_URL = S3_URL + '/products/'
    MEDIA_ROOT = S3_URL

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    MEDIA_ROOT,
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'designweb/../templates'),
)

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),
    'PAGINATE_BY': 15,
}

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'yansongzhang10101@gmail.com'
EMAIL_HOST_PASSWORD = 'popdesign1dots'
EMAIL_USE_TLS = True

CRONJOBS = [
    ('*/1 * * * *', 'designweb.management.commands.group_mail_schedule.testing_call', '> /tmp/last_scheduled_job.log'),
]

# Paypal api section
PAYMENT_SANDBOX = {
    'mode': 'sandbox',  # sandbox or live
    'client_id': 'AbQpRdq8rpVgUkfWBv7ItV7kbmhNizliedoHoj1BbKijMUZuJyVtYgyHVEiDHWLGYubYflq1v8JVl-6m',
    'client_secret': 'EIJs4rr71GXFI4gjEsQYLCIpXSbiXnKg2huwIfRpicsDcD7xSYa-y5_lSR5oTY3e0F_5PsDkYD-k-KK-',
}


# Memcache set up
def get_cache():
    try:
        os.environ['MEMCACHE_SERVERS'] = os.environ['mc5.dev.ec2.memcachier.com:11211'].replace(',', ';')
        os.environ['MEMCACHE_USERNAME'] = os.environ['4cdff9']
        os.environ['MEMCACHE_PASSWORD'] = os.environ['696829c4d1']
        return {
            'default': {
                'BACKEND': 'django_pylibmc.memcached.PyLibMCCache',
                'TIMEOUT': 500,
                'BINARY': True,
                'OPTIONS': {'tcp_nodelay': True }
            }
        }
    except:
        return {
            'default': {
                'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'
            }
        }

CACHES = get_cache()