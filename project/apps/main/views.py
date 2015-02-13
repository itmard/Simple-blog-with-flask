# -*- coding: utf-8 -*-
__author__ = 'itmard'

# python import
from datetime import datetime

from mongoengine import DoesNotExist


# flask import
from flask import session, g, abort, render_template, \
    redirect, url_for, flash

# project imports
from project.apps.main import main
from project.utils import edit_property
from project.access import not_login_allowed, login_required
from forms import SignupForm, LoginForm, EditForm, PostForm, \
    EditPostForm
from models import User, Post


@main.route('/', methods=['GET', 'POST'])
@main.route('/login', methods=['GET', 'POST'])
@not_login_allowed
def login():
    form = LoginForm()
    if form.validate_on_submit():
        try:
            user_obj = User.objects.get(username=form.username.data)

            if user_obj.verify_password(form.password.data):
                session['user'] = str(user_obj.pk)
                return redirect(url_for('main.index'))
        except(DoesNotExist):
            pass
        flash('User or password is wrong maybe user does not exist')
    return render_template('login.html', form=form)


@main.route('/logout/', methods=['GET'])
@login_required
def logout():
    del session['user']
    return redirect(url_for('main.login'))


@main.route('/signup/', methods=['GET', 'POST'])
@not_login_allowed
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        try:
            User.objects.get(username=form.username.data)
            flash('User with this username exists')
            return redirect(url_for('main.signup'))
        except(DoesNotExist):
            user_obj = User(username=form.username.data)
            user_obj.blog_title = form.blog_title.data
            user_obj.email = form.email.data
            user_obj.password = form.password.data
            user_obj.save()
            flash('Registered')
            return redirect(url_for('main.login'))
    return render_template('signup.html', form=form)


@main.route('/index/', methods=['GET'])
@login_required
def index():
    user_obj = g.user
    user_posts = Post.objects(user_id=user_obj).order_by('-created_on')
    return render_template('index.html', posts=user_posts)


@main.route('/edit/', methods=['GET', 'POST'])
@login_required
def edit():
    form = EditForm()
    if form.validate_on_submit():
        user_obj = g.user
        user_obj.blog_title = edit_property(user_obj.blog_title,
                                            form.blog_title.data)
        user_obj.email = edit_property(user_obj.email, form.email.data)
        if form.username.data:
            try:
                User.objects.get(username=form.username.data)
                form.username.errors.append('User Exist')
            except(DoesNotExist):
                user_obj.username = form.username.data

        if form.new.data and form.old.data:
            # so user wanted to change his password to
            if not user_obj.change_password(form.old.data, form.new.data):
                form.old.errors.append('Wrong password.')

        elif form.new.data or form.old.data:
            if form.new.data:
                form.new.errors.append('Input old password.')
            else:
                form.old.errors.append('Input new password.')

        user_obj.save()
        flash('Updated')

    return render_template('edit.html', form=form)


@main.route('/post/', methods=['GET', 'POST'])
@login_required
def post():
    form = PostForm()
    if form.validate_on_submit():
        post_obj = Post(post_title=form.post_title.data)
        post_obj.description = form.description.data
        post_obj.user_id = g.user
        post_obj.save()
        flash('Created')
        return redirect(url_for('main.post'))
    return render_template('post.html', form=form)


@main.route('/<string:user_name>/')
def show_posts(user_name):
    try:
        user_obj = User.objects.get(username=user_name)
        user_posts = Post.objects(user_id=user_obj).order_by('-created_on')[:3]
        print user_obj.blog_title
        return render_template('show_posts.html', posts=user_posts)

    except(DoesNotExist):
        return abort(404)


@main.route('/post/delete/<string:pk>/')
@login_required
def delete_post(pk):
    try:
        post_obj = Post.objects.get(pk=pk)
        post_obj.delete()
        post_obj.save()
        flash('Deleted')
    except(DoesNotExist):
        flash('Does not exist')
    return redirect(url_for('main.index'))


@main.route('/post/edit/<string:pk>/', methods=['GET', 'POST'])
@login_required
def edit_post(pk):
    form = EditPostForm()
    try:
        post_obj = Post.objects.get(pk=pk)
    except(DoesNotExist):
        flash('Does not exist')
        return abort(404)

    if form.validate_on_submit():
        post_obj.post_title = edit_property(post_obj.post_title,
                                            form.post_title.data)
        post_obj.description = edit_property(post_obj.description,
                                             form.description.data)
        post_obj.created_on = datetime.utcnow()
        post_obj.save()
        flash('Edited')
    return render_template('post_edit.html', form=form)
