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


def split_string_by_newlines(string, n_characters_per_string):
    """
    Splits the string along newlines returning a list of strings that have at
    most n_characters_per_string characters.
    Usefull to split messages to the FB bot in chunks with max 320 characters
    """
    results = ['']
    chunks = string.split("\n")
    idx = 0
    for c in chunks:
        if len(results[idx] + c) <= n_characters_per_string:
            results[idx] = "\n".join([ results[idx], c ])
        else:
            results.append(c)
            idx += 1
    return [r.strip() for r in results if r]
