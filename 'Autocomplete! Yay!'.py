"""
It's time to create an autocomplete function! Yay!

The autocomplete function will take in an input string and a dictionary array and 
return the values from the dictionary that start with the input string. If there 
are more than 5 matches, restrict your output to the first 5 results. If there are 
no matches, return an empty array.

Example:

autocomplete('ai', ['airplane','airport','apple','ball']) = ['airplane','airport']

For this kata, the dictionary will always be a valid array of strings. Please return 
all results in the order given in the dictionary, even if they're not always alphabetical. 
The search should NOT be case sensitive, but the case of the word should be preserved when 
it's returned.

For example, "Apple" and "airport" would both return for an input of 'a'. However, they 
should return as "Apple" and "airport" in their original cases.

Important note:

Any input that is NOT a letter should be treated as if it is not there. For example, an 
input of "$%^" should be treated as "" and an input of "ab*&1cd" should be treated as "abcd".
"""

def autocomplete(req_definition, dictionary):
    req_definition = "".join(filter(lambda symbol: symbol.isalpha(), req_definition))
    count = 0
    result=[]
    for key in dictionary:
        if req_definition == "":
          return dictionary[:5]
        if count < 5 and req_definition !="":
            if req_definition.lower() == key[0:len(req_definition)].lower():
                count += 1
                result.append(key)
        else:
            break
    return result


#the best solution:

def autocomplete(input_, dictionary):
    input_ = ''.join( [ c for c in list(input_) if c.isalpha() ])
    return [ x for x in dictionary if x.lower().startswith(input_.lower()) ][:5]
