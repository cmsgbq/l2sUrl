from flask import Blueprint
from flask_restful import Api


bp = Blueprint('sUrl', __name__)
api = Api(bp, prefix='')


from . import urls  
