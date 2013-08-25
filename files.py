import os
import os.path
from . import settings

def is_file(filename):
	path = os.path.join(settings.SHARING_DIRECTORY,filename)
	return os.path.isfile(path)

def is_directory(filename):
	path = os.path.join(settings.SHARING_DIRECTORY,filename)
	return os.path.isdir(path)

def get_directory_contents(directory):
	contents = []
	realdir = os.path.join(settings.SHARING_DIRECTORY,directory)
	if len(realdir) > len(settings.SHARING_DIRECTORY) and \
	   realdir[0:len(settings.SHARING_DIRECTORY)] == settings.SHARING_DIRECTORY:
		if not isinstance(realdir,unicode):
			realdir = realdir.decode('utf-8',errors='replace')
		raw_contents = os.listdir(realdir)
		raw_contents.sort()
		contents = [{'name':x, 'path':os.path.join(directory,x),
		  'fullpath':os.path.join(realdir,x),
		  'isdir':os.path.isdir(os.path.join(realdir,x))} for x in raw_contents]
		contents.sort(key=lambda i:0 if i['isdir'] else 1)
	return contents

