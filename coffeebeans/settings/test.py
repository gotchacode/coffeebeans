from .base import *


DEBUG = True
TEMPLATE_DEBUG = DEBUG

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

AWS_STORAGE_BUCKET_NAME = 'assets.coffeebeans.nl'

MEDIA_URL = 'http://assets.coffeebeans.nl.s3-website-eu-west-1.amazonaws.com/'