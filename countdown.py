number= input("countdown from what number?")
#Asking the user to input a number to start off with
for x in range(1,number + 1):
    #This is the range of the numbers that will be included in the countdown
    print number
    number = number - 1
    #It prints the number then sets a new number by subtracting 1
print "Boom!"
#prints out boom in the bottom
