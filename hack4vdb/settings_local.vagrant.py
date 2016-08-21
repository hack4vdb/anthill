SECRET_KEY = 'asd'
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'anthill',
        'USER': 'anthill',
        'PASSWORD': 'vander',
    }
}

EMAIL_HOST = '127.0.0.1'
EMAIL_HOST_USER = 'vagrant'
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 25
EMAIL_USE_TLS = False
