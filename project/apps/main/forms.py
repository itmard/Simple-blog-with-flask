# -*- coding: utf-8 -*-
__author__ = 'itmard'

# flask imports
from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, SubmitField, PasswordField, validators


class SignupForm(Form):
    blog_title = StringField(validators=[validators.DataRequired()])
    username = StringField(validators=[validators.DataRequired()])
    email = StringField(validators=[validators.Email(),
                                    validators.DataRequired()])
    password = PasswordField(validators=[validators.DataRequired(),
                                         validators.Length(min=6)])
    submit = SubmitField()


class EditForm(Form):
    blog_title = StringField(validators=[validators.optional()])
    username = StringField(validators=[validators.optional()])
    email = StringField(validators=[validators.Email(),
                                    validators.optional()])
    old = PasswordField(validators=[validators.Optional(),
                                    validators.Length(min=6)])
    new = PasswordField(validators=[validators.Optional(),
                                    validators.Length(min=6)])
    submit = SubmitField()


class LoginForm(Form):
    username = StringField(validators=[validators.DataRequired()])
    password = PasswordField(validators=[validators.DataRequired()])
    submit = SubmitField()


class PostForm(Form):
    post_title = StringField(validators=[validators.DataRequired()])
    description = TextAreaField(validators=[validators.DataRequired()])
    submit = SubmitField()


class EditPostForm(Form):
    post_title = StringField(validators=[validators.optional()])
    description = TextAreaField(validators=[validators.optional()])
    submit = SubmitField()

