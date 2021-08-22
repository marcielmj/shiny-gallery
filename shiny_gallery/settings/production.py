from os import getenv
from secrets import token_urlsafe

from dj_database_url import config

from .base import *


SECRET_KEY = getenv("SECRET_KEY", token_urlsafe(50))

DEBUG = False

ALLOWED_HOSTS = ("*",)

ADMINS = (("Marciel Sousa", "marcielmj@gmail.com"),)


SECURE_HSTS_INCLUDE_SUBDOMAINS = True

SECURE_HSTS_PRELOAD = True

SECURE_HSTS_SECONDS = 60

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

db_from_env = config("DATABASE_URL", conn_max_age=600, ssl_require=True)
DATABASES["default"].update(db_from_env)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_ROOT.mkdir(exist_ok=True)

DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

STATICFILES_STORAGE = "storages.backends.s3boto3.S3ManifestStaticStorage"


AWS_ACCESS_KEY_ID = getenv("AWS_ACCESS_KEY_ID")

AWS_SECRET_ACCESS_KEY = getenv("AWS_SECRET_ACCESS_KEY")

AWS_STORAGE_BUCKET_NAME = getenv("AWS_STORAGE_BUCKET_NAME")


THUMBNAIL_DEFAULT_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
