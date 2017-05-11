#ex 8.1
def change_case(sentence,my_type):
    """Returns the sentence in uppercase or lowercase depending on the type requested
    Arguments:
        sentence - sentence to be transformed
        mytype - either "upper" or "lower"
    Returns:
        sentence transformed to upper or lower case
    >>> change_case("rock","upper")
    'ROCK'
    >>> change_case("PAPER","lower")
    'paper'
    >>> change_case("pApEr","upper")
    'PAPER'
    >>> change_case("rock","lower")
    'rock'
    >>> change_case("PapeR","lower")
    'paper'
    >>> change_case("","upper")
    ''
    >>> change_case("","fred")
    ''
    >>> change_case("Can we dO a WHole Sentence","upper")
    'CAN WE DO A WHOLE SENTENCE'
    """
    uppercase = ["A","B","C","D","E","F","G","H",
                 "I","J","K","L","M","N","O","P",
                 "Q","R","S","T","U","V","W","X","Y","Z"]
    lowercase = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    new_sentence = ""
    for i in range(0,len(sentence)):
        if ((my_type == "upper" and
             sentence[i] in lowercase) or
            (my_type == "lower" and
             sentence[i] in uppercase)):
            new_sentence += get_new_letter(sentence[i],my_type)
        else:
            new_sentence += sentence[i]
    return new_sentence

def get_new_letter(letter, my_type):
    """Returns letter in uppercase or lowercase depending on my_type
    Arguments:
        sentence - letter to be transformed
        my_type - either "upper" or "lower"
    Returns:
        letter transformed to upper or lower case
    >>> get_new_letter("r","upper")
    'R'
    >>> get_new_letter("P","lower")
    'p'
    """
    uppercase = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    lowercase = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    if my_type == "upper":
        for i in range(0,len(lowercase)):
            if lowercase[i] == letter:
                return uppercase[i]
    else:
        for i in range(0,len(uppercase)):
            if uppercase[i] == letter:
                return lowercase[i]


def case_insensitive_substring(my_word, my_string):
    """
    >>> case_insensitive_substring("ab","ab fab")
    True
    >>> case_insensitive_substring("Ab","ab fab")
    True
    >>> case_insensitive_substring("ba", "ab fab")
    False
    """
    my_word=change_case(my_word, "lower")
    my_string=change_case(my_string, "lower")
    if my_word in my_string:
        return True
    return False


#ex 8.2

def advanced_poetry():
    """
    
    """
    
    adjectives= get_word('adjective.txt')
    nouns= get_word('noun.txt')
    adverbs= get_word('adverb.txt')
    verbs= get_word('verb.txt')

    adjective=get_random_word(adjectives)
    noun=get_random_word(nouns)
    adverb=get_random_word(adverbs)
    verb=get_random_word(verbs)

    return get_word('adjective.txt') + ' ' + get_word('noun.txt') + ' ' + get_word('adverb.txt') + ' ' + get_word('verb.txt') + ' ' + get_word('adjective.txt') + ' ' + get_word('noun.txt')

def get_word(filename):
    import random
    file=open(filename, 'r')
    string_list=file.read().split()
    file.close()
    return string_list[random.randint(0, len(string_list)-1)]

def get_random_word(word_list):
    import random
    index = random.randint(0, len(word_list)-1)
    
    

import doctest
doctest.testmod()
