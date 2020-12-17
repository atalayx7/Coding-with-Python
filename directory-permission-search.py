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
	for dirpath, dirs, files in os.walk("C:\\Users\\aergen\\Desktop\\Yeni klasör (2)"):
		x=dirpath.replace('\\','\\\\')
		if "olmamalı" in x:
                    continue
		#print(x)
		elif (isWritable(x)):
			print("ACCESSIBLE!!!")
			print(x)
			print(len(x)*'-')
			nothing.writelines(x+'\n')
		#time.sleep(2)
