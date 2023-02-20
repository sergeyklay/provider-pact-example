# This file is part of the Specmatic Testing Example.
#
# Copyright (C) 2023 Serghei Iakovlev <egrep@protonmail.ch>
#
# For the full copyright and license information, please view
# the LICENSE file that was distributed with this source code.

"""Manage the application creation and configuration process."""

import os

from flask import Flask


def create_app(config=None) -> Flask:
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)

    configure_app(app, config)
    configure_blueprints(app)
    configure_extensions(app)
    configure_context_processors(app)

    return app


def load_env_vars(base_path: str):
    """Load the current dotenv as system environment variable."""
    dotenv_path = os.path.join(base_path, '.env')

    from dotenv import load_dotenv
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path=dotenv_path)


def configure_app(app: Flask, config_name=None):
    """Configure application."""
    from provider.config import config, Config

    # Use the default config and override it afterwards
    app.config.from_object(config['default'])

    if config is not None:
        # Config name as a string
        if isinstance(config_name, str) and config_name in config:
            app.config.from_object(config[config_name])
            config[config_name].init_app(app)
        # Config as an object
        else:
            app.config.from_object(config_name)
            if isinstance(config_name, Config):
                config_name.init_app(app)

    # Update config from environment variable (if any).
    # Export this variable as follows:
    #   export APP_SETTINGS="/var/www/server/config.py"
    app.config.from_envvar('APP_SETTINGS', silent=True)


def configure_blueprints(app: Flask):
    """Configure blueprints for the application."""
    # main blueprint registration
    from provider.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # api blueprint registration
    from provider.api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/v1')


def configure_extensions(app: Flask):
    """Configure extensions for the application."""
    from provider.models import db, Product
    from flask_migrate import Migrate, upgrade

    # Flask-SQLAlchemy
    db.init_app(app)

    # Flask-Migrate
    migrate = Migrate()
    migrate.init_app(app, db)

    @app.cli.command()
    def deploy():
        """Run deployment tasks."""
        # Migrate database to latest revision.
        upgrade()

    @app.cli.command()
    def seed():
        """Add seed data to the database."""
        from faker import Faker
        fake = Faker()

        db.create_all()
        for _ in range(1000):
            Product.seed(fake)


def configure_context_processors(app: Flask):
    """Configure the context processors."""
    import inspect
    from provider import models

    @app.shell_context_processor
    def make_shell_context():
        """Configure flask shell command to automatically import app objects."""
        return dict(
            app=app,
            db=models.db,
            **dict(inspect.getmembers(models, inspect.isclass)))
