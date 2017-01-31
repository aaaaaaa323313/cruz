import os
import sys
import math
import redis
import pickle

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
            key = key + item + '_'

    #print key
    if dict.has_key(key) == True:
        dict[key] += 1
    else:
        dict[key] = 1

for key in dict.keys():
    dict[key] = dict[key] / sum


pkl_globe_f = open('globe_f.pkl', 'rb')
globe_f     = pickle.load(pkl_globe_f)


for key in globe_f.keys():
    g_f = globe_f[key]
    if dict.has_key(key) == True:
        dict[key] = dict[key] * math.log(1.0/g_f + 0.01, 10)
    else:
        dict[key] = 0.0


file_name = os.path.basename(path)
file_name = file_name.split('.')[0]
file_name += ".pkl"

output = open(file_name, 'wb')
pickle.dump(dict, output)
output.close()


'''
num = len(dict.keys())
tup = sorted(dict.items(), key=lambda a:a[1], reverse = True)
cum = 0.0
for i in range(0, num):
    if tup[i][1] > 0*0.001:
        #print tup[i][0], '\t', tup[i][1]
        #r.set(tup[i][0], tup[i][1])
        #cum += tup[i][1]
        #print cum
'''

