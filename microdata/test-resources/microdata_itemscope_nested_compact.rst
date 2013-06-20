Microdata nested itemscope test
###############################

.. itemscope:: Person
    :tag: p
    :compact:

    My name is :itemprop:`John Doe <name>`

    .. itemscope:: Address
        :tag: span
        :itemprop: address

        My name is :itemprop:`John Doe <name>`
