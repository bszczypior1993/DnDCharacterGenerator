import random
import math
from pprint import pprint


# 6 abilities: strength, dexterity, constitution, intelligence, wisdom and charisma
# determine score of each by rolling 6-sided dice 4 times, record sum of top 3 rolls.
# hitpoints = 10 + constitution modifier
# constitution modifier = const - 10/2 and round down


# knowledge base
hitpoints = 10
abilities = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]
races = {'Aasimar': ['Protector', 'Scourge', 'Fallen'],
         'Dragonborn': [],
         'Dwarf': ['Hill', 'Mountain', 'Grey'],
         'Elf':['High', 'Wood', 'Dark', 'Eladrin'],
         'Gnome': ['Forest', 'Rock', 'Deep'],
         'Goliath': [],
         'Halfling': ['Lightfoot', 'Stout', 'Ghostwise'],
         'Human': ['Non-variant', 'Variant'],
         'Orc': [],
         'Thiefling': ['Feral', 'Devil Tongue', 'Winged', 'Hellfire']
         }

abilitydict = dict.fromkeys(abilities, None)

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