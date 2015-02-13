# -*- coding: utf-8 -*-
__author__ = 'itmard'

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class DefaultConfig(object):
    DEBUG = True
    DEPLOYMENT = False

    SECRET_KEY = 'Data@itmard'
    KEY_SECRET_KEY = '4fbX5nvGkBvmKwyBPrS!Xq@!N^QEXxn5'
    WTF_CSRF_ENABLED = False

    ACCEPT_LANGUAGES = ['en']

    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'Asia/tehran'

    MONGODB_SETTINGS = {'DB': 'simple_blog',
                        'HOST': '127.0.0.1',
                        'PORT': 27017}

    BOOTSTRAP_SERVE_LOCAL = True

    TEMPLATE = 'default'
    SITE_NAME = 'SimpleBlog'

    # Blueprint need to be installed entered here
    INSTALLED_BLUEPRINTS = (
        'main',
    )

    if DEBUG:
        LOG_FORMAT = '\033[1;35m[%(asctime)s]\033[1;m [\033[1;31m %(levelname)s \033[1;m] \033[1;32m[%(logger_name)s]\033[1;m: \
        \033[1;33m %(message)s \033[1;m'
    else:
        LOG_FORMAT = '[%(asctime)s] %(levelname)s [%(logger_name)s]: %(message)s'

    SALT = 'itmard ie salt khob'


class DevelopmentConfig(DefaultConfig):
    DEBUG = True
