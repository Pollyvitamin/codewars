"""
Modify the kebabize function so that it converts a camel case string into a kebab case.

kebabize('camelsHaveThreeHumps') // camels-have-three-humps
kebabize('camelsHave3Humps') // camels-have-humps

Notes:
    the returned string should only contain lowercase letters
"""

def kebabize(string):
  result=[]
  for letter in string:
    if letter.islower():
      result.append(letter)
    elif letter.isdigit():
      pass
    else:
      result.append(' ')
      result.append(letter.lower())
  if len(result) == 0:
    return ''
  if result[0] == ' ':
    return ''.join(result[1:]).replace(' ', '-')
  else:
    return ''.join(result).replace(' ', '-')
    
 
 # the best decision:
 
 def kebabize(s):
    return ''.join(c if c.islower() else '-' + c.lower() for c in s if c.isalpha()).strip('-')
