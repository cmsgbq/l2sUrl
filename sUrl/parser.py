# -*- coding: utf-8 -*-


from flask_restful import reqparse

pUrl_post = reqparse.RequestParser(bundle_errors=True)
pUrl_post.add_argument('url_org', type=str, required=True, location=['json', 'args', 'form'])
pUrl_post.add_argument('url_short', type=str, required=False, location=['json', 'args', 'form'])

