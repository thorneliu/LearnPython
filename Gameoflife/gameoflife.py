import random, time

WorldLength = 14
WorldWidth  = 15

def Random0or1():
    return 1 if random.random() <= 0.5 else 0

LifeGrid = [[Random0or1() for col in range(WorldLength)] for row in range(WorldWidth)]

def LivesAroundMe(i, j):
    #return the Living cells around a given location(i,j)
    sum = 0
    for row in range(i-1, i+2):
        for col in range(j-1, j+2):
            if row in range(0, WorldWidth) and col in range(0, WorldLength):
                sum = sum + LifeGrid[row][col]
    return sum

def PrintLifeGrid():
    for row in LifeGrid:
        list = ['*' if i else ' ' for i in row]
        str = ' '.join(list)
        print str

def LifeChangeMode(i,j):
    neighbours = LivesAroundMe(i,j)
    if LifeGrid[i][j]:
        if neighbours < 2 or neighbours > 3:
            LifeGrid[i][j] = 0
    else:
        if neighbours == 3:
            LifeGrid[i][j] = 1

LifeCycle = 1
while LifeCycle <= 10:
    LifeCycle = LifeCycle + 1
    for row in range(0, WorldWidth):
        for col in range(0, WorldLength):
            LifeChangeMode(row, col)
    print "LifeCycle:\n", LifeCycle
    time.sleep(1)
    PrintLifeGrid()
