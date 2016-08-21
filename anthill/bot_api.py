#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import requests

from itsdangerous import JSONWebSignatureSerializer


def send_text(text, fb_bot_id):
    s = JSONWebSignatureSerializer('anthill4vdb')

    data = {
        "msgtype": "t", # text
        "fb_recipient_id": fb_bot_id,
        "delay": 0,
        "data": text
    }
    payload = {
        "data": s.dumps(data)
    }
    requests.post('https://vdbmemes.appspot.com/fb/relay', json=payload)

