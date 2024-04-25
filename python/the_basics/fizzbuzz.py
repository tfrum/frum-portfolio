# FizzBuzz is a classic programming problem meant to test some of your math knowledge.
# It's a great way to learn about arrays and math functions.
# Here's how it might be presented:

"""
    Given an integer from 1 to 100:
        If the integer is divisible by 3 print "fizz"
        If the integer is divisible by 5 print "buzz"
        If the integer is divisible by 3 and 5 print "fizzbuzz"
        Otherwise print the integer.

    Can you print this all on one line?
"""

# By using '[]' we can define a variable as an array in Python.
array = []

# A for-loop is going to be your go-to for this sort of problem.
# We use the modulo operator (%) to check if there's a remainder from the division.
# Remember that if a number is divisible by another there will be no remainder.
for i in range(1, 101): # Don't forget that we start counting at 0, not 1!
    if i % 3 == 0 and i % 5 == 0:
        array.append('fizzbuzz ') # For this solution we want to append the string to the array.
    elif i % 3 == 0:
        array.append('fizz')
    elif i % 5 == 0:
        array.append('buzz')
    else:
        array.append(i)

# This will print the solution on one line, but it also prints the formatting of a list:
print(array)

# This will print the solution on one line properly:
# You use a for loop to grab the values and add them to an empty variable in-order with join()
# You also use str() to convert the value to a string first, since numbers aren't strings.
joined_string = ' '.join(str(x) for x in array) # the ' ' there adds a space between the joined elements.
print(joined_string)

# But this code will print the solution line-by-line:
for string in array:
    print(string)