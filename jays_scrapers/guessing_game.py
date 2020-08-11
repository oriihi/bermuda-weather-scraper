print ('Welcome to my game!\n')
print('Please guess an integer between 0 and a 100.\n')  
print("You'll be told if it was correct or not.\n")
print("if your first guess is within 10 you'll be told you're warm\n")
print("if your first guess is more than 10 away from correct you'll be told you're cold\n")
print('If your guess is incorrect guess again.\n')
print("you'll be told if you're getting warmer or colder.\n")
print("Continue guessing until you guess the correct number.\n")
print("You'll then be told how many guesses it took you, once you guess correctly\n")

import random
x = random.randint(1,100)
#print(x)


guesses = []

my_guess=int(input('Please make your guess--  '))

guesses.append(my_guess)

print(guesses)

if my_guess >100 or my_guess <1:
    print("Out of bounds!")
       
if abs(x-my_guess)>10:
    print('Cold!')
else:
    print('Warm!')


while guesses[0] != x:
    my_guess=int(input('Please make your guess--  '))
    guesses.append(my_guess)
    print(guesses)
    
    if my_guess >100 or my_guess<1:
        print("Out of bounds!")
        
        pass
    
    if my_guess==x:
        break
            
    else:
        if abs((x-guesses[-2]))>abs((x-guesses[-1])):
            print('Warmer!')
        else:
            print('Colder!')
            
   

print('You Win!')
print('It only took you-')
print (len(guesses))
print('guesses - Well done!')
