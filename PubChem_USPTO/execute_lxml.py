import os
#change the directory as per uspto data tar file directory
for x in os.walk('//sas/vidhya/CompoundDb4jV2/USPTO/uspto_data'):
	cnt =0
	for filename in os.listdir(x[0]):
		if(filename.find('.xml') != -1):
			print(filename+"	"+str(cnt))
			#print(x[0][2:])
			command = "python3 lxmlparser.py " + "//" + x[0][2:] + " " + filename
			cnt = cnt + 1
			os.system(command)
