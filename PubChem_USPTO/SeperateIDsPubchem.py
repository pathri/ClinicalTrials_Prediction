fh = open("/sas/vidhya/CompoundDb4jV2/USPTO/data/AllPatPubNumbersUSPubchem.txt","w")
#f = open("AllPubNumbersUSPubchem.txt","w")
hand = open("/sas/vidhya/CompoundDb4jV2/USPTO/data/AllOthersUSPubchem.txt","w")
fhand = open("/sas/vidhya/CompoundDb4jV2/USPTO/data/US.txt")
count = 1
for row in fhand:
	#print("no. ",count)
	pid = row.rstrip()
	if(len(pid)==11 or len(pid)==9):
		fh.write(pid + "\n")
	elif(len(pid)==13 or len(pid) == 15):
		fh.write(pid + "\n")
	else:
		hand.write(pid + "\n")
	count+=1
	if (count%10000000 == 0):
		print(count)
fhand.close()
fh.close()
#f.close()
hand.close()
		
		

