"""
You need to write regex that will validate a password to make sure it meets the following criteria:

    At least six characters long
    contains a lowercase letter
    contains an uppercase letter
    contains a number

Valid passwords will only be alphanumeric characters.
"""

regex="^(?=.*?\d)(?=.*?[A-Z])(?=.*?[a-z])[A-Za-z\d]{6,}$"

#(?=.*?\d) Checks for atleast one digit
#(?=.*?[A-Z]) Atleast one uppercsae.
#(?=.*?[a-z]) Atleast one lowercase.
#[A-Za-z\d]{6,} Matches uppercase or lowercase or digit characters 6 or more times. This
# ensures that the match must have atleast 6 characters.
#https://stackoverflow.com/questions/28334506/match-password-with-python-regex
#https://regex101.com/r/aQ9vG2/1
