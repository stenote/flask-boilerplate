# -*- coding: utf-8 -*-

from app.apis.demo_api import demo_api

from app.apis.rest_api import rest_api

apis = {
    '/demo': demo_api,
    '/rest': rest_api,
}
