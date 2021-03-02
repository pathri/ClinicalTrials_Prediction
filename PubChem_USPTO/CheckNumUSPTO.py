import pickle

pickle_in = open("/sas/vidhya/CompoundDb4jV2/USPTO/data/Pat.pickle","rb")
Pat = pickle.load(pickle_in)

pickle_in = open("/sas/vidhya/CompoundDb4jV2/USPTO/data/Pub.pickle","rb")
Pub = pickle.load(pickle_in)

fhand1 = open("/sas/vidhya/CompoundDb4jV2/USPTO/data/AllPatPubNumbersUSPubchem.txt")
#fhand1 = open("AllPubNumbersUSPubchem.txt")
file1 = open("/sas/vidhya/CompoundDb4jV2/USPTO/data/Found.txt","w")
file2 = open("/sas/vidhya/CompoundDb4jV2/USPTO/data/NotFound.txt","w")
#file1 = open("PubFound.txt","w")
#file2 = open("PubNotFound.txt","w")
count = 1
#file1.write(str(Pub))
#file2.write(str(Pat))
a = 0
b =0
c = 0
for patnum in fhand1:
	x = patnum.split("	")
	patnum = x[1].rstrip()
	patn = patnum[2:]  #removing US for patentNumbers
	if (patn in Pat):
		a = a+1
		file1.write(patnum+"|"+patn+"\n")
	elif(patnum in Pub):
		b =b +1
		file1.write(patnum+"|"+patnum+"\n")
	else:
		c =c +1
		file2.write(patnum+"\n")
	count += 1
	if (count%2000000 ==0):
		print(count)

print("pat found   "+str(a))
print("pub found   "+str(b))
print("not found   "+str(c))
#fhand.close()
fhand1.close()
file1.close()
file2.close()

