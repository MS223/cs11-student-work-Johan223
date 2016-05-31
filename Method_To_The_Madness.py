class Time(object): #this is the times that are defined in this funciton
 def __init__(self, hour, minute, second):
     self.hour = hour
     self.minute = minute
     self.second = second
 def __str__(self): #this is how the function will be printed out, with the semi colon and hour, min and second
    return str(self.hour) + ":" + str(self.minute) + ":" + str(self.second)

 def __add__(self, other): # this function adds the corresponding hour, minuet and second of each time, so that id oesn't add all the numbers, but instead adds the number by its placeent of time (hour,min,sec)
     return str(self.hour + other.hour) + ":" + str(self.minute + other.minute) + ":" +str(self.second + other.second)

#these are the times that I have chosen to add together
time1 = Time(7, 10, 4)
time2 = Time(12,45,9)
time3 = Time(10,21,3)
print time1 # first time
print time2 # second time
print time3 #third time
print " " #space in between
print time1 + time2 #time 1 and time 2 combined
print time1 + time3
print time2 + time3
