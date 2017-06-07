"""
Implement String#ipv4_address?, which should return true if given object is an IPv4 address 
- four numbers (0-255) separated by dots.
It should only accept addresses in canonical representation, so no leading 0s, spaces etc.
"""

def ipv4_address(address):
  import re
  for i in address.split('.'):
    if not i.isdigit():
      return False
  if re.match('^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$', address) != None:
       return True
  else:
    return False
    
#best decision:
from re import compile, match

REGEX = compile(r'((\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.){4}$')

def ipv4_address(address):
    # refactored thanks to @leonoverweel on CodeWars
    return bool(match(REGEX, address + '.')) 
