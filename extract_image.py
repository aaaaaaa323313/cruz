import os
import sys

path = str(sys.argv[1])

for f in os.listdir(path):
    file_path = os.path.join(path, f)
    if os.path.isfile(file_path):
        print f
        f_name, _ = f.split('.')
        image_path = os.path.join(path, f_name)
	try:
        	os.mkdir(image_path)
	except:
		print 'The dictionary exists'
                continue

        cmd = "/home/zhz/bin/ffmpeg -i " + file_path + " -vf fps=0.2 " + image_path + '/' + f_name + "_" + "%04d.jpg -hide_banner"
        print cmd
        os.system(cmd)

