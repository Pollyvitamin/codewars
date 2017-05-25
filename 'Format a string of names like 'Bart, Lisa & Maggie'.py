"""
Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.

Example:

namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

namelist([ {'name': 'Bart'} ])
# returns 'Bart'

namelist([])
# returns ''

Note: all the hashes are pre-validated and will only contain A-Z, a-z, '-' and '.'.
"""

def namelist(names):
  import string
  valid_symbols=string.ascii_lowercase+string.ascii_uppercase+'-'+'.'
  tmp_result=[]
  results=''
  for item in names:
    for value in item.values():
      for letter in value:
        if letter not in valid_symbols:
          return "Name shoud contains only A-Z, a-z, '-' and '.' symbols"
      tmp_result.append(value)
  if len(tmp_result) == 0:
    return ''
  if len(tmp_result) == 1:
    return tmp_result[0]
  if len(tmp_result) == 2:
    return '{} & {}'.format(tmp_result[0], tmp_result[1]) 
  else:
    for item in tmp_result[:-2]:
      results+=item + ', '
    return results+ tmp_result[-2]+' & '+tmp_result[-1]
