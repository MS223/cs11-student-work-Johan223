import random

def mystery_function(x, y):
    random_number = random.randint(0,2) # What's the range of randoms?
    if random_number > 0: # What's the probability that random_number is greater than 0?
        z = x + y
    else:
        z = x * y
    result z
mystery_function(1, 2)
#When we run this code the return function doesn't print out the result, 
#but when the print code is put in it does print out the result, or the random number. You could only only know the result if you 
#put in the print code. 
#Also, the return function s not known to the person but te result can be use for the computer in other functions.
