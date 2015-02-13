# -*- coding: utf-8 -*-
__author__ = 'itmard'

# python import
from mongoengine import ValidationError, DoesNotExist

# flask import
from flask import Flask, request, jsonify, g, session, abort


# project import
from project.extensions import db, login_manager, bootstrap
from project.config import DefaultConfig

DEFAULT_APP_NAME = 'project'


def create_app(config=None, app_name=DEFAULT_APP_NAME):
    app = Flask(app_name, static_folder='statics', template_folder='templates')

    configure_app(app, config)
    configure_i18n(app)
    configure_blueprints(app)
    configure_before_handlers(app)
    configure_extensions(app)
    add_user_to_jinja(app)

    return app


def configure_app(app, config):
    """
    tanzimate kolli app ke mamolan dar yek file zakhore mishavat tavasote in tabe
    megdar dehi va load mishavad
    """

    # config default ro dakhele app load mikone
    app.config.from_object(DefaultConfig())
    # sys.path.append(os.path.dirname(os.path.realpath(__file__)))
    if config is not None:
        # agar config degari be create_app ersal shode bashe dar in bakhsh load mishe
        # agar tanzimate in bakhsh gablan va dakhele defalt config tanzim shode
        # bashe dobare nevisi mishe
        app.config.from_object(config)

    # dar sorati ke environment variable baraye tanzimat set shode bashe ham
    # load mishe
    app.config.from_envvar('project_CONFIG', silent=True)


def configure_blueprints(app):
    """
    Tanzimate marbot be blueprint ha va load kardan ya nasbe onha ro inja anjam midim
    """

    blueprints = DefaultConfig.INSTALLED_BLUEPRINTS
    for blueprint in blueprints:
        bp = __import__('project.apps.%s' % blueprint, fromlist=[blueprint])
        app.register_blueprint(getattr(bp, blueprint))


def configure_i18n(app):
    """
    tanzimate marbot be i18n va systeme tarjome dar in bakhsh emal mishavad
    """


def configure_before_handlers(app):
    from project.apps.main.models import User

    def set_user():
        if 'user' in session:
            g.user = User.objects.get(pk=session.get('user'))
        else:
            g.user = None

    app.before_request(set_user)

def configure_extensions(app):
    db.init_app(app)
    login_manager.init_app(app)
    bootstrap.init_app(app)


def add_user_to_jinja(app):
    pass
