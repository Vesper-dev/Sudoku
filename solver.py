import random
from check import check
from fileLib import read, writeLines, replaceChar, addSpace, deleteSpace

tab=[]
tab=read('3.txt')
deleteSpace(tab)

def possibilityTab(board):
    cTab=[]
    for i in range(9):
        cTab.append([])
        for j in range(9):
            cTab[i].append([])
            
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == '0':
                for l in range(9):
                    if check(board, str(l+1),j,i) == 1:
                        cTab[i][j].append(str(l+1))
    return cTab

def newBoardSolved(board, possibTab):
    solved=[]
    for i in range(9):
        solved.append('')


    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] >='1' and board[i][j] <='9':
                solved[i]+=board[i][j]
            else:
                if len(possibTab[i][j]) == 1:
                    solved[i]+=possibTab[i][j][0]
                else:
                    solved[i]+='0'
    return solved

def isSolved(board):
    for i in board:
        if i.count('0') > 0:
            return False
    return True

def heuristicSolving(board):
    tab = []
    tab=board
    test=[]
    while True:
        if test == tab: break
        if isSolved(tab): break
        test = tab
        tab=newBoardSolved(tab, possibilityTab(tab))
    return tab

def bruteforceSolvin(board):
    tab=[]
    tab = heuristicSolving(board)
    cTab=[]
    for i in range(9):
        cTab.append([])
        for j in range(9):
            cTab[i].append([])
    cTab = possibilityTab(tab)
    tab = setValues(cTab, tab, 0, 0, 9, 9)
    return tab

iter=0
def setValues(cTab, tab, x, y, ex, ey):
    newTab = []
    newTab = tab
    coX=0
    coY=0
    for i in range(y, ey):
        for j in range(x, ex):
            if newTab[i][j] == '0':
                box=[]
                for k in range(len(cTab[i][j])):
                    char = random.choice(cTab[i][j])
                    cTab[i][j].remove(char)
                    box.append(char)
                    if check(tab,char,j,i) == 1:
                        newTab[i]=replaceChar(newTab[i], j, char)
                        coX=j
                        coY=i
                if newTab[i][j] != '0':
                    setValues(cTab, newTab, coX, coY, j, i)
                    cTab[i][j]=box
    return newTab
                

s=[]
s=bruteforceSolvin(tab)
addSpace(s)
for i in s:
    print(i)
