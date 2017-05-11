import random

def poetry():
    """Returns a line of poetry of the form Noun Verb Noun
    Arguments:
        none
    Returns:
        line of poetry
    """
    noun1 = random.randint(0,5)
    verb = random.randint(0,3)
    noun2 = random.randint(0,5)
    nouns=["friend","dog","cat","rabbit","girl","boy"]
    verbs=["loves","hates","likes","is afraid of"]
    return nouns[noun1] + " "  + verbs[verb] + " " + nouns[noun2]

poetry()

import doctest
doctest.testmod()
