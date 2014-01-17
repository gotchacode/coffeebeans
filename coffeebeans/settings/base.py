# Django base settings for coffeebeans project.

import os
import dj_database_url
from socialschools_cms.base_settings import *


PROJECT_ROOT = os.sep.join(os.path.abspath(os.path.dirname(__file__))\
                     .split(os.sep)[:-2])

APP_ROOT = os.sep.join(os.path.abspath(os.path.dirname(__file__))\
                     .split(os.sep)[:-1])

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Support', 'support@socialschools.nl'),
)

MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Amsterdam'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'nl'

LANGUAGES = (
        ('nl', 'Dutch'),
)

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
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(os.environ.get("WWW_DIR", PROJECT_ROOT), "media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(os.environ.get("WWW_DIR", PROJECT_ROOT), "static")

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(APP_ROOT, "static"),
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'c7zcndtp+(q!fwm*s@hu&(k(2d(x%sd2$6($_(zoq*koji+!c_'

# List of callables that know how to import templates from various sources.

ROOT_URLCONF = 'coffeebeans.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'coffeebeans.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(APP_ROOT, "templates"),
)

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(APP_ROOT, "static"),
)


TEMPLATE_DIRS = (
    os.path.join(APP_ROOT, "templates"),
)

CSS_LOGIN_URL = 'http://coffeebeans.socialschools.nl'

