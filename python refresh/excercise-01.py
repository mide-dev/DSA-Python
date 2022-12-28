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
    
    
is_multiple(21, 7)
is_multiple(10, 3)