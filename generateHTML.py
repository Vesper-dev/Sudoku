#!usr/bin/env python
from fileLib import *

def generateHTML(src, fName):
    htmlTemp=[]
    tempName = 'HTML/htmlTemp.html'
    htmlTemp=readOutSpace(tempName)
    
    for i in src:
        for j in i:
            for k in range(lenght(tempName)):
                if isField(htmlTemp[k]):
                    if j != '0':
                        htmlTemp[k] = insertChar(htmlTemp[k],20,j);
                    else:
                        htmlTemp[k] = insertChar(htmlTemp[k],20,' ');
                    break
    write(fName, htmlTemp)

def isField(string):
    if len(string) == 26:
        return 1
    else:
        return 0
    
