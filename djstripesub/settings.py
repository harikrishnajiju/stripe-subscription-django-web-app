"""
Django settings for djstripesub project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-6@rdtei@s@!(4+^o7_&m2j0dhi@hm$s*)x6nwbo2_w*!c_b2*-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['stripesubscriptiondjango.herokuapp.com',
                 '127.0.0.1',
                 ]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites', # new
    'allauth', # new
    'allauth.account', # new
    'allauth.socialaccount', # new
    'subscriptions.apps.SubscriptionsConfig' #subscriptions app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djstripesub.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'djstripesub.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# for django >= 3.1
STATICFILES_DIRS = [Path(BASE_DIR).joinpath('static')]  # new

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


#AUTHENTICATIONNN

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

# We have to set this variable, because we enabled 'django.contrib.sites'
SITE_ID = 1

# User will be redirected to this page after logging in
LOGIN_REDIRECT_URL = '/'

# If you don't have an email server running yet add this line to avoid any possible errors.
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

#CSRF TRUSTED ORIGINS

CSRF_TRUSTED_ORIGINS = ["https://stripesubscriptiondjango.herokuapp.com",]

#STRIPE

STRIPE_PUBLISHABLE_KEY = 'pk_test_51LeiyXSCC5Vm9q7RZW4FOfNpvf0dQFVgjXPfJAaVZbX15Zs77UrCM7oQVR22ZA3E8VeqxIgmaNGU9c1Ugdh4556J0085oBOWpc'
STRIPE_SECRET_KEY = 'sk_test_51LeiyXSCC5Vm9q7RhikfYG3Q0h3CGIx818oftn8PTyzk9OGgxkTMQMOVDiHwfrqAjVW5D4P8IrpL73skJFqub8Ty00wekDd8Tm'

STRIPE_PRICE_ID = 'price_1LezClSCC5Vm9q7RbnDrFB0E' #1000 mobile plan
STRIPE_PRICE_ID2 = 'price_1LfGaTSCC5Vm9q7R7ueAdZd6' #2000 basic plan
STRIPE_PRICE_ID3 = 'price_1LfGkhSCC5Vm9q7RnD4iGden' #5000 standard plan
STRIPE_PRICE_ID4 = 'price_1LfGyASCC5Vm9q7RdyLgB1hn' #700 premium plan monthly

STRIPE_ENDPOINT_SECRET = 'whsec_fc349d312fd129b9d8e22437e1678e499eaff126614eb87be4f9baf0cff6efb8'
