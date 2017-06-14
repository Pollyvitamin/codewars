"""
Write a function named firstNonRepeatingCharacter that takes a string input, and returns 
the first character that is not repeated anywhere in the string.

For example, if given the input 'stress', the function should return 't', since the letter t 
only occurs once in the string, and occurs first in the string.

As an added challenge, upper- and lowercase letters are considered the same character, but 
the function should return the correct case for the initial letter. For example, the input 
'sTreSS' should return 'T'.

If a string contains all repeating characters, it should return the empty string ("").
"""

def first_non_repeating_letter(string):
    amount=[]
    for i in string.lower():
      amount.append(string.lower().count(i))
    for letter, count in zip(string,amount):
      if count == 1:
        return letter
    return ''
 
