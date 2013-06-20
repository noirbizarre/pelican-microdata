# -*- coding: utf-8 -*-
import unittest

from os.path import dirname, join

from pelican import readers


CONTENT_PATH = dirname(__file__)


def _path(*args):
    return join(CONTENT_PATH, *args)


class TestMicrodata(unittest.TestCase):
    def setUp(self):
        super(TestMicrodata, self).setUp()

        import microdata
        microdata.register()

    def assert_rst_equal(self, rstfile, expected):
        content, _ = readers.read_file(_path(rstfile))
        self.assertEqual(content.strip().replace('\n', ''), expected.strip())

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
            '<div itemscope itemtype="http://data-vocabulary.org/Person">'
            'My name is <span itemprop="name">John Doe</span>'
            '</div>'
        )
        self.assert_rst_equal('microdata_itemscope.rst', expected)

    def test_itemscope_tag(self):
        expected = (
            '<p itemscope itemtype="http://data-vocabulary.org/Person">'
            'My name is <span itemprop="name">John Doe</span>'
            '</p>'
        )
        self.assert_rst_equal('microdata_itemscope_tag.rst', expected)

    def test_nested_scope(self):
        expected = (
            '<div itemscope itemtype="http://data-vocabulary.org/Person">'
            '<p>'
            'My name is <span itemprop="name">John Doe</span>'
            '</p>'
            '<p itemprop="address" itemscope itemtype="http://data-vocabulary.org/Address">'
            'My name is <span itemprop="name">John Doe</span>'
            '</p>'
            '</div>'
        )
        self.assert_rst_equal('microdata_itemscope_nested.rst', expected)

    def test_nested_scope_p(self):
        expected = (
            '<p itemscope itemtype="http://data-vocabulary.org/Person">'
            'My name is <span itemprop="name">John Doe</span>'
            '<span itemprop="address" itemscope itemtype="http://data-vocabulary.org/Address">'
            'My name is <span itemprop="name">John Doe</span>'
            '</span>'
            '</p>'
        )
        self.assert_rst_equal('microdata_itemscope_nested_p.rst', expected)
