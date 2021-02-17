import math
effectiveness = {
    "electric":{
      "electric": 0.5,
      "fire": 1,
      "grass": 1,
      "water": 2,
      "stell":2
    },
    "fire":{
      "electric": 1,
      "fire": 0.5,
      "grass": 2,
      "water": 0.5,
      "stell":2
    },
    "grass":{
        "electric": 1,
        "fire": 0.5,
        "grass": 0.5,
        "water": 2,
        "stell":0.5
    },
    "water":{
        "electric": 0.5,
        "fire": 2,
        "grass": 0.5,
        "water": 0.5,
        "stell":2
    },
    "stell":{
        "electric": 0.5,
        "fire": 0.5,
        "grass": 2,
        "water": 0.5,
        "stell":0.5
    }
}

def calculate_damage(your_type, opponent_type, attack, defense):
    return math.ceil(50 * (attack / defense) * effectiveness[your_type][opponent_type]);
case = int(input())
for i in range (case):
    you,enemy,attack,defense=inpft().split(" ")
    print("case #%i: %s" %(i+1,calculate_damage(you,enemy,int(attack),int(defense))))
