# ERRORS HANDLING
from collections.abc import Iterable



# GPA CALCULATOR
def GPA_calc():
    print( 'Welcome to the GPA calculator.' )
    print( 'Please enter all your letter grades, one per line.' )
    print( 'Enter a blank line to designate the end.' )
    # map from letter grade to point value
    points = {'A+' :4.0, 'A' :4.0, 'A-' :3.67, 'B+' :3.33, 'B':3.0, 'B-' :2.67,
    'C+' :2.33, 'C' :2.0, 'C' :1.67, 'D+' :1.33, 'D' :1.0, 'F' :0.0}

    num_courses = 0
    total_points = 0
    done = False
    while not done:
        grade = input('Enter grade:')   # read line from user
        if grade == '':     # empty line was entered    
            done = True
        elif grade not in points:    # unrecognized grade entered
            print(f'Unkown grade {grade} being ignored')
        else:
            num_courses += 1
            total_points += points[grade]
        if num_courses > 0: # avoid division by zero
            print( 'Your GPA is {0:.3}'.format(total_points / num_courses))
        
        

# sum of numbers
myList = [1,2,3,4,5,6,7,8,9];


def computeSum(values):
    if not isinstance(values, Iterable):
        raise TypeError('parameter must be an iterable type')
    
    total = 0
    for v in values:
        if not isinstance(v, (int, float)):
            raise TypeError('elements must be numeric')
        total += v
    print(f'total sum of numbers: {total}')
    return total


# try except 
def returnAge():
    age = -1

    while age <= 0:
        try:
            age = int(input('Enter your age in years:'))
            if age <= 0:
                print('Your age must be positive')
                break
            print(f"you're {age} years old!")
            
        except (ValueError, EOFError):
            print('invalid response')
            break
            
# generators and iterators
def factors(n):
    result = []
    for i in range(1,n+1):
        if n % i == 0:
            result.append(i)
    return result


            
def factors2(n):
    for i in range(1,n+1):
        if n % i == 0:
            yield i

       
# fibonacci with generators
def fibonacci():
    a = 0
    b = 1
    
    while a < 200:
        yield a
        future = a + b
        a = b
        b = future

# conditional 'for' expression    
squares = [i*i for i in range(10)]

# conditional 'if' expression    
def multiply(param):
    return param * 2

i = 3
twice = multiply(i if i % 2 == 0 else 0)

# tuple unpacking
# using the above fib example
def fibonacci2():
    a, b = 0, 1
    
    while a < 200:
        yield a
        a, b = b, a+b
        
