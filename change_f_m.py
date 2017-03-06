import os
import sys
import pickle


def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

path = str(sys.argv[1])
file = open(path)

cnt  = 1
last_key = ['first']
last_id  = ''



for line in file.readlines():
    line  = line.strip('\n')
    items = line.split(' ')

    image_id = (items[0])[0:11]
    key_set  = []

    key = ''
    for i in range(1, len(items)):
        if hasNumbers(items[i]) == False:
            key = key + items[i] + '_'
        else:
            key_set.append(key)
            key = ''

    if image_id != last_id:
        print last_key[0] + ' ' + str(cnt)
        print '\n'
        last_id  = image_id
        last_key = key_set
        cnt = 1
        print image_id
        continue

    if len(list(set(key_set).intersection(set(last_key)))) > 0:
        cnt += 1
    else:
        print last_key[0] + ' ' + str(cnt)
        last_key = key_set
        cnt = 1

