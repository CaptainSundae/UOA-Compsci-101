def add_gst (list_of_prices):
    """Adds GST to the prices in a list.

    Arguement:
    list of prices -- a list containing the prices of products without gst (float)

    Return:
    list of prices -- a list of products containing the prices of the products with gst (float)

    Tests:
    >>> add_gst ([3])
    [3.45]

    """
    with_gst=[]
    for price in list_of_prices:
        price= price*1.15
        with_gst= with_gst + [round(price,2)]
        
    return with_gst

import doctest
doctest.testmod ()
    
