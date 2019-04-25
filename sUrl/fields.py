# -*- coding: utf-8 -*-


from flask_restful import fields
sUrl_get = {
    'url_org' : fields.String,
    'times' : fields.Integer,
    'url_short': fields.String,
    'generate_time': fields.Integer,
    'status': fields.Integer,
}

pUrl_post ={
    'url_org' : fields.String,
    'times' : fields.Integer,
    'url_short': fields.String,
    'generate_time': fields.Integer,
    'status': fields.Integer,
}

