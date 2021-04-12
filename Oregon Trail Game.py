import random
nameofMC = input("What is your name? ").capitalize()
def turn():
    days = 0
    maxdays = 15
    foodatbeginning = 10
    food = foodatbeginning
    while True:
        end_day = input("Do you want to end day? Y/Yes or N/No. ").capitalize()
        if end_day == "Y" and end_day != "N":
            days += 1
            print("Today is day", days)
            food = food - 1
            print("You have", food, "food left")
        if food == 0:
            print(nameofMC, "has died.")
            return False
        elif end_day == "N":
            days = days
            print("Today is day", days)
        if days >= maxdays:
            print("Congratulations", nameofMC, "you have surived.")
            return False
           
def objectivesurvival():
    print("Hello", nameofMC, "welcome to Objective: Survival")
    while True:
        if turn() == False:
            break
    action1 = []
    action2 = []

objectivesurvival()
#turn()
#food()
