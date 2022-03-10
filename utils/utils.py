import os

def readFile(fileName):
    files = open(fileName, 'r+')
    arr = []
    for line in files:
        arr.append(line[:-1])
    files.close()
    return arr


def writeFile(fileName, content):
    with open(fileName, 'a') as f1:
        f1.write(content + os.linesep)