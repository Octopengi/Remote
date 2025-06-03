#Funcs 
import classes as Class
import random

def Distribute():
    suite = random.choices(["Diamond", "Heart", "Spade", "Club"])[0]
    rank = random.choices(["1", "2", "3", "4", "5", "6", "7", "8"])[0]
    return Class.Card(suite, rank)