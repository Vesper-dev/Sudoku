#!/usr/bin/env python

import random
from fileLib import replaceChar, read

def mixRow(board):
    if len(board) != 9:
        print('board must have 9 elements!!!')
    else:
        numSub = random.choice([0,1,2]) * 3
        for i in range(3):
            numRow1 = random.choice([0,1,2]) + numSub
            numRow2 = random.choice([0,1,2]) + numSub
            replaceRow(board, numRow1, numRow2)

def mixColumn(board):
    if len(board) != 9:
        print('board must have 9 elements!!!')
    else:
        numSub = random.choice([0,1,2]) * 3
        for i in range(3):
            numCol1 = random.choice([0,1,2]) + numSub
            numCol2 = random.choice([0,1,2]) + numSub
            replaceColumn(board, numCol1, numCol2)

def mixSubfieldColumn(board):
    for i in range(3):
        numSub = random.choice([0,1,2])
        numSub2 = random.choice([0,1,2])
        replaceSubfieldInColumn(board, numSub, numSub2)

def mixSubfieldRow(board):
    for i in range(3):
        numSub = random.choice([0,1,2])
        numSub2 = random.choice([0,1,2])
        replaceSubfieldInRow(board, numSub, numSub2)

def replaceColumn(tab, numC1, numC2):
    numC1*=2
    numC2*=2
    if argTest(len(tab[0]), numC1, numC2):
        print('Bad arguments')
    else:
        box=[]
        for i in range(len(tab)):
            box.append(tab[i][numC1])
            tab[i] = replaceChar(tab[i], numC1, tab[i][numC2])
            tab[i] = replaceChar(tab[i], numC2, box[i][0])

def replaceRow(tab, numR1, numR2):
    if argTest(len(tab), numR1, numR2):
        print('Bad arguments')
    else:
        box = tab[numR1]
        tab[numR1] = tab[numR2]
        tab[numR2] = box
    
def argTest(lenght, arg1, arg2):
    if lenght <= arg1 or lenght <= arg2:
        return 1
    if arg1 < 0 or arg2 < 0:
        return 1
    return 0
    
def replaceSubfieldInRow(tab, subR1, subR2):
    if argTest(len(tab)//3, subR1, subR2):
        print('Bad arguments')
    else:
        for i in range(3):
            replaceRow(tab, (subR1*3)+i, (subR2*3)+i)

def replaceSubfieldInColumn(tab, subC1, subC2):
    if argTest(len(tab)//3, subC1, subC2):
        print('Bad arguments')
    else:
        for i in range(3):
            replaceColumn(tab, (subC1*3)+i, (subC2*3)+i)

def generateBoard(board):
    numMixing = random.choice([1,2,3,4,5,6])
    for i in range(numMixing):
        mixRow(board)
        mixColumn(board)
        mixSubfieldRow(board)
        mixSubfieldColumn(board)
        
def addGap(board, difficultyLevel):
    pool=[0,1,2,3,4,5,6,7,8]
    for i in range(difficultyLevel*10):
        x = random.choice(pool)
        y = random.choice(pool)
        board[y] = replaceChar(board[y], x, '0')
        
def getBoard(difficultyLevel):
    board = []
    board = read('input.txt')
    generateBoard(board)
    addGap(board, difficultyLevel)
    return board
