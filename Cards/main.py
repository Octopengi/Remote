#We playing cards here maaaaaan 
import classes as Class
import random

master = Class.GameMaster()

you = Class.Hand()

you.Draw(9)

you.ShowHand("liST")

you.PlayCard(random.randint(0, len(you.hand) - 1), True)