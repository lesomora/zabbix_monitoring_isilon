#!/usr/bin/python 
import urllib3
import isi_sdk_8_0
urllib3.disable_warnings()

class ISIConnection():
        def __init__(self):
                self.user = "" #Username
                self.password = "" #Password

        def Conn(self, host):
                configuration = isi_sdk_8_0.Configuration()
                configuration.host = 'https://{0}:8080'.format(host)
                configuration.username = self.user
                configuration.password = self.password
                configuration.verify_ssl = False
                ISIClient = isi_sdk_8_0.ApiClient(configuration)
                return ISIClient