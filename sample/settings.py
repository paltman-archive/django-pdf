import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = ()
MANAGERS = ADMINS

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3", # Add "postgresql_psycopg2", "postgresql", "mysql", "sqlite3" or "oracle".
        "NAME": "dev.db",                       # Or path to database file if using sqlite3.
        "USER": "",                             # Not used with sqlite3.
        "PASSWORD": "",                         # Not used with sqlite3.
        "HOST": "",                             # Set to empty string for localhost. Not used with sqlite3.
        "PORT": "",                             # Set to empty string for default. Not used with sqlite3.
    }
}

ROOT_URLCONF = 'sample.urls'
TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
MEDIA_ROOT = ''
MEDIA_URL = ''
ADMIN_MEDIA_PREFIX = '/media/'
SECRET_KEY = ''

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

TEMPLATE_DIRS = (
    ('%s/templates' % (os.path.dirname(__file__)))
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    
    # apps for this sample project
    'celery',
    'pdf'
)

# pdf app settings
PDF_UPLOAD_PATH = ''         # Path on webserver where PDF files are uploaded to at first
PDF_REQUEST_QUEUE = ''       # Queue to transmit requests
PDF_RESPONSE_QUEUE = ''      # Queue to transmit responses
PDF_UPLOAD_BUCKET = ''       # Where the documents should be uploaded to
PDF_AWS_ACL = 'public-read'  # ACL to use to record data as
PDF_AMI_ID = 'ami-bb709dd2'  # Cononical Ubuntu 9.10 Image - http://developer.amazonwebservices.com/connect/entry.jspa?externalID=2754
PDF_AWS_KEY = ''             # AWS Key for accessing Bootstrap Bucket and Queues
PDF_AWS_SECRET = ''          # AWS Secret Key for accessing Bootstrap Bucket and Queues
PDF_KEYPAIR_NAME = ''        # The keypair name of your EC2 account

# celery/rabbitmq settings
BROKER_HOST = "127.0.0.1"
BROKER_PORT = 5672
BROKER_VHOST = "/"
BROKER_USER = "guest"
BROKER_PASSWORD = "guest"

CELERY_RESULT_BACKEND = "amqp"
