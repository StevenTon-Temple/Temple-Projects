import random
nameofch = input("What is your name? ") 
def turn():
    days = 0
    maxdays = 15
    while True:
        end_day = input("Do you want to end day Y/Yes or N/No ").capitalize()
        if end_day == "Y":
            days += 1
            print("Today is day", days)
        if days >= maxdays:
            break
def objectivesurvival():
    print("Hello", nameofch, "welcome to Objective: Survival")
    action1 = []
    action2 = []

objectivesurvival()
turn()
