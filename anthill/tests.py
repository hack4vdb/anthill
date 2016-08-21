#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest

from utils import concat_list_verbosely


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

