ALLOWED_HOSTS = ["*"]
DEBUG = True

# Database configuration
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "admin",
        "USER": "postgres",
        "PASSWORD": "1111",
        "HOST": "localhost",
        "PORT": "5432",
        "ATOMIC_REQUESTS": True,
    }
}

HOST = "http://localhost:8000"