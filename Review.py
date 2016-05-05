def max_value(integer):
    for x in range(1,integer + 1):
        print x
max_value(8) # it counts off from1 to the number placed in here


def compare_lists(): # define the function compare_lists
    list1 = [4,5,15,11,23,42] # this is is list 1
    list2 = [1,8,7,16,7,35] #this is list 2
    for x in list1: #this checks every number in list 1
        if x > list2[list1.index(x)]:# This checks each number in the list and see if the number is bigger or smaller then the number in the other list
            print x #This prints the results
        else:
            print list2[list1.index(x)] #if the number is smaller then it takes the other number of the list to see if the number is bigger and prints out that number
compare_lists()

 
def swapping_stars(): # define swapping stars
    height = 6 #this is the height of the shape 
    width = 3 #this is the width of the shape
    for x in range (0, height): 
        if x % 2 == 1:
            print "- * " * width
        else:
            print '* - ' * width
swapping_stars()



