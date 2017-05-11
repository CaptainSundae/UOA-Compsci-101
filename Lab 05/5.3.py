def count_names_in_file (filename):
    """Prints the number of names in a text file

    >>> count_names_in_file ("names.txt")
    6
    """
    file= open(filename, 'r')
    contents = file.read()
    file.close()

    word_list = contents.split(',')
    return (len(word_list))
import doctest
doctest.testmod ()
