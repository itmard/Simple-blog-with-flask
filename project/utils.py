# -*- coding: utf-8 -*-
__author__ = 'itmard'

def edit_property(old, new):
    '''
    helper for edit value
    :param old:
    :param new:
    :return:
    '''
    if new not in [None, '', u'']:
        old = new
    return old