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


