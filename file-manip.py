import ntpath
import glob
import os

if ntpath.exists('C:/Users/Arvind/Desktop/Newfolder'):
	# print ntpath.walk('C:/Users/Arvind/Desktop/Newfolder')
	print 'here'


# print glob.glob('C:/Users/Arvind/Desktop/Newfolder/*.mp3');
dir = 'C:/Users/Arvind/Desktop/Newfolder/'
for x in glob.glob(dir + '*.mp3'):
	if ntpath.exists(x):
		print ntpath.rename(x, "test")

