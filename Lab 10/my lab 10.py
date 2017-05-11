import random

def spy(my_string):
    """function which inputs a string and encodes and prints out the secret code.
    It then decodes it and prints out the original string.
    Arguments:
        my_string - the string we want to encode
    Returns:
        Nothing
    """
    my_string = my_string.lower()
    code, coded_master = master_encode(my_string)
    print("Code is:",code)
    new_string = master_decode(coded_master,code)
    print("Deciphered as:", new_string)

def master_encode(my_string):
    """function which encodes a string
    Arguments:
        my_string - the string to be encoded
    Returns:
        code - my_string in its coded form
        coded_master - the master string in its coded form
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    base_string = "abbcccddddeeeeeffffffggggggghhhhhhhhiiiiiiiiijjjjjjjjjjkkkkkkkkkkkllllllllllllmmmmmmmmmmmmmnnnnnnnnnnnnnnoooooooooooooooppppppppppppppppqqqqqqqqqqqqqqqqqrrrrrrrrrrrrrrrrrrsssssssssssssssssssttttttttttttttttttttuuuuuuuuuuuuuuuuuuuuuvvvvvvvvvvvvvvvvvvvvvvwwwwwwwwwwwwwwwwwwwwwwwxxxxxxxxxxxxxxxxxxxxxxxxyyyyyyyyyyyyyyyyyyyyyyyyyzzzzzzzzzzzzzzzzzzzzzzzzzz                           "
    master = shuffle(base_string)
    cipher = shuffle(alphabet)
    code = encode(my_string,cipher)
    coded_master = encode(master,cipher)
    return code, coded_master

def master_decode(string1,my_string):
    """function which decodes a string
    Arguments:
        string1 - the master string in coded form
        my_string - the string to be decoded
    Returns:
        new_string - decoded string
    """
    base_string = "abbcccddddeeeeeffffffggggggghhhhhhhhiiiiiiiiijjjjjjjjjjkkkkkkkkkkkllllllllllllmmmmmmmmmmmmmnnnnnnnnnnnnnnoooooooooooooooppppppppppppppppqqqqqqqqqqqqqqqqqrrrrrrrrrrrrrrrrrrsssssssssssssssssssttttttttttttttttttttuuuuuuuuuuuuuuuuuuuuuvvvvvvvvvvvvvvvvvvvvvvwwwwwwwwwwwwwwwwwwwwwwwxxxxxxxxxxxxxxxxxxxxxxxxyyyyyyyyyyyyyyyyyyyyyyyyyzzzzzzzzzzzzzzzzzzzzzzzzzz                           "
    original_dictionary = histogram(base_string)
    encoded_dictionary = histogram(string1)
    new_string = decode(my_string,original_dictionary,encoded_dictionary)
    return new_string


def encode(my_string,new_alphabet):
    """function which does the actually encoding of a string
    Arguments:
        my_string - the string to be encoded
        new_alphabet - the shuffled alphabet to encode the string with
    Returns:
        encoded_string - the string in its coded form
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    encoded_string=""
    for i in range(0,len(my_string)):
        for j in range(0,len(alphabet)):
            if my_string[i] == alphabet[j]:
                encoded_string += new_alphabet[j]
    return encoded_string

#10.1
def decode(string,dictionary_one,dictionary_two):
    """
    Takes the values from one dictionary and uses it to decode a secret message using the key in a different dictionary.

    Arguement:
    string -- an encoded string
    diction_one -- a dictionary  
    diction_two -- a dictionary

    Return:
    decoded message

    >>> decode("twlwjmzjdkjzplmva", {'t': 20, 'u': 21, 'v': 22, 'w': 23, 'p': 16, 'q': 17, 'r': 18, 's': 19, 'x': 24, 'y': 25, 'z': 26, 'd': 4, 'e': 5, 'f': 6, 'g': 7, ' ': 27, 'a': 1, 'b': 2, 'c': 3, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'h': 8, 'i': 9, 'j': 10, 'k': 11}, {'t': 8, 'u': 3, 'v': 14, 'w': 5, 'p': 20, 'q': 11, 'r': 26, 's': 22, 'x': 23, 'y': 24, 'z': 19, 'd': 13, 'e': 6, 'f': 2, 'g': 10, ' ': 21, 'a': 7, 'b': 17, 'c': 15, 'l': 18, 'm': 9, 'n': 4, 'o': 1, 'h': 16, 'i': 12, 'j': 27, 'k': 25})
    'here is my string'

    >>> decode("cxnlvbujwlumxejlnjqnkb", {'t': 20, 'u': 21, 'v': 22, 'w': 23, 'p': 16, 'q': 17, 'r': 18, 's': 19, 'x': 24, 'y': 25, 'z': 26, 'd': 4, 'e': 5, 'f': 6, 'g': 7, ' ': 27, 'a': 1, 'b': 2, 'c': 3, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'h': 8, 'i': 9, 'j': 10, 'k': 11}, {'t': 21, 'u': 18, 'v': 8, 'w': 19, 'p': 11, 'q': 3, 'r': 22, 's': 13, 'x': 14, 'y': 12, 'z': 25, 'd': 16, 'e': 7, 'f': 23, 'g': 24, ' ': 10, 'a': 26, 'b': 5, 'c': 1, 'l': 20, 'm': 9, 'n': 15, 'o': 6, 'h': 17, 'i': 2, 'j': 27, 'k': 4})
    'another string to code'


    """
    new_string=""
    for letter in string:
        number= dictionary_two[letter]
        for key in dictionary_one:
            if number== dictionary_one[key]:
               new_string+=key
    return new_string



#10.2
def histogram(string):
    """
    Takes a string and returns a dictionary that represents a histogram of letter counts

    Arguement:
    string -- a string

    Returns:
    histogram dictionary of letter counts

    """
    histogram = {}
    for letter in string:
        if letter not in histogram:
            histogram[letter] = 1
        else:
            histogram[letter] += 1
    return histogram

#10.3
def shuffle(string):
    """
    Takes a string and shuffles it into a random order

    Arguement:
    string -- a string

    Returns:
    a shuffled string
    """
    import random
    new_string=""
    while len(string)>0:
        num= random.randint(0, len(string)-1)
        new_string+= string[num]
        string= string[:num] + string[num+1:]
    return new_string

import doctest
doctest.testmod()


















            
    
    
