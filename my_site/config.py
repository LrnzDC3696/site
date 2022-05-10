from os import environ

DJANGO_DEBUG = True if environ['DJANGO_DEBUG'] == '1' else False
DJANGO_SECRET_KEY = environ['DJANGO_SECRET_KEY']

GOOGLE_CLIENT_ID = environ['GOOGLE_CLIENT_ID']
GOOGLE_CLIENT_SECRET = environ['GOOGLE_CLIENT_SECRET']
