# -*-coding:utf-8 -*-

from werkzeug.wsgi import DispatcherMiddleware
from spyne.server.wsgi import WsgiApplication

from apps import spyned
from apps.flasked import app


# SOAP services are distinct wsgi applications, we should use dispatcher
# middleware to bring all aps together
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/soap': WsgiApplication(spyned.create_app(app))
})

if __name__ == '__main__':
    app.run()
