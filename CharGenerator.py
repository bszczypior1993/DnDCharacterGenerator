import random
import math

# 6 abilities: strength, dexterity, constitution, intelligence, wisdom and charisma
# determine score of each by rolling 6-sided dice 4 times, record sum of top 3 rolls.
# hitpoints = 10 + constitution modifier
# constitution modifier = const - 10/2 and round down

hitpoints = 10
abilities = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]
abilitydict = dict.fromkeys(abilities, None)

def roll_dice():
    return random.randint(1, 6)

def calculate_score():
    scorelist = []
    i = 0
    while i < 4:
        scorelist.append(roll_dice())
        i += 1
    scorelist.remove(min(scorelist))
    scoresum = sum(scorelist)
    return scoresum

def calculate_character():
    for key in abilitydict:
        abilitydict[key] = calculate_score()
    constmodifier = math.floor((abilitydict["constitution"] - 10)/2)
    health = 10 + constmodifier
    abilitydict["health"] = health
    print(f"""Congratulations! 
    You've successfully generated your new DnD character. Here are your stats:
    Hitpoints: {abilitydict["health"]}
    Strength: {abilitydict["strength"]}
    Dexterity: {abilitydict["dexterity"]}
    Constitution: {abilitydict["constitution"]}
    Intelligence: {abilitydict["intelligence"]}
    Wisdom: {abilitydict["wisdom"]}
    Charisma: {abilitydict["charisma"]}""")
calculate_character()