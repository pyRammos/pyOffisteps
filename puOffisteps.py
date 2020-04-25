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
    mummywins =0
    daddywins =0
    zoewins =0
    lucaswins =0
    runs =0
    start = time.time()
    for x in range(itterations):
        mummy=0
        daddy=0
        zoe=0
        lucas=0
        winner=False
        while not winner:
            runs += 1
            newmummy=getPos(mummy+thorwDice())
            if newmummy<=100:
                mummy=newmummy
            if (mummy==100):
                #print ("mummy won")
                mummywins = mummywins +1
                winner=True
            newdaddy = getPos(daddy + thorwDice())
            if newdaddy<=100:
                daddy=newdaddy
            if (daddy == 100):
                #print("daddy won")
                daddywins = daddywins +1
                winner = True
            newzoe = getPos(zoe + thorwDice())
            if newzoe<=100:
                zoe=newzoe
            if (zoe == 100):
               # print("zoe won")
                zoewins = zoewins +1
                winner = True
            newlucas = getPos(lucas + thorwDice())
            if newlucas<=100:
                lucas=newlucas
            if (lucas == 100):
               # print("lucas won")
                lucaswins = lucaswins +1
                winner = True
    end = time.time()
    print(f"Mummy Wins {mummywins}")
    print(f"Daddy Wins {daddywins}")
    print(f"Zoe Wins {zoewins}")
    print(f"Lucas Wins {lucaswins}")
    #print (f"It took {end-start:.5f} seconds runs to calculate {itterations}, on an average of {itterations/(end-start):.5f} per second")
    print(f"It took {runs:,} turns to complete the {itterations} games. That is {runs / (end - start):.0f} turns per second")
    print ("------------------")

if __name__ == '__main__':
    with Pool(5) as p:
         p.map(playGame, [79995,79998,79997,80000,79996,79999,45000])


