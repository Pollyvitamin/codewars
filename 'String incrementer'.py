"""
Your job is to write a function which increments a string, to create a new string. 
If the string already ends with a number, the number should be incremented by 1. 
If the string does not end with a number the number 1 should be appended to the new string.

Examples:

foo -> foo1
foobar23 -> foobar24
foo0042 -> foo0043
foo9 -> foo10
foo099 -> foo100

Attention: If the number has leading zeros the amount of digits should be considered.
"""
import string

def increment_string(strng):
    alfa_part=[]
    num_part=[]
    full_nam=[]
    if len(strng) == 0:
        return '1'
    if strng.isalpha():
        return strng+'1'
    else:
        for item in strng:
            if item in string.ascii_letters:
              alfa_part.append(item)
            else:
                num_part.append(item)
        full_nam.extend(str(int(''.join(num_part))+1))
        while len(num_part) != len(full_nam):
            full_nam.insert(0,'0')
        return ''.join(alfa_part + full_nam)
