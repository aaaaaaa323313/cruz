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


dict = sorted(dict.items(), key=lambda a:a[1], reverse = True)
print dict[1:5]
