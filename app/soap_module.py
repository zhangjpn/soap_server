# -*-coding:utf-8 -*-

from flask_spyne import Spyne
from spyne.protocol.soap import Soap11
from spyne.model.primitive import Unicode, Integer
from spyne.model.complex import Iterable


def create_soap_service(app):
    spyne = Spyne(app)
    class SomeSoapService(spyne.Service):
        __service_url_path__ = '/soap/someservice'
        __in_protocol__ = Soap11(validator='lxml')
        __out_protocol__ = Soap11()

        @spyne.srpc(Unicode, Integer, _returns=Iterable(Unicode))
        def echo(str, cnt):
            for i in range(cnt):
                yield str

    soap_service = SomeSoapService()
    return soap_service