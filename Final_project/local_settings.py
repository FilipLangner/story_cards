# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'story_cards',
        'PASSWORD': 'coderslab',
        'USER': 'postgres',
        'HOST': 'localhost',
    }
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=q!6#^v1&+zc12e99^e)$+bk1&h1u3)4gu37y$1$iz2g^6-$2n'