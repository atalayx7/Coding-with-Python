"""
import os
import time
for dirpath, dirs, files in os.walk("C:\\Users\\Atalay\\Desktop\\New folder"):
	print(dirpath)
	time.sleep(2)
"""
"""

for birim in birimler:
	os.access('/path/to/folder', os.W_OK)

print(len(birimler))
"""


"""

with open ("letsdo.txt",'r') as f:
	f=f.readlines()

	for i in f:
		print()
"""
import string
import re
import os
import time
def isWritable(directory):
    try:
        temp_filename = "idunno"
        #count = 0
        filename = os.path.join(directory, temp_filename)
        while(os.path.exists(filename)):
            filename = "{}.{}".format(os.path.join(directory, temp_filename))
            #print("filename",filename)
            #count = count + 1
        f = open(filename,"w")
        f.close()
        os.remove(filename)

        return True
    except Exception as e:
        #print "{}".format(e)
        return False
#x="C:\Users\Atalay\Desktop\New folder\New folder (5)"
#directory = "C:\\Users\\Atalay\\Desktop\\New folder\\New folder (4)\\New folder (2)"

with open("something.txt","w") as nothing:
	for dirpath, dirs, files in os.walk("C:\\Users\\Atalay\\Desktop\\New folder"):
		x=dirpath.replace('\\','\\\\')
		#print(x)
		if (isWritable(x)):
			print("ACCESSIBLE!!!")
			print(x)
			print(len(x)*'-')
			nothing.writelines(x+'\n')
		#time.sleep(2)

	#elif not isWritable(x):
		#continue
	#	print(x,"NOT ACCESSIBLE")
	#if isWritable(x):
	#	print(x,"NOT ACCESSIBLE")

#isWritable("C:\\Users\\Atalay\\Desktop\\New folder\\New folder (4)\\New folder")