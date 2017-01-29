import os
import sys


path = str(sys.argv[1])
file = open(path)

for line in file.readlines():
    print line,
