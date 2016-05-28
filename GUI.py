import pygame, sys, os

#Tablice danych przedstawiające plansze Sudoku i jeje stan;
mainBoard = []#aktualne wartości prezentowane na planszy sudoku;
for i in range(9):
    mainBoard.append('100010001')
constBoard = mainBoard#przechowuje miejsca w tablicy których nie można zmienić;

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
    global  isSelectedOption, selOptionPos
    x, y = mPos
    if y >=5 and y <= 25:
        if x >= 5 and x <= 75:
            isSelectedOption = True
            selOptionPos = 5, 5
            print 'New'
        if x >= 85 and x <= 155:
            isSelectedOption = True
            selOptionPos = 85, 5
            print 'Load'
        if x >= 165 and x <= 235:
            isSelectedOption = True
            selOptionPos = 165, 5
            print 'Save'
        if x >= 245 and x <= 315:
            isSelectedOption = True
            selOptionPos = 245, 5
            print 'Print'
            
def gamePanel(mPos):
    global  isSelectedOption, selOptionPos
    x, y = mPos
    if x >=525 and x <= 595:
        if y >= 105 and y <= 125:
            isSelectedOption = True
            selOptionPos = 525, 105
            print 'Prompt'
        if y >= 155 and y <= 175:
            isSelectedOption = True
            selOptionPos = 525, 155
            print 'Check'
        if y >= 205 and y <= 225:
            isSelectedOption = True
            selOptionPos = 525, 205
            print 'Solve'
    
def sudokuBoardEvent(mPos):
    pass

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
gSelectedOption =pygame.image.load('Graphics\SelectedOption.png')

#Zmienne opisujące stan;
isSelectedOption = False
isSelectedField = False

#Pozycje elementów graficznych;
selOptionPos = 0, 0
selFieldPos = 0, 0

#Pętla główna okna;
while True:

#Pętla zdarzeń;
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            menuPanelEvent(pygame.mouse.get_pos())
            sudokuBoardEvent(pygame.mouse.get_pos())
        if event.type == pygame.MOUSEBUTTONUP and isSelectedOption == True:
            isSelectedOption = False

#Rysowanie okna i jego elementów;
    window.fill(bgColour)
    blitSudokuBoard(window, mainBoard)
    window.blit(gMenuPanel, (0, 0))
    window.blit(gGamePanel, (520, 100))
    if isSelectedOption == True:
        window.blit(gSelectedOption, selOptionPos)
    if isSelectedField == True:
        window.blit(gSelectedField, selFieldPos)
    pygame.display.flip()


    
