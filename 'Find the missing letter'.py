"""
Write a method that takes an array of consecutive (increasing) letters 
as input and that returns the missing letter in the array.

You will always get an valid array. And it will be always exactly one 
letter be missing. The length of the array will always be at least 2.
The array will always contain letters in only one case.

Example:

['a','b','c','d','f'] -> 'e'
['O','Q','R','S'] -> 'P'
"""
import string

def find_missing_letter(chars):
  alphabet=list(string.ascii_letters)
  for letter in alphabet[(alphabet.index(chars[0])):(alphabet.index(chars[0])+len(chars))]:
    if letter not in chars:
      return letter

#Top solution:
def find_missing_letter(c):
    return next(chr(ord(c[i])+1) for i in range(len(c)-1) if ord(c[i])+1 != ord(c[i+1]))
