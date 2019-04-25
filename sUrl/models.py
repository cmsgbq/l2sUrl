# -*- coding: utf-8 -*-


from dbalchemy import db, ModelDefault
from sqlalchemy.orm import relationship
from util.timestamp import get_now_timestamp



class NormalURL(ModelDefault):
    __tablename__ = 'normal_url'
    id = db.Column(db.Integer, primary_key=True)
    url_org = db.Column(db.String(2000), nullable=False)
    times = db.Column(db.Integer, nullable=False, default=0)
    url_short = db.Column(db.String(10), nullable=True)
    generate_time = db.Column(db.BigInteger, nullable=False, default=get_now_timestamp())

    def __init__(self,
                 url_org,
                 generate_time=None,
                 *args,
                 **kwargs):
        self.url_org = url_org
        super(NormalURL, self).__init__(*args, **kwargs)

    def __repr__(self):
        return f'<NormalURL {self.id} : {self.url_org}>' 

