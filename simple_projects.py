#!/usr/bin/env python
# coding: utf-8

# In[1]:


#weight converter

weight = int(input('weight : '))
unit = input('(L)bs or (K)g : ')
if unit.upper() == "L":
    converted_weight = weight*0.45
    print(f"You are {converted_weight} kilos")
else:
    converted_weight = weight/0.45
    print(f"You are {converted_weight} pounds")


# In[4]:


#guess the number

secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count<guess_limit:
    guess = int(input("Guess the number:"))
    guess_count +=1
    if guess == secret_number:
        print("You won the game!")
        break
    else:
        print("Sorry, you lose!")


# In[6]:


#car game

command = ""
started  = False
while True:
    command = input(">").lower()
    if command == "start":
        if started:
            print("The car has already started!")
        else:
            started = True
            print("The car has started")
    elif command == "stop":
        if not started:
            print("The car has already stopped!")
        else:
            started = False
            print("The car has stopped")
    elif command == "help":
        print("""
start = To start the car
stop = To stop the car
quit = To quit the game
        """)
    elif command == "quit":
        break
    else:
        print("Sorry, I didn't understand that")


# In[ ]:


#To convert entered number into words

