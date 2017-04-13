"""
File: main.py
Authors: Eduardo Tapia
Date: 4/12/17
Purpose: To reverse a string containing multiple words
"""

def reversewords(words):
    """
    Returns the reverse of the string passed in
    :param words: original string
    :return: the reversed version of the string
    """
    # Check if input is valid
    if type(words) is not str:
        return "Error. Invalid Input. Please input a non-empty string"
    if len(words) == 1:
        return words
    words = words.split(' ')
    result = ''
    # Iterate through the strings
    for word in words:
        reversed_word = ''
        for character in word:
            if not character.isspace():
                reversed_word = character + reversed_word
        result += reversed_word + ' '
    return result

def main():
    string1 = "green car"
    string2 = "UCSD is really sunny today"
    string3 = 2323
    string4 = 'aaaa\nabb\nbbbb aa\nabb b bb\ncc \nccc\n cccdddddd ddd\n'
    string5 = 'a'
    print reversewords(string1)
    print reversewords(string2)
    print reversewords(string3)
    print reversewords(string4)
    print reversewords(string5)
    return 0

if __name__ == "__main__":
    main()