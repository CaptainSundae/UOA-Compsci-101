

def who_wins(person1_choice,person2_choice):
    """Returns the name of the person who won, "person1" , "person2" , or "tie"
    Arguments:
        person1_choice - person1's choice
        person2_choice - person2's choice
    Returns:
     "person1" or "person2"
    >>> who_wins("rock","scissors")
    'person1'
    >>> who_wins("scissors","paper")
    'person1'
    >>> who_wins("paper","rock")
    'person1'
    >>> who_wins("rock","paper")
    'person2'
    >>> who_wins("scissors","rock")
    'person2'
    >>> who_wins("paper","scissors")
    'person2'
    >>> who_wins("paper","paper")
    'tie'
    """
    if (person1_choice == "rock" and person2_choice == "scissors") or (person1_choice == "scissors" and person2_choice == "paper") or (person1_choice == "paper" and person2_choice == "rock"):
        return "person1"
    elif person1_choice == person2_choice:
        return "tie"
    return "person2"


import doctest
doctest.testmod()
