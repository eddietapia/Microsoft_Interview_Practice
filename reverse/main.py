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
    if words is None or type(words) is not str:
        return "Error. Invalid Input. Please input a non-empty string"
    if len(words) == 1:
        return words
    words = words.split(' ')
    # Iterate through the strings
    result = ''
    for word in words:
        reversed_word = ''
        for character in word:
            reversed_word = character + reversed_word
        result += reversed_word + ' '
    return result

def main():
    string1 = "green car"
    string2 = "UCSD is really sunny today"
    print reversewords(string1)
    print reversewords(string2)
    return 0

if __name__ == "__main__":
    main()