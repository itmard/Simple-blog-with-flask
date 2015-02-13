# -*- coding: utf-8 -*-
__author__ = 'itmard'

from flask.ext.mongoengine import MongoEngine
from flask.ext.bootstrap import Bootstrap
from flask.ext.login import LoginManager

__all__ = ['db', 'bootstrap', 'login_manager']


db = MongoEngine()
bootstrap = Bootstrap()
login_manager = LoginManager()