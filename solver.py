import numpy as np

f = open("testeasy20.txt", 'r')

solved = 0
puzzle = [ line.split() for line in f]
#print(puzzle)

arr = np.zeros([9,9], dtype= "i")
i = 0 
j = 0
possibleVals = '123456789'


def elimPossible(row, col, val):
    for i in range(9):
        pass
    pass

def printTest():
    print(arr)

#create solving matrix.
for i in range(9):
    for j in range(9):
        if puzzle[i][j] == '0':
            arr[i][j] =  possibleVals + '0'
        elif 0 < int(puzzle[i][j]) < 10 : 
            arr[i][j] = puzzle[i][j] + puzzle[i][j]
#print(arr)
print(str(arr[0][0])[0])
printTest()


#solve

while solved != 81:
    for i in range(9):
        for j in range(9):
            square = str(arr[i][j])
            if len(square) > 1:
                if square.endswith('0') == False and len(square) == 2:
                    #confirmed square found, now remove from possible, change len to 1 and add 1 to solved
                    pass
                if square.endswith('0') == True and len(square) == 2:
                    #unconfirmed square has only one possible, confirm it
                    pass
            
