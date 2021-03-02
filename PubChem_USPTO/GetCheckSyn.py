import pickle
import sys

#infile = str(sys.argv[1])
infile = "/sas/vidhya/CompoundDb4jV2/USPTO/data/AllOthersUSPubchem.txt"

pickle_in = open("/sas/vidhya/CompoundDb4jV2/USPTO/data/SynId.pickle","rb")
SynId = pickle.load(pickle_in)

pickle_in = open("/sas/vidhya/CompoundDb4jV2/USPTO/data/IdSyns.pickle","rb")
IdSyns = pickle.load(pickle_in)

pickle_in = open("/sas/vidhya/CompoundDb4jV2/USPTO/data/Pat.pickle","rb")
Pat = pickle.load(pickle_in)

pickle_in = open("/sas/vidhya/CompoundDb4jV2/USPTO/data/Pub.pickle","rb")
Pub = pickle.load(pickle_in)

fhand = open(infile)
a = 0
b =0
c =0
d = 0
file1 = open("/sas/vidhya/CompoundDb4jV2/USPTO/data/NotFound1.txt","a")
file2 = open("/sas/vidhya/CompoundDb4jV2/USPTO/data/Found1.txt","a")
cnt =0
for line in fhand:
	flag = 0
	cnt =cnt +1
	patnumlist = line.split("\t")
	patnum = patnumlist[1].rstrip()
	patid = patnum
	patnum = patnum.replace("-",'')
	if (patnum in SynId):
		ids = SynId[patnum]
	else :
		c = c +1
		file1.write(patid+"\n") #No synonym at all
		#print("Not Found :",patnum)
		continue
	synonyms = IdSyns[ids]
	#print(synonyms)
	for syn in synonyms:
		syn1 = syn[2:] #syn1 = without US(to check in Patents
		if (syn1 in Pat):
			file2.write(patid+"|"+syn1+"\n")
			flag = 1
			a = a + 1
			#print(patnum,syn1)
			break

		elif (syn in Pub):
			b = b + 1
			file2.write(patid+"|"+syn+"\n")
			flag = 1
			break

	if (flag == 0):
		d = d + 1
		file1.write(patid+"\t")
		for syn in synonyms:
			file1.write(syn+" ")
		file1.write("\n")
	if (cnt%10000000 ==0):
		print(cnt)

#print("total: "+len(fhand))

fhand.close()
file1.close()
file2.close()

print("Pat matching " + str(a))
print("Pub matching " + str(b))
print("No synonyms " + str(c))
print("Not found with synonyms " + str(d))
		
	 
