action = raw_input("What would you like to do?")
day= raw_input("What day of the week?").lower()
To_Do = {
    "monday": [],
    "tuesday":[],
    "wednesday":[],
    "thursday":[],
    "friday":[],
    "saturday":[],
    "sunday":[],
}
print To_Do

def add():
    To_Do[day]= action.append()
# so far Ihave the action that has a prompt for the user to type in for what they will do and the day of the week , I just have to work on getting that information in the proper keys.
