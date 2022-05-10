import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-^cm4^v0^c+9$o(0ui0*tx!y7ipk8(*qx+67ro5=xy85@qe2-!u'

DEBUG = True

ALLOWED_HOSTS = ['predatoryplantshop.com', '127.0.0.1', 'localhost']

INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'store',
	'cart',
	'account',
	'payment',
	'orders',

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

ROOT_URLCONF = 'Shop.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [BASE_DIR / 'templates'],
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
				'store.context_processors.categories',
				'cart.context_processors.cart'
			],
		},
	},
]

WSGI_APPLICATION = 'Shop.wsgi.application'

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': BASE_DIR / 'db.sqlite3',
	}
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATICFILES_DIRS = [
	os.path.join(BASE_DIR, 'static'),
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

AUTH_USER_MODEL = 'account.UserBase'
LOGIN_REDIRECT_URL = '/account/dashboard'
LOGIN_URL = '/account/login'

# EMAIL
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# STRIPE
STRIPE_ENDPOINT_SECRET = 'whsec_7dd52bb8609d80194b88d6588964684ecf3b9d46e0551ea0cdced65ace96fef9 '
STRIPE_SECRET_KEY = 'sk_test_51Kwk0bL0oFtSpOzDjOCp7qtwjlWYFy1tfQ9MR0iueYbd6teDh1QyT9QXenljVy50DfcB14pX0j8BTtaM599fRpKx00WV9q4ZlE'
os.environ.setdefault('STRIPE_PUBLISHABLE_KEY',
                      'pk_test_51Kwk0bL0oFtSpOzDnp4F9USQQVgCLw2yJvSot8EYO0y1sfZqn9ZZ1vMjT6xr7YJaGQ3iVPXXtwggnh5vf85tWBZU00nSFKAYUf')

# CART SESSION AJDI
CART_SESSION_ID = 'cart'