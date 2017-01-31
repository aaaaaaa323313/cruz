import os
import sys

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

path = str(sys.argv[1])
file = open(path)

dict = {}
sum  = 0.0

for line in file.readlines():
    sum += 1
    items = line.split(' ')
    key   = ''
    for item in items:
        if hasNumbers(item) == False and len(item) > 0:
            key = key + item + ' '

    #print key
    if dict.has_key(key) == True:
        dict[key] += 1
    else:
        dict[key] = 1

for key in dict.keys():
    dict[key] = dict[key] / sum


tup = sorted(dict.items(), key=lambda a:a[1], reverse = True)


cum = 0.0
for i in range(0,365):
    if tup[i][1] > 1*0.001:
        print tup[i][0] #'\t', tup[i][1]
        cum += tup[i][1]
        #print cum



