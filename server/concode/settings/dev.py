from concode.settings.base import *

DEBUG = True
ALLOWED_HOSTS = []
SECRET_KEY = 'secret_b8)-gp*_!t7seu#np%o7#5%l$&trc=jp2xt%am+%xo@42$pdo_'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
