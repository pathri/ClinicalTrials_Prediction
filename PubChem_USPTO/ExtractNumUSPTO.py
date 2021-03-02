import csv
fhand = open("/sas/vidhya/CompoundDb4jV2/USPTO/data/PubPatAppUSPTO.csv","w")
fName = "/sas/vidhya/CompoundDb4jV2/USPTO/data/ALLPatents.csv"
lines = open(fName)
lines = lines.read()
lines = lines.split("\n")
num = 0
skip = []
for x in range(0,len(lines)-1):
	row = lines[x].rstrip().split("|")
	if (len(row) != 9):
		skip.append(x+1)
	if x not in skip:
		appD = row[0]
		appNo = row[1]
		pubNo = row[3]
		patNo = row[5]
		record = pubNo + "|" + patNo + "|" + appNo + "|" + appD + "\n"
		fhand.write(record)
		num += 1	
		if (num%2000000 ==0):
			print(num)

print("No of lines:" + str(len(lines)))
print("last line"+lines[len(lines)-1])
print("skip" + str(len(skip)))
print("No Of Rows writtern to new file:" , num)
	
fhand.close()
