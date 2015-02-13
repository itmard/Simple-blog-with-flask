# -*- coding: utf-8 -*-
__author__ = 'itmard'

# python imports
from hashlib import sha384
from datetime import datetime

# flask imports
from mongoengine import Document, StringField, DateTimeField, ReferenceField


# project imports


class User(Document):
    blog_title = StringField(required=True)
    username = StringField(required=True)
    email = StringField(required=True)
    __password = StringField(required=True)

    def __init__(self, *args, **kwargs):
        Document.__init__(self, *args, **kwargs)

        if 'password' in kwargs:
            self.password = kwargs['password']

    @property
    def password(self):
        raise IOError('No read access to this property!')

    @password.setter
    def password(self, password):

        # if self.__password was empty we will save password hexdigest
        if not self.__password:
            self.__password = sha384(password).hexdigest()

    def verify_password(self, password):
        return sha384(password).hexdigest() == self.__password

    def change_password(self, old_password, new_password):
        if self.verify_password(old_password):
            self.__password = sha384(new_password).hexdigest()
            return True
        return False

    def reset_password(self):
        self.__password = None

    meta = {
        'indexes': ['username']
    }


class Post(Document):
    user_id = ReferenceField('User', required=True)
    post_title = StringField(required=True)
    description = StringField(required=True)
    created_on = DateTimeField(default=datetime.utcnow)

    meta = {
        'indexes': ['user_id']
    }
