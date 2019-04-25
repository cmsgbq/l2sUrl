# -*- coding: utf-8 -*-

from settings import INIT_FIRST_SEQ
from .models import (
    NormalURL
)
from util.change import changeBase
# from .error import sUrlError


def add_a_url(params: dict, commit=True):
    if params['url_short']:
        u = NormalURL.query.filter_by(url_short=params['url_short']).one_or_none()
        if u:
            u.status = -3
            return u
        u = NormalURL.create(commit=commit, **params)
        return u
    else:
        u = NormalURL.query.filter_by(url_org=params['url_org']).one_or_none()
        if u:
            u.status = -1
            return u
            # {'status': -1 }
            # raise sUrlError.UrlHasExist(params.url_org)
        u = NormalURL.create(commit=commit, **params)
        update_url_short(u, commit)
        return u


def update_url_short(a:NormalURL, commit=True):
    if NormalURL.query.filter_by(url_short=changeBase(a.id + INIT_FIRST_SEQ, 62)).one_or_none():
        a.update(**{'url_short':changeBase(a.id + INIT_FIRST_SEQ, 62)+'x'})
    else:
        a.update(**{'url_short':changeBase(a.id + INIT_FIRST_SEQ, 62)})


def update_url_click_times(a:NormalURL, commit=True):
    a.update(**{'times':a.times + 1})
    

def get_url(params: dict, commit=True, count=True):
    a = NormalURL.query.filter_by(url_short=params['url_short']).one_or_none()
    if a==None:
        return {'status': -2 }
        # raise sUrlError.UrlHasExist(params.url_org)
    if count:
        update_url_click_times(a)
    return a

