from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'fintrack',
        'USER': 'postgres',
        'PASSWORD': '922933',
        'HOST': 'localhost'
    }
}

OPEN_EXCHANGE_RATES_APP_ID = '3dce0b4e6fba47f5a2de000e38556619'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kh!mn=3e(g94%4f$)47t4(ctq_*#=wuhtd0+4@d_@x4&a71fci'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


