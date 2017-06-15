"""
Write function scramble(str1,str2) that returns true if a portion of str1 characters can 
be rearranged to match str2, otherwise returns false.

For example:
str1 is 'rkqodlw' and str2 is 'world' the output should return true.
str1 is 'cedewaraaossoqqyt' and str2 is 'codewars' should return true.
str1 is 'katas' and str2 is 'steak' should return false.

Only lower case letters will be used (a-z). No punctuation or digits will be included.
Performance needs to be considered

Test.assert_equals(scramble('rkqodlw','world'),True)
Test.assert_equals(scramble('cedewaraaossoqqyt','codewars'),True)
Test.assert_equals(scramble('katas','steak'),False)
Test.assert_equals(scramble('scriptjava','javascript'),True)
Test.assert_equals(scramble('scriptingjava','javascript'),True)
"""

import itertools
def scramble(s1,s2):
    if s2 in [''.join(i) for i in itertools.permutations(s1, r=len(s2))]:
      return True
    else:
      return False
