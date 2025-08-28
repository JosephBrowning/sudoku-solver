import numpy as np

def giveGuessIndex(arr):
    tempAns = '1234567890'
    ans = (0,5)
    for row in range(9):
        for col in range(9):
            square = str(arr[row][col])
            if len(square) == 3 or len(square) == 2:
                ans = (row,col)
                return ans
            elif len(square) < len(tempAns) and len(square) >= 2:
                ans = (row,col)
    return ans

def Guess(iterations, prevSolved, solved, arr):
    originalSave = arr.copy()
    #find guess with smallest len
    #  min(arr, key=lambda x : len(str(x)))
    #  attempt = 
    guessIndex = giveGuessIndex(arr)
    square = str(arr[guessIndex[0]][guessIndex[1]])
    newSquare = removeChar(square,0)
    print(guessIndex, guessIndex[0], guessIndex[1])
    print(len(newSquare))
    printTest()
    print('solved:', solved)
    arr[guessIndex[0],guessIndex[1]] = int(newSquare)
    #start guessing
    while solved != 81:
        iterations = iterations + 1
        prevSolved = solved
        for row in range(9):
            for col in range(9):
                square = str(arr[row][col])
                if len(square) > 1:
                    if len(square) == 2:
                        #unconfirmed square has only one possible, confirm it
                        
                        elimPossible(row,col,square[0])

                        # make it len 1
                        arr[row][col] = int(square[0])

                        solved = solved + 1
                elif len(square) < 1:
                    #need to make it so the orignal save doesn't have the faulty guess
                    #uhh mabye put call to guess here so that it doesn't have to do another iteration
                    arr = originalSave

                    arr, solved = Guess(iterations, prevSolved, solved, arr)
                    return arr, solved
        if solved == prevSolved:
            arr, solved = Guess(iterations, prevSolved, solved, arr)
    return arr, solved

def removeChar(s ,index):
    return s[:index] + s[index+1:]

def getBounds(row, col):
    if 0 <= row <= 2:
        if 0 <= col <= 2:
            return [[0,2],[0,2]]
        elif 3 <= col <= 5:
            return [[0,2],[3,5]]
        elif 6 <= col <= 8:
            return [[0,2],[6,8]]
    elif 3 <= row <= 5:
        if 0 <= col <= 2:
            return [[3,5],[0,2]]
        elif 3 <= col <= 5:
            return [[3,5],[3,5]]
        elif 6 <= col <= 8:
            return [[3,5],[6,8]]
    elif 6 <= row <= 8:
        if 0 <= col <= 2:
            return [[6,8],[0,2]]
        elif 3 <= col <= 5:
            return [[6,8],[3,5]]
        elif 6 <= col <= 8:
            return [[6,8],[6,8]]
    
def elimArea(rowBound, colBound, val):
    # print(rowBound, colBound)
    for row in range(rowBound[0],rowBound[1]+1):
        for col in range(colBound[0],colBound[1]+1):
            squareCheck = str(arr[row,col])
            if squareCheck.endswith('0') and squareCheck.find(val) != -1:
                newSquare = removeChar(squareCheck, squareCheck.find(val))
                arr[row,col] = int(newSquare)

def elimPossible(row, col, val):
    square = str(arr[row,col])
    

    #check rows and colemns
    for i in range(9):
        rowCheck = str(arr[i,col])
        colCheck = str(arr[row,i])
        if rowCheck.endswith('0') and rowCheck.find(val) != -1:
            newSquare = removeChar(rowCheck,rowCheck.find(val))
            arr[i,col] = int(newSquare)
        if colCheck.endswith('0') and colCheck.find(val) != -1:
            newSquare = removeChar(colCheck,colCheck.find(val))
            arr[row,i] = int(newSquare)

    #check 3x3 areas
    bounds = getBounds(row, col)
    elimArea(bounds[0], bounds[1], val)

def printTest():
    print(arr)

if __name__ == '__main__':

    f = open("testmedium.txt", 'r')

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
    prevSolved = -1
    iterations = 0
    # while solved != 81:
    while solved != prevSolved:
        iterations = iterations + 1
        prevSolved = solved
        for row in range(9):
            for col in range(9):
                square = str(arr[row][col])
                if len(square) > 1:
                    if len(square) == 2:
                        #unconfirmed square has only one possible, confirm it
                        
                        elimPossible(row,col,square[0])

                        # make it len 1
                        arr[row][col] = int(square[0])

                        solved = solved + 1
                    # if square.endswith('0') == False and len(square) == 2:
                    #     #confirmed square found, now remove from possible, change len to 1 and add 1 to solved
                    #     elimPossible(row, col, square[0])

                    #     # make it len 1
                    #     arr[row][col] = int(square[0])
                        
                    #     solved = solved + 1
                    # if square.endswith('0') == True and len(square) == 2:
                    #     #unconfirmed square has only one possible, confirm it
                        
                    #     elimPossible(row,col,square[0])

                    #     # make it len 1
                    #     arr[row][col] = int(square[0])

                    #     solved = solved + 1

    # square = str(arr[7][1])
    # elimPossible(7,1,square[0])
    # arr[7][1] = int(square[0])
    printTest()
    print(solved)
    print(iterations)

    arr, solved = Guess(iterations,prevSolved,solved, arr)
    printTest()

