# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest

from lxml import html

from os.path import dirname, join

from pelican import Pelican
from pelican.readers import Readers
from pelican.settings import DEFAULT_CONFIG

RESOURCES_PATH = join(dirname(__file__), 'test-resources')


def get_settings(**kwargs):
    settings = DEFAULT_CONFIG.copy()
    for key, value in kwargs.items():
        settings[key] = value
    settings['PLUGINS'] = ['microdata']
    return settings


def normalize(text):
    return html.tostring(html.fromstring(text), pretty_print=True)


class TestMicrodata(unittest.TestCase):
    def assert_rst_equal(self, rstfile, expected, **kwargs):
        pelican = Pelican(settings=get_settings(**kwargs))
        reader = Readers(pelican.settings)
        content = reader.read_file(base_path=RESOURCES_PATH, path=rstfile).content
        self.assertEqual(normalize(content), normalize(expected))

    def test_itemprop(self):
        expected = (
            '<p>'
            '<span itemprop="name">Test</span>'
            '</p>'
        )
        self.assert_rst_equal('microdata_itemprop.rst', expected)

    def test_itemprop_url(self):
        expected = '<p><a href="http://somewhere/" itemprop="url">Test</a></p>'
        self.assert_rst_equal('microdata_itemprop_url.rst', expected)

    def test_itemscope(self):
        expected = (
            '<div itemscope itemtype="http://schema.org/Person">'
            'My name is <span itemprop="name">John Doe</span>'
            '</div>'
        )
        self.assert_rst_equal('microdata_itemscope.rst', expected)

    def test_itemscope_tag(self):
        expected = (
            '<p itemscope itemtype="http://schema.org/Person">'
            'My name is <span itemprop="name">John Doe</span>'
            '</p>'
        )
        self.assert_rst_equal('microdata_itemscope_tag.rst', expected)

    def test_nested_scope(self):
        expected = (
            '<div itemscope itemtype="http://schema.org/Person">'
            '<p>'
            'My name is <span itemprop="name">John Doe</span>'
            '</p>'
            '<p itemprop="address" itemscope itemtype="http://schema.org/Address">'
            'My name is <span itemprop="name">John Doe</span>'
            '</p>'
            '</div>'
        )
        self.assert_rst_equal('microdata_itemscope_nested.rst', expected)

    def test_nested_scope_compact(self):
        expected = (
            '<p itemscope itemtype="http://schema.org/Person">'
            'My name is <span itemprop="name">John Doe</span>'
            '<span itemprop="address" itemscope itemtype="http://schema.org/Address">'
            'My name is <span itemprop="name">John Doe</span>'
            '</span>'
            '</p>'
        )
        self.assert_rst_equal('microdata_itemscope_nested_compact.rst', expected)

    def test_custom_vocabulary(self):
        expected = (
            '<div itemscope itemtype="http://data-vocabulary.org/Person">'
            'My name is <span itemprop="name">John Doe</span>'
            '</div>'
        )
        self.assert_rst_equal('microdata_itemscope.rst', expected,
                              MICRODATA_VOCABULARY='http://data-vocabulary.org')
