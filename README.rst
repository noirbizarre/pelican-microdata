Microdata plugin for Pelican
============================

.. image:: https://secure.travis-ci.org/noirbizarre/pelican-microdata.svg?branch=master
   :target: https://travis-ci.org/noirbizarre/pelican-microdata
.. image:: https://coveralls.io/repos/noirbizarre/pelican-microdata/badge.png?branch=master
    :target: https://coveralls.io/r/noirbizarre/pelican-microdata?branch=master
.. image:: https://img.shields.io/pypi/l/pelican-microdata.svg
    :target: https://pypi.python.org/pypi/pelican-microdata
.. image:: https://img.shields.io/pypi/pyversions/pelican-microdata.svg
    :target: https://pypi.python.org/pypi/pelican-microdata

`Microdata`_ semantic markups support for `Pelican`_ static blog generator.

Installation
------------

Install the plugin via ``pip``:

.. code-block:: bash

    ~$ pip install pelican-microdata


Usage
-----

To load the plugin, you have to add it in your settings file.

.. code-block:: python

    PLUGINS = (
        'microdata',
    )

Once loaded you have access to microdata rst directives.


Directives
~~~~~~~~~~

Microdata plugin provides two directives:

- ``itemscope``, a block directive allowing to declare an itemscope block:

  .. code-block:: ReST

      .. itemscope:: <Schema type>
          :tag: element type (default: div)
          :itemprop: optionnal itemprop attribute
          :compact: optionnal

          Nested content

- ``itemprop``, an inline directive/role allowing to annotate some text with an itemprop attribute.

  .. code-block:: ReST

      :itemprop:`Displayed text <itemprop name>`
      :itemprop:`Displayed text <itemprop name:http://some.url/>`

Settings
~~~~~~~~

You can define a vocabulary to use with the ``MICRODATA_VOCABULARY`` setting.

.. code-block:: python

    MICRODATA_VOCABULARY = 'http://data-vocabulary.org'

If not set, `schema.org <http://schema.org>` is the default value.

Example
~~~~~~~

This reStructuredText document:

.. code-block:: ReST

    .. itemscope:: Person
        :tag: p

        My name is :itemprop:`Bob Smith <name>`
        but people call me :itemprop:`Smithy <nickanme>`.
        Here is my home page:
        :itemprop:`www.exemple.com <url:http://www.example.com>`
        I live in Albuquerque, NM and work as an :itemprop:`engineer <title>`
        at :itemprop:`ACME Corp <affiliation>`.


will result in:

.. code-block:: html

    <p itemscope itemtype="http://schema.org/Person">
        My name is <span itemprop="name">Bob Smith</span>
        but people call me <span itemprop="nickname">Smithy</span>.
        Here is my home page:
        <a href="http://www.example.com" itemprop="url">www.example.com</a>
        I live in Albuquerque, NM and work as an <span itemprop="title">engineer</span>
        at <span itemprop="affiliation">ACME Corp</span>.
    </p>


.. _Microdata: http://schema.org/
.. _Pelican: http://getpelican.com/
