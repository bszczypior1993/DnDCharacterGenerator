import random
import math
from pprint import pprint
from prettytable import PrettyTable


# 6 abilities: strength, dexterity, constitution, intelligence, wisdom and charisma
# determine score of each by rolling 6-sided dice 4 times, record sum of top 3 rolls.
# hitpoints = 10 + constitution modifier
# constitution modifier = const - 10/2 and round down


# knowledge base
hitpoints = 10

table = PrettyTable(['race', 'subrace', 'strmodifier', 'dexmodifier', 'conmodifier', 'intmodifier', 'wismodifier', 'charmodifier'])
table.add_row(['Aasimar', 'Protector', None, None, None, None, 1, 2])
table.add_row(['Aasimar', 'Scourge', None, None, 1, None, None, 2])
table.add_row(['Aasimar', 'Fallen', 1, None, None, None, None, 2])
table.add_row(['Dragonborn', None, 2, None, None, None, None, 1])
table.add_row(['Dwarf', 'Hill', None, None, 2, None, 1, None])
table.add_row(['Dwarf', 'Mountain', 2, None, 2, None, None, None])
table.add_row(['Dwarf', 'Grey', 1, None, 2, None, None, None])
table.add_row(['Elf', 'High', None, 2, None, 1, None, None])
table.add_row(['Elf', 'Wood', None, 2, None, None, None, None])
table.add_row(['Elf', 'Dark', None, None, 2, None, None, 1])
table.add_row(['Elf', 'Eladrin', None, 2, None, 1, 1, None])
table.add_row(['Gnome', 'Forest', None, 1, None, 2, None, None])
table.add_row(['Gnome', 'Rock', None, None, 1, 2, None, None])
table.add_row(['Gnome', 'Deep', None, 1, None, 2, None, None])
table.add_row(['Goliath', None, 2, None, 1, None, None, None])
table.add_row(['Halfling', 'Lightfoot', None, 2, None, None, None, 1])
table.add_row(['Halfling', 'Stout', None, 2, 1, None, None, None])
table.add_row(['Halfling', 'Ghostwise', None, 2, None, None, 1, None])
table.add_row(['Human', 'Non-Varian', 1, 1, 1, 1, 1, 1])
table.add_row(['Human', 'Variant', None, None, None, None, None, None]) #remember to handle user selection
table.add_row(['Orc', None, 2, None, 1, -2, None, None])
table.add_row(['Tiefling', 'Feral', None, 2, None, 1, None, None])
table.add_row(['Tiefling', 'Devil Tongue', None, None, None, 1, None, 2])
table.add_row(['Tiefling', 'Winged', None, None, None, 1, None, 2])
table.add_row(['Tiefling', 'Hellfire', None, None, None, 1, None, 2])

print(table)

# 6-sided dice roller
def roll_dice():
    return random.randint(1, 6)

# calculates the sum of the top 3 dice rolls
def calculate_score():
    scorelist = []
    i = 0
    while i < 4:
        scorelist.append(roll_dice())
        i += 1
    scorelist.remove(min(scorelist))
    scoresum = sum(scorelist)
    return scoresum


#asks the user to pick the race
#must adjust to the new table
def ask_race():
    print(f"The 5e approved races are:")
    pprint(races)
    race = input("Which basic race would you like to use?\n").title()
    if race in races:
        if races[race] == []: #checks if the race is on the list
            return race
        else:
            subrace = input(f"Your chosen race is {race}. Which subrace would you like to use?\n").title() #user chooses subrace
            if subrace in races[race]: # checks if subrace is available
                return race, subrace
            else:
                print("Incorrect choice. Try again!")
    else:
        print("Incorrect choice. Try again!")

ask_race()




#must adjust to the new table
def calculate_stats():
    for key in abilitydict:
        abilitydict[key] = calculate_score()
    constmodifier = math.floor((abilitydict["constitution"] - 10) / 2)
    health = 10 + constmodifier
    abilitydict["health"] = health

  #  if race == "Dragonborn":
   #     abilitydict['strength'] += 2
    #    abilitydict['charisma'] += 1

        #elif race == "Dwarf":

    return abilitydict



#must adjust to the new table
def calculate_character():
    calculate_stats()

    print(f"""Congratulations! 
    You've successfully generated your new DnD character. 
    
    It's a {calculate_stats().race}.
    Here are your stats:
    Hitpoints: {abilitydict["health"]}
    Strength: {abilitydict["strength"]}
    Dexterity: {abilitydict["dexterity"]}
    Constitution: {abilitydict["constitution"]}
    Intelligence: {abilitydict["intelligence"]}
    Wisdom: {abilitydict["wisdom"]}
    Charisma: {abilitydict["charisma"]}""")
calculate_character()

#github commit owner test`