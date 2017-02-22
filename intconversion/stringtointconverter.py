"""
Author: Eddie Tapia
File name: stringtointconverter.py
Purpose: Converts a string to an integer without using built in functions
Date: Feb 20th 2017
"""


def checkFormat(string):
    """
    Used as a helper function to check if string contains valid integers
    :param string: the string whose characters we will check
    :return: True if contains valid integer, False otherwise
    """
    if string is None:
        return False
    list_of_valid_characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for character in string:
        if character not in list_of_valid_characters:
            return False
    return True


def string_to_int(input):
    """
    Will convert a valid string into an integer
    :param: input: the string that we are trying to convert to an integer
    :return: integer that was converted from the string passed in
    """
    # Check if it is a valid string and if it is empty
    if not isinstance(input, (str, unicode)) or not input:
        return 'Invalid string passed in'
    # Check if it is negative
    if input[0] == '-':
        input = input[1:]
    # Check if it is in the correct format
    if not checkFormat(input):
        return 'Invalid string passed in'
    # Loop through the string backwards and add the values
    converted_int = 0
    tens_place = 1
    for char in reversed(input):
        value = int(char)
        converted_int += value * tens_place
        tens_place *= 10
    return converted_int


def main():
    """
    Main function that will run our methods that converts strings to ints
    :return:
    """
    answer =  string_to_int('32342343')
    print 'Answer is:', answer, ' Type:', type(answer)
    answer2 = string_to_int('-932')
    print 'Answer is:', answer2, ' Type:', type(answer2)


if __name__ == "__main__":
    main()