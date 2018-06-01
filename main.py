"""
To create an electronic pet.

Author: Yuhao Zhu
Version:
    20180601: Create an electronic pet that changes status every 5 minutes.
"""

import random
import threading
import time

# Two ways to change the status:
# 1. Every time when the timer changes, the three status changes also.
# 2. Every time when the user input something, change rate changes.

# Initialize the timer.
def the_timer():
    global timer, hours, status, hunger, health, happiness

    # Change time.
    hours += 1
    if hours > 23:
        hours = 0

    # Change status according to time.
    if hours == 0:
        status = "sleep"    # Stop activity and go to sleep.
    elif hours == 8 and status == "sleep":
        status = "letalone"    # Wake up from sleep.

    # Change index.
    if status == "letalone":
        hunger += 2
        happiness -= 1
    elif status == "sleep":
        hunger += 1
    elif status == "walk":
        hunger += 3
        health += 1
    elif status == "play":
        hunger += 3
        happiness += 1
    elif status == "feed":
        hunger -= 3
    elif status == "seedoctor":
        health += 4

    # Change index du to index.
    if hunger > 80 or hunger < 20:
        health -= 2
    if happiness < 20:
        health -= 1

    # Prevent values from overflowing.
    if hunger > 100:
        hunger = 100
    elif hunger < 0:
        hunger = 0
    if health > 100:
        health = 100
    elif health < 0:
        health = 0
    if happiness > 100:
        happiness = 100
    elif happiness < 0:
        happiness = 0
    
    timer = threading.Timer(5.0, the_timer)
    timer.start()

def print_status(hours, status, hunger, health, happiness):
    hunger_bar = "*" * int(hunger/2) + "-" * (50 - int(hunger/2))
    happiness_bar = "*" * int(happiness/2) + "-" * (50 - int(happiness/2))
    health_bar = "*" * int(health/2) + "-" * (50 - int(health/2))
    print("Current time: {} o'clock.".format(hours))
    print("My current status is: {}".format(status_sentence(status)))
    print("Happiness:   Sad {} Happy({:03})".format(happiness_bar, happiness))
    print("Hungry:     Full {} Hungry({:03})".format(hunger_bar, hunger))
    print("Health:     Sick {} Health({:03})".format(health_bar, health))
    print()

def status_sentence(status):
    if status == "sleep":
        return "I am sleeping..."
    elif status == "walk":
        return "I am walking..."
    elif status == "play":
        return "I am playing..."
    elif status == "feed":
        return "I am eating..."
    elif status == "seedoctor":
        return "I am seeing doctor..."
    elif status == "letalone":
        return "I am awake but doing nothing..."

"""
Some initialization and constant.
"""

hours = 0
hunger = random.randint(0, 100)
health = random.randint(0, 100)
happiness = random.randint(0, 100)
status = "sleep"
order = ""
welcome_words = """
My name is Tommy, a cute cat...
You can walk and play with me. You need also give me delicious food and take me to hospital in case of illness. You can also made me doing nothing...
Command:
1. walk
2. play
3. feed
4. seedoctor
5. letalone
6. status: check my status
7. bye
"""

# Initialize the flag.
flag_program = True

"""
The program!
"""
the_timer()

print(welcome_words)

while flag_program == True:
    command = input("You want:")
    if command == "walk":
        if status == "sleep":
            comfirm = input("Are you sure? It will make me unhappy! Type 'y' to confirm.")
            if comfirm == "y":
                print("I am walking...\n")
                status = command
                happiness -= 4
            else:
                print()
        else:
            print("I am walking...\n")
            status = command
    elif command == "play":
        if status == "sleep":
            comfirm = input("Are you sure? It will make me unhappy! Type 'y' to confirm.")
            if comfirm == "y":
                print("I am playing...\n")
                status = command
                happiness -= 4
            else:
                print()
        else:
            print("I am playing...\n")
            status = command
    elif command == "feed":
        if status == "sleep":
            comfirm = input("Are you sure? It will make me unhappy! Type 'y' to confirm.")
            if comfirm == "y":
                print("I am eating...\n")
                status = command
                happiness -= 4
            else:
                print()
        else:        
            print("I am playing...\n")
            status = command
    elif command == "seedoctor":
        if status == "sleep":
            comfirm = input("Are you sure? It will make me unhappy! Type 'y' to confirm.")
            if comfirm == "y":
                print("I am seeing doctor...\n")
                status = command
                happiness -= 4
            else:
                print()
        else:
            print("I am seeing doctor...\n")
            status = command
    elif command == "letalone":
        if status == "sleep":
            comfirm = input("Are you sure? It will make me unhappy! Type 'y' to confirm.")
            if comfirm == "y":
                print("I am awake but doing nothing...\n")
                status = command
                happiness -= 4
            else:
                print()
        else:       
            print("I am awake but doing nothing...\n")
            status = command
    elif command == "status":
        command = ""
        print_status(hours, status, hunger, health, happiness)
    elif command == "bye":
        command = ""
        print("Remember to see me! Bye!")
        timer.cancel()
        flag_program = False
    else:
        command = ""
        print("I cannot understand you.\n")