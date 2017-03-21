/*
 * Filename: main.cpp
 * Author: Eddie Tapia
 * Description: This file is used to check if the
 * Date: 3/20/17
 */

#include <iostream>
using namespace std;

enum Result {
    Japanese = 2,
    English = 1,
    Malformed = 0
};
struct jap_char{
    char character[2]; // Two bytes

    jap_char(char letter){
        // Set the high bit
        character[0] = (1 << 7);
        // Set the low bit
        character[1] = letter;
    }
};

/*
 * Function: NumChars
 * Purpose: To determine whether the last character in the buffer defined
 * as the bytes between begin and end is English or Japanese. Japanese
 * characters are two bytes long and always have a 1 in the high bit of
 * high byte. English chars are one byte long and always have a 0 in the
 * high bit.
 * Return: 2 if last character is Japanese
 * 1 if last character is English
 * 0 if the data in the buffer is malformed
 */
int NumChars(char * begin, char * end){
    Result res = Malformed;
    // Check beginning parameter is valid
    if (!begin){
        cout << "Invalid Parameters Passed Into NumChars" << endl;
        return res;
    }
    char *copyStart = begin;
    bool flag = true;
    while(flag) {
        // Check if we have reached the last character
        if (copyStart == end){
            flag = false;
        }

        int highbit = (*copyStart >> 7) & 1;

        // Check if the byte is a japanese character
        if (highbit == 1) {
            // Check if there exists another char after it
            if(copyStart == end){
                return Malformed; // Since it is jap char, it needs two bytes
            }
            // Check if the last byte is the last character in the buffer
            if( ++copyStart == end) {
                flag = false;
                res = Japanese;
            }
            else {
                // If it is not the last character, keep traversing the buffer
                copyStart += 2;
            }
        }
        // Check if the byte is an english character
        else if (highbit == 0) {
            res = English;
            copyStart++;
        }
    }
    return res;
}

int main() {
    char englishWord[] = "car";
    char * englishEnd = englishWord + 2;
    jap_char japaneseWord('s');
    char * japCharPointer = japaneseWord.character;
    char * japEndPointer = japaneseWord.character + 1;

    int answer = NumChars(englishWord, englishEnd);
    cout << answer << endl;
    answer = NumChars(japCharPointer, japEndPointer);
    cout << answer << endl;

    // Test cases to check

    return 0;
}