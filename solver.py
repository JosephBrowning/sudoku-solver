import numpy as np


def removeChar(s ,index):
    return s[:index] + s[index+1:]

def checkPosition(row, col):
    pass

def elimPossible(row, col, val):
    square = str(arr[row,col])
    for i in range(9):
        rowCheck = str(arr[i,col])
        colCheck = str(arr[row,i])
        if rowCheck.endswith('0') and rowCheck.find(val) != -1:
            newSquare = removeChar(rowCheck,rowCheck.find(val))
            arr[i,col] = int(newSquare)
        if colCheck.endswith('0') and colCheck.find(val) != -1:
            newSquare = removeChar(colCheck,colCheck.find(val))
            arr[row,i] = int(newSquare)
    

def printTest():
    print(arr)

if __name__ == '__main__':

    f = open("testeasy20.txt", 'r')

    solved = 0
    puzzle = [ line.split() for line in f]
    #print(puzzle)

    arr = np.zeros([9,9], dtype= "i")
    i = 0 
    j = 0
    possibleVals = '123456789'


    #create solving matrix.
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == '0':
                arr[i][j] =  possibleVals + '0'
            elif 0 < int(puzzle[i][j]) < 10 : 
                arr[i][j] = puzzle[i][j] + puzzle[i][j]
    #print(arr)
    print(str(arr[0][0])[0])
    #printTest()

    #solve

    while solved != 81:
        for row in range(9):
            for col in range(9):
                square = str(arr[i][j])
                if len(square) > 1:
                    if square.endswith('0') == False and len(square) == 2:
                        #confirmed square found, now remove from possible, change len to 1 and add 1 to solved
                        elimPossible(row, col, square[0])

                        # make it len 1
                        arr[i][j] = int(square[0])
                        
                        solved = solved + 1
                    if square.endswith('0') == True and len(square) == 2:
                        #unconfirmed square has only one possible, confirm it
                        
                        elimPossible(row,col,square[0])

                        # make it len 1
                        arr[i][j] = int(square[0])

                        solved = solved + 1

    printTest()
                
