import random
days = 0
maxdays = 30
def organtrail():
    while True:
        if choice == "yes":
            days +=1
            print(days)
        if days >= maxdays:
            break
nameofch = input("What is your name? ")
choice = input("Your choice? ")
