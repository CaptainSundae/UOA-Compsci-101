#ex9.1
def find_longest(string):
    """
    Arguement:
    string -- a string

    Return:
    length of the longest string

    """
    lines= string.split('\n')
    longest_number=len(string[0])

    for line in lines:
        if len(line)> longest_number:
            longest_number=len(line)
    return(longest_number)

#9.2
def find_num_lines(strings):
    """"""
    line=strings.split("\n")
    return len(line[:-1])
#9.3
def print_line_length(string):
    """"""
    lines=string[:-1].split("\n")
    for line in lines:
        print(len(line))

#9.4
def pad_lines(string,padding_character):
    """
    >>> pad_lines(" 1 @ #\n2 $ %   \n3 ^ &     \n", "*")
    ' 1 @ #****\n2 $ %   **\n3 ^ &     \n'

    """
    longest=find_longest(string)
    lines=string[:-1].split("\n")
    output=''
    for line in lines:
        while len(line) < longest:
            line += padding_character
        output += (line +"\n")

    return (output)
    

    
