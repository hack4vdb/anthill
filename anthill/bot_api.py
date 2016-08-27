#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import requests

from itsdangerous import JSONWebSignatureSerializer


def send_text(text, fb_bot_id, delay=0):
    s = JSONWebSignatureSerializer('anthill4vdb')
    data = {
        "msgtype": "t", # text
        "fb_recipient_id": fb_bot_id,
        "delay": delay,
        "data": text
    }
    payload = {
        "data": s.dumps(data)
    }
    requests.post('https://vdbmemes.appspot.com/fb/relay', json=payload)


def send_text_with_button(text, button, fb_bot_id, delay=0):
    s = JSONWebSignatureSerializer('anthill4vdb')
    data = {
        "msgtype": "r", # free form
        "fb_recipient_id": fb_bot_id,
        "delay": delay,
        "data": {
            "recipient": {
                "id": fb_bot_id
            },
            "message": {
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "button",
                        "text": text,
                        "buttons":[{
                            "type": "web_url",
                            "url": button.get('url', ''),
                            "title": button.get('text', '')
                        }]
                    }
                }
            }
        }
    }
    payload = {
        "data": s.dumps(data)
    }
    print(s.dumps(data))
    requests.post('https://vdbmemes.appspot.com/fb/relay', json=payload)

