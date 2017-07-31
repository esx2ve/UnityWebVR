import shutil
import os 
import sys
import exceptions

print os.getcwd()
os.chdir(os.getcwd())

def rmtree(path_name):
	try:
		shutil.rmtree(path_name)
		print 'succesfully deleted ' + path_name
	except exceptions.OSError, e:
		print 'failed to delete ' + path_name
		pass

rmtree('./Out')
rmtree('./Library/il2cpp_cache')
rmtree('./Library/webgl_cache')
rmtree('./Temp/StagingArea/Data')

os.mkdir('./Out')
