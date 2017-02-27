import os
import sys
import pickle


def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

path = str(sys.argv[1])
file = open(path)

cnt  = 0
last_key = []


for line in file.readlines():
    line  = line.strip('\n')
    items = line.split(' ')

    image_id = items[0]
    key_set  = []

    key = ''
    for i in range(1, len(items)):
        if hasNumbers(items[i]) == False:
            key = key + items[i] + '_'
        else:
            key_set.append(key)
            key = ''

    if len(list(set(key_set).intersection(set(last_key)))) > 0:
        cnt += 1
    else:
        #print cnt
        last_key = key_set
        cnt = 0
        print image_id

