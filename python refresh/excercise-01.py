
# EXCERCISE 01

# Write a short Python function, is_multiple(n, m), that takes two integer
# values and returns True if n is a multiple of m, that is, n = mi for some
# integer i, and False otherwise

# a mutiple is true if n divided by m gives remainder 0.
import string
import random


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


def is_multiple(n, m):
    return n % m == 0

#########################################

# EXCERCISE 02

# Write a short Python function, is_even(k), that takes an integer value and
# returns True if k is even, and False otherwise. However, your function
# cannot use the multiplication, modulo, or division operators.


def is_even(k):
    if k % 2 == 0:
        print(f"{k} is even")
        return True
    print(f'{k} is not even')

# is_even(2)
# is_even(3)

# Another way


def is_even(k):
    return k % 2 == 0

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
            min_number = i

        # get maximum number
        if i > max_number:
            max_number = i
    print(min_number, max_number)
    return (min_number, max_number)

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


def sum_of_squares2(num): return print(sum(num**2 for num in range(num + 1)))

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


def sum_of_odd_squares2(n): return print(
    sum(n**2 for n in range(n + 1) if n % 2 != 0))

# sum_of_odd_squares2(4)
# sum_of_odd_squares2(5)

#########################################

# EXCERCISE 08

# Python allows negative integers to be used as indices into a sequence,
# such as a string. If string s has length n, and expression s[k] is used for in
# dex −n ≤ k < 0, what is the equivalent index j ≥ 0 such that s[j] references
# the same element?


s = [1, 2, 3]
k = -1
# print(s[k])

j = len(s) - 1
# print(s[j])

#########################################

# EXCERCISE 09

# What parameters should be sent to the range constructor, to produce a
# range with values 50, 60, 70, 80?

range1 = [i for i in range(50, 81, 10)]

#########################################

# EXCERCISE 10

# What parameters should be sent to the range constructor, to produce a
# range with values 8, 6, 4, 2, 0, −2, −4, −6, −8?

range2 = [i for i in range(8, -9, -2)]

#########################################

# EXCERCISE 11

# Demonstrate how to use Python’s list comprehension syntax to produce
# the list [1, 2, 4, 8, 16, 32, 64, 128, 256].

generateList = [pow(2, i) for i in range(9)]

#########################################

# EXCERCISE 12

#  Python’s random module includes a function choice(data) that returns a
# random element from a non-empty sequence. The random module includes
#  a more basic function randrange, with parameterization similar to
# the built-in range function, that return a random choice from the given
# range. Using only the randrange function, implement your own version
# of the choice function


my_list = ['bag', 'apple', 'orange', 'shoes',
           'banana', 'rope', 'shell', 'snail', 'goat']


def my_choice(lst):
    list_length = len(lst)
    pick_random = random.randrange(0, list_length)
    return lst[pick_random]

# print(f'using inbuilt choice method: {random.choice(my_list)}')
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


def detect_odd(lst):
    check_for_duplicates = []

    for num in lst:
        for val in lst:
            # prevent multiplying a number with itself
            if num == val:
                continue
            # calculate the product of every pair in the sequence
            product = num * val
            # check if product is odd
            if product % 2 != 0:
                # check if product as been added by a previous pair
                # to remove redundancy i.e. (1 * 3) is same as (3 * 1)
                if product in check_for_duplicates:
                    continue
                # if product is odd and there are no duplicates
                # store the product to check against future duplicate and print the result
                else:
                    check_for_duplicates.append(product)
                    print(f'{num} * {val} equals {product} which is odd')


seq = [1, 2, 9, 3, 4, 11, 7, 5]
# detect_odd(seq)

#########################################

# EXCERCISE 15

#  Write a Python function that takes a sequence of numbers and determines
# if all the numbers are different from each other (that is, they are distinct).


def is_distict(seq):
    if not isinstance(seq, list):
        seq = list(seq)

    return len(set(seq)) == len(seq)

#########################################

# EXCERCISE 16

#  In our implementation of the scale function (page 25), the body of the loop
# executes the command data[j] = factor. We have discussed that numeric
# types are immutable, and that use of the = operator in this context causes
# the creation of a new instance (not the mutation of an existing instance).
# How is it still possible, then, that our implementation of scale changes the
# actual parameter sent by the caller?

#########################################

# EXCERCISE 17

#  Had we implemented the scale function (page 25) as follows, does it work
# properly?
# def scale(data, factor):
# for val in data:
# val = factor
# Explain why or why not.

#########################################

# EXCERCISE 18

#  Demonstrate how to use Python’s list comprehension syntax to produce
# the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].


lst_comp = [num * (num+1) for num in range(10)]
# print(lst_comp)

#########################################

# EXCERCISE 19

# Demonstrate how to use Python’s list comprehension syntax to produce
# the list [ a , b , c , ..., z ], but without having to type all 26 such
# characters literally.


alphabet = [letter for letter in string.ascii_lowercase]
# print(alphabet)

#########################################

# EXCERCISE 20

#  Python’s random module includes a function shuffle(data) that accepts a
# list of elements and randomly reorders the elements so that each possible
# order occurs with equal probability. The random module includes a
# more basic function randint(a, b) that returns a uniformly random integer
# from a to b (including both endpoints). Using only the randint function,
# implement your own version of the shuffle function.


shuffle_test = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# random.shuffle(shuffle_test)
# list.sort(shuffle_test)


def shuffle(data):
    # store user input
    my_data = data
    shuffled_list = []
    # length of user list is greater than zero only if list still contains element(s)
    while len(my_data) != 0:
        # choose a random integer with respect to input list current length
        rand = random.randint(0, len(my_data) - 1)
        # use the random intger as index to pick an item on input list
        # append the item to shuffled list
        shuffled_list.append(my_data[rand])
        # remove the item from input list
        my_data.pop(rand)
    return shuffled_list

# print(shuffle(shuffle_test))

#########################################

# EXCERCISE 21

#  Write a Python program that repeatedly reads lines from standard input
# until an EOFError is raised, and then outputs those lines in reverse order
# (a user can indicate end of input by typing ctrl-D).


def revered_input():
    data = []
    try:
        while True:
            x = input()
            data.append(x)
            if x == '':
                break

    except EOFError:
        data = reversed(data)
        for i in data:
            print(i)

#########################################

# EXCERCISE 22

# Write a short Python program that takes two arrays a and b of length n
# storing int values, and returns the dot product of a and b. That is, it returns
# an array c of length n such that c[i] = a[i] · b[i], for i = 0,...,n−1.
