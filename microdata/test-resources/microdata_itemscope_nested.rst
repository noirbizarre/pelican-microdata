Microdata nested itemscope test
###############################

.. itemscope:: Person

    My name is :itemprop:`John Doe <name>`

    .. itemscope:: Address
        :tag: p
        :itemprop: address

        My name is :itemprop:`John Doe <name>`
