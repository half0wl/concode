import os
import dj_database_url

from concode.settings.base import *


DEBUG = False
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
ALLOWED_HOSTS = ['concode-api.herokuapp.com']
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

# Disable DRF's browsable API
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}

# CORS
CORS_ORIGIN_WHITELIST = (
    'concode-api.herokuapp.com',
    'concode.herokuapp.com',
    'localhost:8000',
    '127.0.0.1:8000'
)
