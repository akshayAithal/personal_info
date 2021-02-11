#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Yggdrasil application server definition."""

# pylint: disable=no-member

import os
import warnings

from flask import Flask
from flask_apscheduler import APScheduler

# from flask_restful import Api, Resource  # Implement OpenAPI/Swagger definitions

from flask_migrate import Migrate

# TODO: Use the gkn library instead.
from personal_info.logger import install_logger, logger


def create_app(config_filename=None, config=None):
    """Application factory function that returns the flask app
    with the configs loaded correctly.

    Use YGGDRASIL_CFG to point to a right configuration file.

    The CFG file *needs* to set the SQLALCHEMY_URI value, and the SECRET_KEY.

    For secret key, use os.urandom(32). Don't put the function into the file.
    Open an interpreter, calculate this value and put that value into the file
    as a string.

    Protip: If something does not work, try accessing this in incognito mode.

    Args:
        config_filename: Path to a config file. This can be
            relative to the instance folder.
        config: This is the name of one of the configs that should be loaded.
            This is loaded from the config file. Example: config='test' will
            load test.py

    """

    app = Flask(
        __name__,
        static_folder="ui/assets",
        template_folder="ui",
        instance_relative_config=True)

    #if config:
    #    app.config.from_object(config)
    #else:
    #    app.config.from_object("config.default")

    if config_filename:
        app.config.from_pyfile(config_filename)
    else:
        if os.environ.get("PERSONAL_CFG"):
            app.config.from_envvar("PERSONAL_CFG")
        else:
            warnings.warn(
                "Either set the YGGDRASIL_CFG environment variable"
                "or provide the config_filename argument to the "
                "application factory function. The default configuration "
                "has been used, but the changes to the database are "
                "now stored in memory, which is not recommended.",
                UserWarning)
    #logger.debug("SQLALCHEMY_DATABASE_URI = {}".format(
    #    app.config["SQLALCHEMY_DATABASE_URI"]))

    install_logger(app)
    from personal_info.api import home_blueprint
    app.register_blueprint(home_blueprint)
    return app
