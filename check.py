#!/usr/bin/env python

def check(tab,char,x,y):
    if checkHorizontal(tab,char, y) != 0:
        if checkVertical(tab,char, x) != 0:
            if checkSubField(tab,char, x, y) != 0:
                return 1
    return 0

def checkHorizontal(tab,char, y):
    amount = tab[y].count(char)
    if amount != 0:
        #print('Horizontal fail')
        return 0
    else:
        return 1

def checkVertical(tab,char, x):
    amount = countVertical(tab,char, x)
    if amount != 0:
        #print('Vertical fail')
        return 0
    else:
        return 1

def countVertical(tab, char, x):
    amount = 0
    for i in range(len(tab)):
        if tab[i][x] == char:
            amount += 1
    return amount

def checkSubField(tab,char, x, y):
    mX = maxRange(x)
    mY = maxRange(y)
    for i in range(mY-3, mY):
        for j in range(mX-3, mX):
            if tab[i][j] == char:
                #print('Subfield fail')
                return 0
    return 1

def maxRange(y):
    if y < 3:
        return 3
    if y < 6:
        return 6
    return 9




