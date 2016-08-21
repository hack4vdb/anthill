#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals


def concat_list_verbosely(string_list):
    """
    Convert list of strings into comma separated string with smart usage of "und"
    """
    if len(string_list) > 1:
        result = ", ".join(string_list[:-1])
        return " und ".join([result] + string_list[-1:])
    else:
        return ", ".join(string_list)


def make_absolute_url(path):
    #TODO: load domain from settings
    return 'http://weilsumwasgeht.at{}'.format(path)

