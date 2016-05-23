#!/usr/bin/env python

def lenght(fName):
    return len(open(fName, 'rU').readlines())


def read(fName):
    try:
        table=[]
        file = open(fName,'r')
        try:
            for x in range(lenght(fName)):
                table.append(file.readline())  
        finally:
            file.close()
        return table
    except IOError :
        print("Error: file: "+fName+" doesn't exist")
        return 1
    
def writeLines(fName, listOfRow):
    file = open(fName,'w')
    try:
        for i in listOfRow:
            if i[len(i)-1] != '\n':
                i+='\n'
            file.write(i)
            
                
    finally:
        file.close()

def write(fName, buffer):
    file = open(fName,'w')
    try:
        file.write(buffer)
    finally:
        file.close()
		
def insertChar(string, index, char):
    begin = string[0:index]
    end = string[index:]
    return begin + char + end

def replaceChar(string, index, char):
    begin = string[0:index]
    end = string[index+1:]
    return begin + char + end

def deleteSpace(board):
    for i in range(len(board)):
        board[i] = board[i].strip()
        board[i] = board[i].replace(' ','')

def addSpace(board):
    for i in range(len(board)):
        k=1
        for j in range(8):
            board[i] = insertChar(board[i],k,' ')
            k+=2
