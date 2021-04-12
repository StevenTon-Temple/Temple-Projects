import random
def turn():
    days = 0
    maxdays = 15
    while True:
        choice = input("Your choice? ")
        if choice == "yes":
            days += 1
            print(days)
        if days >= maxdays:
            break
def objectivesurvival():
    action1 = []
    action2 = []

nameofch = input("What is your name? ")
#objectivesurvival()
turn()
