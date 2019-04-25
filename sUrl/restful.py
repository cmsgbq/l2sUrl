# -*- coding: utf-8 -*-

from flask_restful import Resource, marshal
from flask import current_app, redirect
from . import parser
from . import handlers
from . import fields
# from .error import PaymentError


class sUrl(Resource):
    fields_get = fields.sUrl_get
    def get(self, surl):
        print('#'*15, surl)
        u = handlers.get_url({'url_short':surl})
        print(u.url_org)
        return redirect('http://'+u.url_org)

class infoUrl(Resource):
    fields_get = fields.sUrl_get
    def get(self, surl):
        u = handlers.get_url({'url_short':surl}, count=False)
        return marshal(u, self.fields_get)

class pUrl(Resource):
    parser_post = parser.pUrl_post
    fields_post = fields.pUrl_post

    def post(self):
        params = self.parser_post.parse_args(strict=True)
        print(params)
        u = handlers.add_a_url(params)
        return marshal(u, self.fields_post)



