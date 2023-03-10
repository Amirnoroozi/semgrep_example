# cf. https://github.com/wsvincent/djangoforprofessionals/blob/
3f1b4e1199af91b07593eb6fe521252dfc67c75d/ch10-books/config/settings.py
from pathlib import Path
from environs import Env # new
env = Env() # new
env.read_env() # new
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("DJANGO_SECRET_KEY")
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DJANGO_DEBUG")
ALLOWED_HOSTS = ['.herokuapp.com', 'localhost', '127.0.0.1']
# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites', # new
    # Third-party
    'crispy_forms', # new
    'allauth', # new
    'allauth.account', # new
    # Local
    'accounts', # new
    'pages', # new
    'books', # new
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
ROOT_URLCONF = 'config.urls'
TEMPLATES = [
    # ok: global-autoescape-off
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(BASE_DIR.joinpath('templates'))], # new
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
            # ruleid: global-autoescape-off
            'autoescape': False
WSGI_APPLICATION = 'config.wsgi.application'
# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    "default": env.dj_db_url("DATABASE_URL", default="postgres://postgres@db/postgres")
}
# Password validation
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
