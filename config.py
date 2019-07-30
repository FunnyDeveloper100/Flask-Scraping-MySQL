from os import getenv
import os


def bool_env(var_name, default=False):
    test_val = getenv(var_name, default)
    # Explicitly check for "False" and "false" since all non-empty strings are
    # normally coerced to True.
    if test_val in ('False', 'false'):
        return False
    return bool(test_val)


def float_env(var_name, default=0.0):
    """Get an environment variable coerced to a float value.
    This has the same arguments as bool_env. If a value cannot be coerced to a
    float, a ValueError will be raised.
    """
    return float(getenv(var_name, default))


def int_env(var_name, default=0):
    """Get an environment variable coerced to an integer value.
    This has the same arguments as bool_env. If a value cannot be coerced to an
    integer, a ValueError will be raised.
    """
    return int(getenv(var_name, default))


def str_env(var_name, default=''):
    """Get an environment variable as a string.
    This has the same arguments as bool_env.
    """
    return getenv(var_name, default)


# Set those for Heroku configuration
APPLICATION_ENV = str_env('APPLICATION_ENV', 'development')
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


def get(name, default=None):
    """
    Get the value of a variable in the settings module scope.
    """
    return globals().get(name, default)


class BaseConfig(object):
    DEBUG = bool_env('DEBUG', True)
    PORT = int_env('PORT', 8001)

    SECRET_KEY = str_env('SECRET_KEY', 'Upw0rk!')

    SQLALCHEMY_DATABASE_URI = str_env(
        'SQLALCHEMY_DATABASE_URI',
        'mysql://test:12345@mysql_db/csv_mysql'
    )


class DevConfig(BaseConfig):
    # Database connection (Dev)
    BASE_URI = "http://localhost:8001"


class StagingConfig(BaseConfig):
    BASE_URI = "http://domain.test"
    PORT = 80


class ProdConfig(BaseConfig):
    # Database connection (Prod)
    BASE_URI = "http://domain.test"
    DEBUG = False
    PORT = 80


settings = None
if APPLICATION_ENV == 'development':
    settings = DevConfig()
elif APPLICATION_ENV == 'staging':
    settings = StagingConfig()
elif APPLICATION_ENV == 'production':
    settings = ProdConfig()
