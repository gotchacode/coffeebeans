import os
import dj_database_url
import urlparse

PROJECT_ROOT = os.sep.join(os.path.abspath(os.path.dirname(__file__))\
                     .split(os.sep)[:-2])

APP_ROOT = os.sep.join(os.path.abspath(os.path.dirname(__file__))\
                     .split(os.sep)[:-1])


APP_VERSION = __version__

ADMINS = (
    ('Admin', 'vinit.kumar@changer.nl'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL', 'postgres://localhost/coffeebeans'))
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Amsterdam'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join(os.environ.get("WWW_DIR", PROJECT_ROOT), "media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL =  '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(os.environ.get("WWW_DIR", PROJECT_ROOT), "static", APP_VERSION)

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = "/static/%s/" % APP_VERSION

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(APP_ROOT, "static"),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.transaction.TransactionMiddleware',

    'socialschools.apps.multitenant.middleware.TenantResolver',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'coffeebeans.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'coffeebeans.wsgi.application'

LOCALE_PATHS = (
    os.path.join(APP_ROOT, "locale"),
)


TEMPLATE_DIRS = (
    os.path.join(APP_ROOT, "templates"),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',

    'mptt',
    'storages',
    'easy_thumbnails',

    'djangosaml2',
    'south',
)

BROKER_URL = 'django://'

import djcelery
djcelery.setup_loader()

AUTH_USER_MODEL = 'profiles.UserProfile'


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue'
        }

    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True
        },
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'djangosaml2' : {
            'handlers': ['console'],
            'level': 'DEBUG',
        }
    }
}

ACCOUNT_ACTIVATION_DAYS = 7
DEFAULT_FROM_EMAIL = 'no-reply@socialschools.nl'

TESTING = False

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/accounts/login'
LOGOUT_URL = '/accounts/logout'

SESSION_EXPIRE_AT_BROWSER_CLOSE = True


EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = os.environ.get('SENDGRID_USERNAME')
EMAIL_HOST_PASSWORD = os.environ.get('SENDGRID_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True


CSS_POSTS_PAGINATION = 8
CSS_PUBLIC_POSTS = 10

CSS_MAX_PHOTO_SIZE = 1000, 750

CSS_APPDOMAIN_SUFFIX = 'socialschools.nl'

DEFAULT_AUTHENTICATION_BACKEND = 'django.contrib.auth.backends.ModelBackend'
SAML_AUTHENTICATION_BACKEND = 'djangosaml2.backends.Saml2Backend'
GOOGLE_AUTHENTICATION_BACKEND = 'social.backends.google.GoogleOpenId'

AUTHENTICATION_BACKENDS = (GOOGLE_AUTHENTICATION_BACKEND, DEFAULT_AUTHENTICATION_BACKEND, SAML_AUTHENTICATION_BACKEND,)

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.social_auth.associate_by_email',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details'
)



DEFAULT_FILE_STORAGE = 'socialschools.settings.s3storage.MediaS3BotoStorage'
STATICFILES_STORAGE = 'socialschools.settings.s3storage.StaticS3BotoStorage'

AWS_S3_SECURE_URLS = False
AWS_LOCATION = 'media/'
S3_MAX_FILESIZE = 8388608 # 8 megbytes
S3_POLICY_EXPIRATION = 200000

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY =os.environ.get('AWS_SECRET_ACCESS_KEY')

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONPRenderer',
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
        'socialschools.generic.views.JSONHTMLRenderer',
    ),
        'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'PAGINATE_BY': 10,
    'FILTER_BACKEND': 'rest_framework.filters.DjangoFilterBackend',
    'UNAUTHENTICATED_USER': 'socialschools.apps.profiles.AnonymousUserProfile',
}

THUMBNAIL_DEFAULT_STORAGE = 'socialschools.settings.s3storage.MediaS3BotoStorage'
THUMBNAIL_PRESERVE_EXTENSIONS = True

THUMBNAIL_BASEDIR = 'thumbnail'
THUMBNAIL_DUMMY_PROCESSING = STATIC_URL + 'socialschools/img/thumbnail_in_progress.png'
THUMBNAIL_GRAVATAR = STATIC_URL + 'socialschools/img/avatar.png'
THUMBNAIL_GROUP_GRAVATAR = STATIC_URL + 'socialschools/img/group_avatar.png'

THUMBNAIL_ALIASES = {
    '': {
        'small': {'size': (140, 140), 'crop': True},
    },
}

ugettext = lambda s: s

LANGUAGES = (
  ('en', ugettext('English')),
  ('nl', ugettext('Dutch')),
)

FORMAT_MODULE_PATH = 'socialschools.formats'

redis_url = urlparse.urlparse(os.environ.get('REDISTOGO_URL', 'redis://localhost:6379'))

CACHES = {
    "default": {
        "BACKEND": "redis_cache.cache.RedisCache",
        # location scheme seems to be hostname:port:dbnumber
        'LOCATION': '%s:%s:0' % (redis_url.hostname, redis_url.port),
        "OPTIONS": {
            "CLIENT_CLASS": "redis_cache.client.DefaultClient",
            'PASSWORD': redis_url.password,
        }
    }
}

NOTIFICATION_READ_DEFAULT_REDIRECT = 'dashboard:home'

PARSE_APPLICATION_ID = os.environ.get('PARSE_APPLICATION_ID')
PARSE_REST_API_KEY = os.environ.get('PARSE_REST_API_KEY')
PARSE_PUSH_URL = 'https://api.parse.com/1/push'