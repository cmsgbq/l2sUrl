# -*- coding: utf-8 -*-


import time


def get_now_timestamp():
    return time.time()*1000


def get_today_zero_timestamp():
    t = time.localtime(time.time())
    time1 = time.mktime(time.strptime(time.strftime(
        '%Y-%m-%d 00:00:00', t), '%Y-%m-%d %H:%M:%S'))
    return int(time1*1000)


def get_zero_timestamp(timestamp):
    t = time.localtime(timestamp/1000)
    time1 = time.mktime(time.strptime(time.strftime(
        '%Y-%m-%d 00:00:00', t), '%Y-%m-%d %H:%M:%S'))
    return int(time1*1000)


def get_month_zero_timestamp():
    t = time.localtime(time.time())
    time1 = time.mktime(time.strptime(time.strftime(
        '%Y-%m-01 00:00:00', t), '%Y-%m-%d %H:%M:%S'))
    return int(time1*1000)
