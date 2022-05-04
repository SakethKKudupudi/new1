# #string concatenation( aka how to put strings together )
# #Suppose we want to create a string that says "subscribe to ____" this blanxk is going tobe youtuber
# youtuber = "Saketh"# some string variable

# #a few ways to do this 
# #first way 
# print("subscribe to "+youtuber) #here youtuber is concatenated to string 'subscribe to' by using "+"
# #OR
# print("subscribe to {}".format(youtuber)) # this code format is 'string {}'.format(youtuber)
# #OR
# #this is third method called F-string method. we can define an Fstring by just prepending an F in front of the string 
# print(f"subscribe to {youtuber}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb2: ") # Verb2 will be the name of the variable
famous_peron = input("Famous Person: ")
madlibs = f"Computer programming is {adj} !  it makes me so excited all the time because\
 I love to {verb1}. Stay hydrated and {verb2} like you are {famous_peron}!"

print(madlibs)