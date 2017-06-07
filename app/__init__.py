# -*-coding:utf-8 -*-

from flask import Flask
from .views import init_views
from .soap_module import create_soap_service


def create_app():
    app = Flask(__name__)
    init_views(app)
    create_soap_service(app)
    return app