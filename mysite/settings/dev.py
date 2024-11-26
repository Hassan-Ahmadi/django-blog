from mysite.settings.base import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config(
    "SECRET_KEY",
    default="django-insecure-19=hbi--*be@@hffo!vjw@r#+^#(j$%lw#z3@14rp$$4g7e7$f",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", cast=bool, default=True)

MAINTENANCE_MODE = False

ALLOWED_HOSTS = ["*"]


# to let djnago know what is the real domain name
# 2 is the id of localhost
SITE_ID = 2

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

STATIC_ROOT = BASE_DIR / "static"
STATICFILES_DIRS = [BASE_DIR / "statics"]


MEDIA_ROOT = BASE_DIR / "media"

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    # other finders..
    "compressor.finders.CompressorFinder",
)

COMPRESS_ENABLED = True  # Enable compression
COMPRESS_OFFLINE = True  # Offline compression
COMPRESS_ROOT = STATIC_ROOT  # Set the path to your static files directory

X_FRAME_OPTIONS = "SAMEORIGIN"
