# -*- coding: utf-8 -*-

from . import api
from . import restful


api.add_resource(restful.sUrl, '/s/<string:surl>', endpoint='sUrl')
api.add_resource(restful.infoUrl, '/info/<string:surl>', endpoint='infoUrl')

api.add_resource(restful.pUrl, '/p', endpoint='pUrl')

