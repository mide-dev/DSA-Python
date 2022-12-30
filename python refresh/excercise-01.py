
# EXCERCISE 01

# Write a short Python function, is_multiple(n, m), that takes two integer
# values and returns True if n is a multiple of m, that is, n = mi for some
# integer i, and False otherwise

# a mutiple is true if n divided by m gives remainder 0.
def is_multiple(n, m):
    if n % m == 0:
        print(f"{n} is a multiple of {m}")
        return True
    else:
       print(f"{n} is not a multiple of {m}")
       return False 
    
# is_multiple(21, 7)
# is_multiple(10, 3)

# Another way
def is_multiple(n,m):
    return n % m == 0

#########################################

# EXCERCISE 02

#Write a short Python function, is_even(k), that takes an integer value and
#returns True if k is even, and False otherwise. However, your function
#cannot use the multiplication, modulo, or division operators.

def is_even(k):
    if k % 2 == 0:
        print(f"{k} is even")
        return True
    print(f'{k} is not even')
    
# is_even(2)
# is_even(3)

# Another way
def is_even(k):
    return k % 2 == 0;

#########################################

# EXCERCISE 03  

# Write a short Python function, minmax(data), that takes a sequence of
# one or more numbers, and returns the smallest and largest numbers, in the
# form of a tuple of length two. Do not use the built-in functions min or
# max in implementing your solution

def minmax(data):
    # declare two variables to store min and max value
    # store their result as the first int in data
    min_number = max_number = data[0]
    
    for i in data:
        # get minimum number
        if i < min_number:
            min_number = i;
            
        # get maximum number
        if i > max_number:
            max_number = i;            
    print(min_number, max_number)
    return(min_number, max_number)

# test_list = [1,2,3,4,5,6,7,8,9]
# minmax(test_list)

#########################################

# EXCERCISE 04

#  Write a short Python function that takes a positive integer n and returns
#  the sum of the squares of all the positive integers smaller than n.

def sum_of_squares(n):
    result = 0
    for i in range(n + 1):
        result += i**2
    print(result)
    return result
        
# sum_of_squares(4)
# sum_of_squares(5)

#########################################

# EXCERCISE 05

# Give a single command that computes the sum from Exercise 04 rely-
# ing on Python’s comprehension syntax and the built-in sum function

sum_of_squares2 = lambda num : print(sum(num**2 for num in range(num + 1)))

# sum_of_squares2(4)
# sum_of_squares2(5)

#########################################

# EXCERCISE 06

#  Write a short Python function that takes a positive integer n and returns
#  the sum of the squares of all the odd positive integers smaller than n.

def sum_of_odd_squares(n):
    result = 0
    for i in range(n + 1):
        if i % 2 != 0:
            result += i**2
    print(result)
    return result

# sum_of_odd_squares(4)
# sum_of_odd_squares(5)

#########################################

# EXCERCISE 07

# Give a single command that computes the sum from Exercise R-1.6, rely
# ing on Python’s comprehension syntax and the built-in sum function.

sum_of_odd_squares2 = lambda n: print(sum(n**2 for n in range(n + 1) if n%2 != 0))

# sum_of_odd_squares2(4)
# sum_of_odd_squares2(5)

#########################################

# EXCERCISE 08

# Python allows negative integers to be used as indices into a sequence,
# such as a string. If string s has length n, and expression s[k] is used for in
# dex −n ≤ k < 0, what is the equivalent index j ≥ 0 such that s[j] references
# the same element?

# s = [1,2,3]
# k = -1
# print(s[k])

# j = len(s) - 1
# print(s[j])

#########################################

# EXCERCISE 09

# What parameters should be sent to the range constructor, to produce a
# range with values 50, 60, 70, 80?

# range1 = [i for i in range(50,81,10)]

#########################################

# EXCERCISE 10

# What parameters should be sent to the range constructor, to produce a
# range with values 8, 6, 4, 2, 0, −2, −4, −6, −8?
    
# range2 = [i for i in range(8,-9,-2)]

#########################################

# EXCERCISE 11

# Demonstrate how to use Python’s list comprehension syntax to produce
# the list [1, 2, 4, 8, 16, 32, 64, 128, 256].

# generateList = [pow(2,i) for i in range(9)]

#########################################

# EXCERCISE 12

#  Python’s random module includes a function choice(data) that returns a
# random element from a non-empty sequence. The random module includes
#  a more basic function randrange, with parameterization similar to
# the built-in range function, that return a random choice from the given
# range. Using only the randrange function, implement your own version
# of the choice function

import random

# my_list = ['bag','apple','orange','shoes','banana','rope','shell','snail','goat']

# print(f'using inbuilt choice method: {random.choice(my_list)}')

def my_choice(lst):
    list_length = len(lst)
    pick_random = random.randrange(0, list_length)
    return lst[pick_random]

# print(f'custom function: {my_choice(my_list)}')

#########################################

# EXCERCISE 13

#  Write a pseudo-code description of a function that reverses a list of n
# integers, so that the numbers are listed in the opposite order than they
# were before, and compare this method to an equivalent Python function
# for doing the same thing.

'''
This code reverses a list of any given integers

function list_reverse(user-input-list)
    take user-input-list and reverse its index i.e. user-input-list[::-1]
    return the result 
'''

def list_reverse(input_list):
    return input_list[::-1]

#########################################

# EXCERCISE 14

#  Write a short Python function that takes a sequence of integer values and
# determines if there is a distinct pair of numbers in the sequence whose
# product is odd.