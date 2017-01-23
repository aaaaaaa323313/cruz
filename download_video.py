#!/usr/bin/python
import os
import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()

video_path = './videos/' + 'user_' + str(sys.argv[2]) + '/'
try:
    os.mkdir(video_path)
except:
    pass

lines = [x.strip() for x in lines]

for line in lines:
    if line.find('watch?') >= 0:
        cmd = 'youtube-dl -o ' + '\'' + video_path + '%(id)s.%(ext)s' + '\'' + ' ' + line
        print cmd
        os.system(cmd)


