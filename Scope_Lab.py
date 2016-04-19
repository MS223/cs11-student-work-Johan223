a = [1, 2, 4]
b = a
def update_list(a_list):
    a_list[3] = "yo"
    b = a_list[4]
    b = 100
my_list = [1, 2, 3, 4, 5]
update_list(my_list)
print my_list
#This first code shows that the the list for "my_list" will take the 4th number of the list which is first since it starts from 0, and replace it with 'yo'
var_1 = "kittens" # This is one variable, global
var_2 = "cookies" #This is the other variable, global
# input: a string
# output: a string
def my_function(my_favorite_things): #global function except 'my_favortie_things'
    song_lyrics = "rain drops on roses," #local
    combined_song = song_lyrics + my_favorite_things #local
    print combined_song
    #instead of 'return' put 'print' so that the human can see it
# input: a string
# output: a string
def my_function_2(item, item2): #global function except for 'item, item2'
    full_lyrics = item + "on " + item2 #local
    full_song = my_function(full_lyrics)#local
    print full_song
    #instead of 'return' put 'print' so that the human can see it
my_song = my_function_2(var_1, var_2)
var_1 = 'cat'
var_2 = 'dog'

def print_out_my_favorite(favorite_pet):
    if favorite_pet == var_1:
        print("My favorite pet is the cat.")
    elif favorite_pet == var_2: #This is changed to an else if statement
        print("My favorite pet is the dog.")
    var_2 = "cat"

print_out_my_favorite(var_1) #This prints out the first statement "My favorite pet is the cat."
print(var_2) #just prints out 'dog'

