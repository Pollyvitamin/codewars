"""
You have to create a function that takes a positive integer number
and returns the next bigger number formed by the same digits:

next_bigger(12)==21
next_bigger(513)==531
next_bigger(2017)==2071

If no bigger number can be composed using those digits, return -1:

next_bigger(9)==-1
next_bigger(111)==-1
next_bigger(531)==-1
  
"""

import itertools
def next_bigger(n):
  possible_dig=sorted(set(["".join(i) for i in itertools.permutations(str(n))]))
  try:
    return int(possible_dig[(possible_dig.index(str(n))+1)])
  except:
    return -1
