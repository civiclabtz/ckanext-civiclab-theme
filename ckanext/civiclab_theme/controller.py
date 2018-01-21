import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckan.lib.base import BaseController
from ckan.common import OrderedDict, c, config, request, _
import requests
import json

class ApplicationsController(BaseController):
    def applications(self):
        return plugins.toolkit.render('applications.html')
    

class DevelopersController(BaseController):
    def developers(self):
        return plugins.toolkit.render('developers.html')

class DataRequestController(BaseController):
    def datarequest(self):
        return plugins.toolkit.render('datarequest.html')

class ContactController(BaseController):
    def contact(self):
        return plugins.toolkit.render('contact.html')


