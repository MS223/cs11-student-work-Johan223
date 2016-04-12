# what does this function return ? This doesn't return anything back to the computer, the print is fr the people.
def print_only(x):
   y = x * 2
   print y

# how is this one different ? This doesn't show the people but it can be used for the computer.
def return_only(x):
   y = x * 2
   return y

# let's try to use our 2 functions
print "running print_only ..."
print_only(7)

print "running return_only ..."
return_only(7)

print "printing print_only ..."
print print_only(7)

print "printing return_only ..."
print return_only(7)

print "using print_only ..."
print_only(7) + 6

print "using return_only ..."
return_only(7) + 6
