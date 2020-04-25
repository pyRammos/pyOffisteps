import os
import time
from multiprocessing import Pool

from random import seed
from random import randint
def getPos(pos):
    oldpos=pos
    switcher={
        2:38,
        4:14,
        8:49,
        16:6,
        21:42,
        28:83,
        47:26,
        48:11,
        50:67,
        55:52,
        62:18,
        64:60,
        71:91,
        80:100,
        86:24,
        93:68,
        95:66,
        98:78
    }
    return switcher.get(pos, oldpos)

def thorwDice():
    value = randint(1,6)
    #print (value)
    return value

def playGame(itterations):
    pl1wins =0
    pl2wins =0
    pl3wins =0
    pl4wins =0
    runs =0
    start = time.time()
    for x in range(itterations):
        pl1=0
        pl2=0
        pl3=0
        pl4=0
        winner=False
        while not winner:
            runs += 1
            newpl1=getPos(pl1+thorwDice())
            if newpl1<=100:
                pl1=newpl1
            if (pl1==100):
                #print ("pl1 won")
                pl1wins = pl1wins +1
                winner=True
            newpl2 = getPos(pl2 + thorwDice())
            if newpl2<=100:
                pl2=newpl2
            if (pl2 == 100):
                #print("pl2 won")
                pl2wins = pl2wins +1
                winner = True
            newpl3 = getPos(pl3 + thorwDice())
            if newpl3<=100:
                pl3=newpl3
            if (pl3 == 100):
               # print("pl3 won")
                pl3wins = pl3wins +1
                winner = True
            newpl4 = getPos(pl4 + thorwDice())
            if newpl4<=100:
                pl4=newpl4
            if (pl4 == 100):
               # print("pl4 won")
                pl4wins = pl4wins +1
                winner = True
    end = time.time()
    print(f"pl1 Wins {pl1wins}")
    print(f"pl2 Wins {pl2wins}")
    print(f"pl3 Wins {pl3wins}")
    print(f"pl4 Wins {pl4wins}")
    #print (f"It took {end-start:.5f} seconds runs to calculate {itterations}, on an average of {itterations/(end-start):.5f} per second")
    print(f"It took {runs:,} turns to complete the {itterations} games. That is {runs / (end - start):.0f} turns per second")
    print ("------------------")

if __name__ == '__main__':
    with Pool(5) as p:
         p.map(playGame, [79995,79998,79997,80000,79996,79999,45000])


