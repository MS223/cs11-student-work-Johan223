 def is_even (x): # this is a vairbale defined "is_even"
     if x % 2 == 0: # if this "x" can be dividoed by 2 without any remainder, 0,  then the number is even and the statement is true, other wise it's false 
         return 'true'
     else:
         if x % 2 == 1:
             return 'false'

def is_int(x):
    if x == int(x):
        return True
    else:
        return False
print is_int(6.7)
