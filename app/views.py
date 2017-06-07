# -*-coding:utf-8 -*-

from flask import render_template, jsonify, make_response


def init_views(app):
    @app.route(r'/get/')
    def get_data():
        data = {
            'code': 1,
            'status': 'ok',
        }

        return jsonify(**data)