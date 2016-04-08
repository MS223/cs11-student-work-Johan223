range= input('pick a range')
#This is what the number will range to
user_guess = input ('pick a number within that range')
#This is what the user guesses
score = 0
#This is the final score of the user with the amount of times they guessed
import random
#This imports a random number from the computer for the user to guess
ran_num = (random.randint(1,range))
#This is where the number is generated
while user_guess != ran_num:
    if user_guess < ran_num:
        #This is if the user guesses less than the number the computer had
       score= score + 1
        #This adds a point for the amount guessed
       print "mmm... guess a little higha "
       user_guess= input ('guess again')
    elif  user_guess > ran_num:
        #This is if the user guesses to high, they have to guess a little lower
       score = score + 1
        #This adds another point if they guess it wrong
       print "mmm...think smaller"
       user_guess= input ('guess again')
print "You go it!"
print "Fail score is " + str(score)
#This prints out the fail score of the user
