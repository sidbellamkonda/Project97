import random
print('Guess a number from 1 to 9')
guessCount=0
number=random.randint(1,9)
while guessCount<3:
    guess=int(input("Enter your guess: "))
    if(guess==number):
        print('That is correct!')
        break
    elif(guess>number and guess<10):
        print('Incorrect. The number is lower')
        guessCount+=1
    elif(guess<number and guess>0):
        print('Incorrect. The number is higher')
        guessCount+=1
    else:
        print('Error: try again')