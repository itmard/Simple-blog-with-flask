# -*- coding: utf-8 -*-
__author__ = 'itmard'

# flask imports
from flask import Blueprint


main = Blueprint('main', __name__)

from . import views
