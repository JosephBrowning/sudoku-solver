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

def solveConstraint(arr, solved):
    error = 0
    for row in range(9):
        for col in range(9):
            square = str(arr[row][col])
            if len(square) == 2:
                #unconfirmed square has only one possible, confirm it
                
                elimPossible(row,col,square[0],arr)

                # make it len 1
                arr[row][col] = int(square[0])

                solved = solved + 1
            elif len(square) < 1 or square == '0':
                error = 1
                return arr, solved, error
    return arr, solved, error

def Guess(prevSolved, solved, arr):
    originalSave = arr.copy()
    originalSolved = solved
    
    fails = 0
    guessIndex = giveGuessIndex(arr)
    square = str(arr[guessIndex[0]][guessIndex[1]])
    
    newSquare = square[0]+square[0]
    arr[guessIndex[0],guessIndex[1]] = int(newSquare)
    #start guessing
    while solved != 81:
        prevSolved = solved
        arr, solved, error = solveConstraint(arr, solved)
        #need to make it so the orignal save doesn't have the faulty guess
        #uhh mabye put call to guess here so that it doesn't have to do another iteration
        if error == 1:
            fails = fails +1
            solved = originalSolved
            prevSolved = -1
            badGuess = str(arr[guessIndex[0],guessIndex[1]])
            arr = originalSave.copy()
            guessSquare = str(arr[guessIndex[0],guessIndex[1]])
            newGuess = removeChar(guessSquare, guessSquare.find(badGuess[0]))

            if newGuess == '0':
                return arr, solved
            
            if fails >= len(guessSquare) - 1:
                return arr, solved
            
            arr[guessIndex[0],guessIndex[1]] = int(newGuess)
            
        if solved != prevSolved:
            continue
        
        arr, solved = Guess(prevSolved, solved, arr)

        if solved == 81:
            continue

        fails = fails + 1
        solved = originalSolved
        prevSolved = -1
        badGuess = str(arr[guessIndex[0],guessIndex[1]])
        arr = originalSave.copy()
        guessSquare = str(arr[guessIndex[0],guessIndex[1]])
        newGuess = removeChar(guessSquare, guessSquare.find(badGuess[0]))
        if newGuess == '0':
            return arr, solved
        if fails >= len(guessSquare) - 1:
            return arr, solved
        arr[guessIndex[0],guessIndex[1]] = int(newGuess)

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
    
def elimArea(rowBound, colBound, val, arr):
    # print(rowBound, colBound)
    for row in range(rowBound[0],rowBound[1]+1):
        for col in range(colBound[0],colBound[1]+1):
            squareCheck = str(arr[row,col])
            if squareCheck.endswith('0') and squareCheck.find(val) != -1:
                newSquare = removeChar(squareCheck, squareCheck.find(val))
                arr[row,col] = int(newSquare)

def elimPossible(row, col, val, arr):
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
    elimArea(bounds[0], bounds[1], val, arr)

if __name__ == '__main__':

    f = open("testhard.txt", 'r')

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

    #solve
    prevSolved = -1
    iterations = 0
    while solved != prevSolved:
        iterations = iterations + 1
        prevSolved = solved
        arr, solved, error = solveConstraint(arr, solved)
        if error == 1:
            print('invalid puzzle')
    arr, solved = Guess(prevSolved,solved, arr)
    print(arr)
    print('solved: ', solved)

