import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def define(word) :
    if word in data :           #checks if the word is in the data file
        number = len(data[word])        #finds the number of elements of list associated with that particular key
        print()                         #extra line
        for i in range(number) :        #displays all possible definitions
            print(data[word][i])
    elif word.capitalize() in data :    #for nouns like Delhi and France with first letter capital
        define(word.capitalize())
    elif word.upper() in data :         #for acronyms like USA and NATO with all capitals
        define(word.upper())
    elif word.lower() in data :         #for normal words typed incorrectly
        define(word.lower())
    elif len(get_close_matches(word, data.keys(), cutoff = 0.75)) > 0 :     #words not exactly in dictionary but with close matches
        closest_match = get_close_matches(word, data.keys(), cutoff = 0.75)[0]      #most probable word
        print("\nThis word does not exist\nDid you mean " + closest_match + " ? (Press 'Y'/'y' for YES or press any other key for NO ) : ", end = '')
        if input().lower() == 'y' :
            return define(closest_match)
    else :
        print("\nThis word does not exist\nNo possible matches found")

loop = True
while(loop) :
    word = input("Enter a word : ")
    define(word.lower())
    print("\nWould you like to enter a different word ? (Press 'Y'/'y' for YES or press any other key for NO ) : ", end = '')
    if input().lower() != 'y' :
        loop = False
    print()
print("\nThanks for using this Interactive Dictionary\n")
