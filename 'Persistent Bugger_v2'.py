"""
!!! Work only with Python2
Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.
For example:
 persistence(39) => 3  # Because 3*9 = 27, 2*7 = 14, 1*4=4
                       # and 4 has only one digit.
 persistence(999) => 4 # Because 9*9*9 = 729, 7*2*9 = 126,
                       # 1*2*6 = 12, and finally 1*2 = 2.
 persistence(4) => 0   # Because 4 is already a one-digit number.
"""

def persistence(n):
  class count():
    count=0
  if n < 10:
    return count.count
  def inner(n):
    sum=1
    for i in str(n):
      sum*=int(i)
    count.count+=1
    if len(str(sum)) >1:
      inner(sum)
    return count.count
  return inner(n)
  
print(persistence(39))
