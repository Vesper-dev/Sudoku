import pygame, sys, os
from fileLib import replaceChar, read, writeLines
from mixBoard import getBoard
from generateHTML import generateHTML
from solver import prompt, bruteforceSolve


#Tablice danych przedstawiające plansze Sudoku i jeje stan;
mainBoard = []#aktualne wartości prezentowane na planszy sudoku;
for i in range(9):
    mainBoard.append('000000000')
constBoard = mainBoard#przechowuje miejsca w tablicy których nie można zmienić;
solved = []
solved = mainBoard[:]

#Funkcje wykorzystywane przez program;
def lineSize(index):#Zwraca ile grubości lini doliczyć;
    if index//3 == 1: return 4
    if index//3 == 2: return 8
    return 0

def getChar(char):
    myFont = pygame.font.SysFont('monospace', 25)
    return myFont.render(char, 1, (0, 0, 0))

def blitSudokuBoard(window, tab):
    window.blit(gSudokuBoard, (150, 100))
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            x = 164 + lineSize(j) + 32 * j
            y = 108 + lineSize(i) + 32 * i
            if tab[i][j] == '0':
                window.blit(getChar(' '), (x, y))
            else:
                window.blit(getChar(tab[i][j]), (x, y))

def menuPanelEvent(mPos):
    menuPanel(mPos)
    gamePanel(mPos)
    
def menuPanel(mPos):
    global  isSelectedOption, selOptionPos, isMessage, messageType
    x, y = mPos
    if y >=5 and y <= 25:
        if x >= 5 and x <= 75:
            isSelectedOption = True
            selOptionPos = 5, 5
            print 'New'
            isMessage = True
            messageType = 0
        if x >= 85 and x <= 155:
            isSelectedOption = True
            selOptionPos = 85, 5
            print 'Load'
            loadBoard()
        if x >= 165 and x <= 235:
            isSelectedOption = True
            selOptionPos = 165, 5
            print 'Save'
            writeLines('Save/board.txt', mainBoard)
        if x >= 245 and x <= 315:
            isSelectedOption = True
            selOptionPos = 245, 5
            print 'Print'
            generateHTML(mainBoard, 'HTML/toPrint.html')

def loadBoard():
    global mainBoard, constBoard, solved
    mainBoard = read('Load/board.txt')
    for i in range(len(mainBoard)):
        for j in range(len(mainBoard[i])):
            if mainBoard[i][j] != '0':
                constBoard[i] = replaceChar(constBoard[i], j, '1')
            else:
                constBoard[i] = replaceChar(constBoard[i], j, '0')
    solved = bruteforceSolve(mainBoard)
    
def gamePanel(mPos):
    global  isSelectedOption, selOptionPos, mainBoard
    x, y = mPos
    if x >=525 and x <= 595:
        if y >= 105 and y <= 125:
            isSelectedOption = True
            selOptionPos = 525, 105
            print 'Prompt'
            prompt(mainBoard)
        if y >= 155 and y <= 175:
            isSelectedOption = True
            selOptionPos = 525, 155
            print 'Check'
            checkSudoku()
        if y >= 205 and y <= 225:
            isSelectedOption = True
            selOptionPos = 525, 205
            print 'Solve'
            mainBoard = solved

def checkSudoku():
    global isMessage, messageType
    global solved, mainBoard
    for i in range(9):
        for j in range(9):
            if mainBoard[i][j] != '0':
                if mainBoard[i][j] != solved[i][j]:
                    isMessage = True
                    messageType = 3
                    return
    isMessage = True
    messageType = 1

def isInField(i, j, pX, pY):
    global isSelectedField
    x = 156 + lineSize(j) + 32 * j
    y = 106 + lineSize(i) + 32 * i
    if pX >= x and pX <= x + 32:
        if pY >= y and pY <= y + 32:
            global selFieldPos, selIndexField
            selIndexField = i, j
            selFieldPos = x, y
            isSelectedField = True
            return True
    isSelectedField = False
    return False
    
def sudokuBoardEvent(mPos, tab):
    global isSelectedField, selFieldPos
    x, y = mPos
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if isInField(i, j, x, y) == True:
                print tab[i][j]
                return
            
def changeChar(event, board, constTab):
   tab = board
   if isSelectedField == True:
         i, j = selIndexField
         if constTab[i][j] != '1':
             pressed = event.key
             if pressed > pygame.K_0 and pressed <= pygame.K_9:
                tab[i] = replaceChar(board[i],j,str(event.key-48))
                return tab
   return board

def drawDeadField(window, position):
    window.blit(gConstField, position)

def addDeadField(window, tab):
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if tab[i][j] == '1':
                x = 156 + lineSize(j) + 32 * j
                y = 106 + lineSize(i) + 32 * i
                drawDeadField(window, (x, y))

def messageService(position):
    x, y=position
    if x>= 252 and x <398:
        if messageType == 0:
            difficultyService(position)
        if messageType == 1:
            correctService(position)
        if messageType == 2:
            successService(position)
        if messageType == 3:
            wrongService(position)

def difficultyService(position):
   x, y = position
   global isMessage
   global mainBoard
   if y>=177 and y<207:
      setNewBoard(1)
      isMessage = False
   if y>=209 and y<239:
      setNewBoard(2)
      isMessage = False
   if y>=241 and y<273:
      setNewBoard(4)
      isMessage = False
      
def setNewBoard(difficult):
    global mainBoard, constBoard, solved
    mainBoard = getBoard(difficult)
    for i in range(len(mainBoard)):
        for j in range(len(mainBoard[i])):
            if mainBoard[i][j] != '0':
                constBoard[i] = replaceChar(constBoard[i], j, '1')
            else:
                constBoard[i] = replaceChar(constBoard[i], j, '0')
    solved = bruteforceSolve(mainBoard)
                
def correctService(position):
   x, y = position
   global isMessage
   if y>=241 and y<273:
      isMessage = False

def successService(position):
   x, y = position
   global isMessage
   if y>=241 and y<273:
      isMessage = False

def wrongService(position):
   x, y = position
   global isMessage
   if y>=241 and y<273:
      isMessage = False

def displayMessage(window):
    if isMessage == True:
        position = 250, 175
        if messageType == 0:
            window.blit(gDifficulty, position)
        if messageType == 1:
            window.blit(gCorrect, position)
        if messageType == 2:
            window.blit(gSuccess, position)
        if messageType == 3:
            window.blit(gWrong, position)


#Główne okno gry;
pygame.init()
pygame.display.set_caption('Sudoku')
size = width, height = 600, 500
window = pygame.display.set_mode(size)
bgColour = 255, 255, 255

#Ładowanie plików graficznych do zmiennych;
gSudokuBoard = pygame.image.load('Graphics\Board.png')
gMenuPanel = pygame.image.load('Graphics\MainOptions.png')
gGamePanel = pygame.image.load('Graphics\GamePanel.png')
gSelectedField = pygame.image.load('Graphics\Selected.png')
gSelectedOption = pygame.image.load('Graphics\SelectedOption.png')
gConstField = pygame.image.load('Graphics\ConstField.png')
gDifficulty = pygame.image.load('Graphics\difficulti.png')
gCorrect = pygame.image.load('Graphics\correct.png')
gSuccess = pygame.image.load('Graphics\success.png')
gWrong = pygame.image.load('Graphics\wrong.png')

#Zmienne opisujące stan;
isSelectedOption = False
isSelectedField = False
isMessage = False

#Pozycje elementów graficznych;
selOptionPos = 0, 0
selFieldPos = 0, 0
selIndexField = 0, 0

#Zmienne dodatkowe;
messageType = 0

#Pętla główna okna;
while True:

#Pętla zdarzeń;
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if isMessage != True:
                menuPanelEvent(pygame.mouse.get_pos())
                sudokuBoardEvent(pygame.mouse.get_pos(), mainBoard)
            else:
                messageService(pygame.mouse.get_pos())
        if event.type == pygame.MOUSEBUTTONUP and isSelectedOption == True:
            isSelectedOption = False
        if event.type == pygame.KEYDOWN and isMessage == False:
            mainBoard = changeChar(event, mainBoard, constBoard)

#Rysowanie okna i jego elementów;
    window.fill(bgColour)
    blitSudokuBoard(window, mainBoard)
    window.blit(gMenuPanel, (0, 0))
    window.blit(gGamePanel, (520, 100))
    if isSelectedOption == True:
        window.blit(gSelectedOption, selOptionPos)
    if isSelectedField == True:
        window.blit(gSelectedField, selFieldPos)
    addDeadField(window, constBoard)
    if isSelectedField == True:
        window.blit(gSelectedField, selFieldPos)
    displayMessage(window)
    pygame.display.flip()


    
