# -*- coding: utf-8 -*-
__author__ = 'itmard'

# python imports
from functools import wraps
from mongoengine import DoesNotExist, ValidationError

# flask imports
from flask import session, abort, request, g, redirect, url_for
# project imports
from project.apps.main.models import User


def is_loged_in():
    '''
    Check if user has been logged in
    :return: Bool , True if user logged in
    '''
    if 'user' in session:
        try:
            User.objects.get(pk=session.get('user'))
            return True
        except (ValidationError, DoesNotExist):
            del session['user']
    return False



def not_login_allowed(f):
    """
    some views aren't accessible when user is logged in
    """

    @wraps(f)
    def decorator(*args, **kwargs):
        if 'user' in session:
            return redirect(url_for('main.index'))
        return f(*args, **kwargs)

    return decorator


def login_required(func):
    '''
    check if user logged in to access a route
    :param func: wrap function
    :return: abort or decorated function
    '''
    @wraps(func)
    def decorator(*args, **kwargs):
        if is_loged_in():
            return func(*args, **kwargs)
        return redirect(url_for('main.login'))
    return decorator

