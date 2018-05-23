from __future__ import print_function
import os
import sys

from dashboard.json_config import JSONConfig

_basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfiguration(object):
    """
    Base configuration. All others are derived from here.
    """
    # Debugging enabled (disable for production site).
    DEBUG = False
    # Testing enabled (disable for production site).
    TESTING = False
    # Application port (HTTP)
    APP_PORT = 5000
    # Application host/ IP address
    APP_HOST = "0.0.0.0"


class DebugConfiguration(BaseConfiguration):
    """
    Configuration for debugging the application.
    """
    DEBUG = True
    APP_PORT = 4000


class TestConfiguration(BaseConfiguration):
    TESTING = True
    APP_PORT = 4000


class LiveConfiguration(BaseConfiguration):
    TESTING = False
    DEBUG = False

    ###############
    # parse config from json config file
    json_config = JSONConfig(os.getenv('MICADO_DASHBOARD_CONFIG',
        '/var/lib/micado/dashboard.json'),
                             namespace='micado-dashboard')
    if json_config:
        APP_PORT = json_config.get("app_port")
        APP_HOST = json_config.get("app_host")

