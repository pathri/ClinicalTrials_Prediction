#Script to Download Patent Data
#This Script can be used to extract any data from the xml file
#INPUT : MapNotFound.csv
#OUTPUT : FinalData.csv, FinalApplicant.csv,FinalInventor.csv, FinaNotFound.csv

import urllib.request
import xml.etree.ElementTree as ET
from url import *
import time
#patent = input("\nEnter Patent ID: ")

fhand = open ("/sas/vidhya/CompoundDb4jV2/USPTO/data/scrape/np.csv")
file4 = open ("/sas/vidhya/CompoundDb4jV2/USPTO/pubchem_scrape_data/data1/FinalNotFound.csv","a")

count = 1
parse_count = 0
not_parse = 0
start_time = time.time()
for line in fhand:

	if (count%10 == 0):
		print(str(count)+"	"+"Parsed  "+str(parse_count)+"	"+"not parsed  "+str(not_parse))
	if (count <= 0):  # till this value it ignores
		count = count +1 
		continue
	if (count > 30000 ): # till this value it scrapes
		print("stopped" + str(count))
		print("Parsed  "+str(parse_count))
		print("not parsed  "+str(not_parse))
		break

	#print ("Patents Parsed :",count)
	p = line.rstrip().split("|")
	PatN = p[1].rstrip().split("\t")
	if (len(PatN) > 1):
		syns = PatN[1].split()
		PatN = PatN[0]
	else:
		syns = PatN
		PatN = PatN[0]
	flag = 0
	syns.reverse()
	for patent in syns:
		url_name = url_patent_name(patent)
		url = "https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/patent/"+url_name+"/XML/?response_type=display"
		#url = "https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/patent/"+url_name+"/XML/?response_type=save&amp;response_basename=Patent_"+url_name
		try:
			s = urllib.request.urlopen(url)
			contents = s.read()
			file_name = "data/Patents_"+str(p[0])+".xml" 
			f = open(file_name, 'wb')
			f.write(contents)
			f.close()
		except:
			#print("Error 404  " + patent)
			continue  # 404 Not Found Error 

		flag = 1
		if (flag == 1):
			parse_count = parse_count + 1
			break	
	if (flag == 0):
		not_parse = not_parse + 1
		file4.write(line)
	count+=1

fhand.close()
file4.close()
print("--- %s seconds ---" % (time.time() - start_time))
