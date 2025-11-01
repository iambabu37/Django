
from datetime import timedelta
from pathlib import Path
import os 
from environ import Env
import dj_database_url


# Build paths inside the project like this: BASE_DIR / 'subdir'.
# Initialize
env = Env()

# Calculate the path to the .env file one directory above settings.py
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Usually project root
ENV_PATH = os.path.join(BASE_DIR, '.env')

# Read the .env file from this specific location
env.read_env(env_file=ENV_PATH)

BASE_DIR = Path(__file__).resolve().parent.parent
# print(BASE_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

SECRET_KEY = env('DJANGO_SECRET_KEY')
DEBUG = env('DEBUG', '') != 'False'

# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.postgres',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'myapp',
    'user',
    'rest_framework',
    'rest_framework_simplejwt.token_blacklist',
    'storages',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    
]

SITE_ID = 1

SOCIALACCOUNT_PROVIDERS = {
    'google' :{
        'APP' : {
            'client_id' : env('OAUTH_GOOGLE_CLIENT_ID'),
            'secret' :  env('OAUTH_GOOGLE_SECRET')
        },
    },
}

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',

]
AUTH_USER_MODEL = 'user.CustomUser'

ROOT_URLCONF = 'myProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,"templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'myProject.wsgi.application'

# AUTHENTICATION_BACKENDS = (
#     'social_core.backends.google.GoogleOAuth2',  # Example OAuth provider
#     'django.contrib.auth.backends.ModelBackend',
# )

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
}

# SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'your-google-client-id'
# SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'your-google-client-secret'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
# sudo -u postgres psql

DATABASES = {
    'default': dj_database_url.config(default='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3'))
}


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / "db.sqlite3",
#     }
# }
# from decouple import config

# # AWS S3 settings
# AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
# AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
# AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
# AWS_S3_REGION_NAME = config('AWS_S3_REGION_NAME')
# AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

# AWS_S3_SIGNATURE_NAME = 's3v4',
# AWS_S3_REGION_NAME = 'AWS_S3_REGION_NAME'
# AWS_S3_FILE_OVERWRITE = False
# AWS_DEFAULT_ACL =  None
# AWS_S3_VERIFY = True
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


# print(AWS_S3_CUSTOM_DOMAIN)
# print(AWS_STORAGE_BUCKET_NAME)
# print(AWS_ACCESS_KEY_ID)
# print(AWS_SECRET_ACCESS_KEY)

# print(config("DB_NAME"))
# AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
# MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# Database settings
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',  # or mysql, etc.
#         'NAME': config('DB_NAME'),
#         'USER': config('DB_USER'),
#         'PASSWORD': config('DB_PASSWORD'),
#         'HOST': config('DB_HOST'),
#         'PORT': config('DB_PORT', default='5432'),
#     }
# }
# print(DATABASES)



# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# MEDIA_URL ='/image/'
# MEDIA_ROOT = BASE_DIR /'static'

STATICFILES_DIRS = [
    BASE_DIR/"static"
]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = '/login/'

LOGIN_REDIRECT_URL = '/'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

SOCIALACCOUNT_LOGIN_ON_GET = True

ACCOUNT_USER_MODEL_USERNAME_FIELD = None  # Disables username field in allauth
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'  # Login via email
ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_EMAIL_VERIFICATION = 'mandatory'  # or 'optional' or 'none' depending on your needs
ACCOUNT_SIGNUP_FIELDS = ('email',)  # Fields you want in signup form (email + password handled)


SOCIALACCOUNT_QUERY_EMAIL = True
SOCIALACCOUNT_AUTO_SIGNUP = True
ACCOUNT_UNIQUE_EMAIL = True
