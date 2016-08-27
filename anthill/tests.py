#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest

from utils import concat_list_verbosely
from utils import split_string_by_newlines


class TestUtils(unittest.TestCase):

    def test_concat_list_verbosely(self):
        list0 = []
        list0a = ['']
        list1 = ['foo']
        list2 = ['foo', 'bar']
        list3 = ['foo', 'bar', 'lorem']
        list4 = ['foo', 'bar', 'lorem', 'ipsum']

        self.assertEqual(concat_list_verbosely(list0), '')
        self.assertEqual(concat_list_verbosely(list0a), '')
        self.assertEqual(concat_list_verbosely(list1), 'foo')
        self.assertEqual(concat_list_verbosely(list2), 'foo und bar')
        self.assertEqual(concat_list_verbosely(list3), 'foo, bar und lorem')
        self.assertEqual(concat_list_verbosely(list4), 'foo, bar, lorem und ipsum')

    def test_split_string_by_newline(self):
        string0 = "hello foo"
        string1 = "hello\nfoo"
        string2 = "hello\nfoo\nwe can do this"
        string2a = "hello\n\nfoo\nwe can do this"
        string3 = "hello foo we can do this"
        self.assertEqual(split_string_by_newlines(string0, 10), ["hello foo"])
        self.assertEqual(split_string_by_newlines(string1, 10), ["hello\nfoo"])
        self.assertEqual(split_string_by_newlines(string2, 10), ["hello\nfoo", "we can do this"])
        self.assertEqual(split_string_by_newlines(string2a, 10), ["hello\n\nfoo", "we can do this"])
        self.assertEqual(split_string_by_newlines(string3, 10), ["hello foo we can do this"])
