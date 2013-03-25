Microdata plugin for Pelican
============================

.. image:: https://secure.travis-ci.org/noirbizarre/pelican-microdata.png
   :target: http://travis-ci.org/noirbizarre/pelican-microdata

Microdata semantic markups support for Pelican Blog Generator

Installation
------------

Install the plugin via ``pip``:

.. code-block:: bash

    ~$ pip install pelican-microdata

Or via ``easy_install``:

.. code-block:: bash

    ~$ easy_install pelican-microdata


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

.. code-block:: ReST

    .. itemscope:: <Schema type>
        :tag: element type (default: div)

        Nested content


    :itemprop:`Displayed test <itemprop name>`


Examples
~~~~~~~~

This reStructuredText document:

.. code-block:: ReST

    .. itemscope: Person
        :tag: p

        My name is :itemprop:`Bob Smith <name>`
        but people call me :itemprop:`Smithy <nickanme>`.
        Here is my home page:
        :itemprop:`www.exemple.com <url:http://www.example.com>`
        I live in Albuquerque, NM and work as an :itemprop:`engineer <title>`
        at :itemprop:`ACME Corp <affiliation>`.


will result in:

.. code-block:: html

    <p itemscope itemtype="http://data-vocabulary.org/Person">
        My name is <span itemprop="name">Bob Smith</span>
        but people call me <span itemprop="nickname">Smithy</span>.
        Here is my home page:
        <a href="http://www.example.com" itemprop="url">www.example.com</a>
        I live in Albuquerque, NM and work as an <span itemprop="title">engineer</span>
        at <span itemprop="affiliation">ACME Corp</span>.
    </p>
