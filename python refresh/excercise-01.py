
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