import os
for root, dirs, files in os.walk('E:\CodeZone', topdown=False):
    for name in files:
    	if name =='svn-git.log':
    		log = os.path.join(root, name)
        	print 'deleted ',log
        	os.remove(log)
    # for name in dirs:
        # os.rmdir(os.path.join(root, name))
