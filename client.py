# -*-coding:utf-8 -*-

import zeep

wsdl = 'http://localhost:5000/soap?wsdl'
# wsdl = 'http://223.68.184.9:8084/DAQItem/services/CallUniversalService?wsdl'
client = zeep.Client(wsdl=wsdl)
client.service.readStringXml('abc')