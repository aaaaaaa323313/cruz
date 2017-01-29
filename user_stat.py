import os
import sys

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

path = str(sys.argv[1])
file = open(path)

dict = {}

for line in file.readlines():
    items = line.split(' ')
    key   = ''
    for item in items:
        if hasNumbers(item) == False and len(item) > 0:
            key = key + item + ' '

    #print key
    if dict.haskey(key) == True:
        dict[key] += 1
    else:
        dict[key] = 1


