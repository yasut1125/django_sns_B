# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-1hq2!lfb%gpsx@1x#(3dm0q50#6pua3enn^*hstp6n=i9-37%&'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'sns_postgres',
        'PORT': '5432',
    }
}