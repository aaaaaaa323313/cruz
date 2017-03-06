import os
import sys
import math
import pickle

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

path = str(sys.argv[1])
file = open(path)

pkl_user_f = open('user_1.pkl', 'rb')
user_f     = pickle.load(pkl_user_f)

w = {}
i = 0

for line in file.readlines():
    line  = line.strip('\n')
    items = line.split(' ')
    p     = float(items[-1])

    key   = ''
    for item in items:
        if hasNumbers(item) == False and len(item) > 0:
            key = key + item + '_'

    p = 1
    w[i] = user_f[key] * p
    i += 1


v = {}

for i in range(3, len(w) - 3):
    v[i] = w[i] + 0.5*w[i-1] + 0.25*w[i-2] + 0.125*w[i-3]
    print v[i]
