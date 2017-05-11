

def remove_punctuation(sentences):
    """Returns the sentence with punctuation removed.
    Arguments:
        sentence - sentence to have punctuation stripped from
    Returns:
        sentence with punctuation removed
    >>> remove_punctuation("'I know the answer! The answer lies within the heart of all mankind! The answer is 12? I think I'm in the wrong building.' (Charles Schulz, 'Peanuts')")
    'I know the answer The answer lies within the heart of all mankind The answer is 12 I think Im in the wrong building Charles Schulz Peanuts'
    >>> remove_punctuation("'Only two things are infinite, the universe and human stupidity, and I'm not sure about the former.' (Albert Einstein)")
    'Only two things are infinite the universe and human stupidity and Im not sure about the former Albert Einstein'
    >>> remove_punctuation('"There are three kinds of lies: lies, damned lies, and statistics." (Disraeli)')
    'There are three kinds of lies lies damned lies and statistics Disraeli'
    """
    new_sentences = ""
    punctuation = ["'","!",".","(",")",",","?",":",'"']
    for character in sentences:
        if character not in punctuation:
            new_sentences += character
    return new_sentences

import doctest
doctest.testmod()
