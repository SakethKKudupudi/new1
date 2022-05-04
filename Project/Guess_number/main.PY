import random  
#when ever we call random it goes to the python package- https://docs.python.org/3/library/random.html
#we will first define a function guess
def guess(x): 
    # x is a parameter that we can pass thatinto this random get number function

    random_number = random.randint(1,x)

    #once the computer has random number, we guess in terminal and input what guess of our number is 
    # and the computer will tell us weither it's too high or too low
    #or if we guessed the number correctly we need to keep looping until we get the right answer
    #since we dont have a predefined universe to iterate over, we are useinf while loop
    #while(expression): #we want to stop the loop when our guess number is equal to the random number generated 
    # from
    
    #while guess != random_number:
    # #we need to actually define this guess and we're not going to make a guess up here because were 
    # just trying to initialize the variable tell python that this variable exists so that we can go back and 
    # change it later

    guess=0 
    
    #If our guest guesses the number as 0 then it is an erroe since number lies in between 1 to x

    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}'))
        print(guess)

    guess(10)   # call our function guest at the bottom of our script
