import os
import sys
import pickle

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

path = str(sys.argv[1])
file = open(path)

cnt  = 0
last_key = ""


for line in file.readlines():
    items = line.split(' ')
    key   = ''
    for item in items:
        if hasNumbers(item) == False and len(item) > 0:
            key = key + item + '_'

    if key == last_key:
        cnt += 1
    else:
        print cnt
        last_key = key
        cnt = 0




