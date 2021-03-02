#Script to Download Patent Data
#This Script can be used to extract any data from the xml file
#INPUT : MapNotFound.csv
#OUTPUT : FinalData.csv, FinalApplicant.csv,FinalInventor.csv, FinaNotFound.csv

import urllib.request
import xml.etree.ElementTree as ET
from url import *
import time
import os.path
from os import path

infile = "/sas/vidhya/CompoundDb4jV2/USPTO/data/scrape/np.csv"
fhand = open(infile)
file = open ("/sas/vidhya/CompoundDb4jV2/USPTO/data/scrape/PubchemMapFound.csv","a")
file1 = open ("/sas/vidhya/CompoundDb4jV2/USPTO/data/scrape/PubchemData.csv","a")
file2 = open ("/sas/vidhya/CompoundDb4jV2/USPTO/data/scrape/PubchemApplicant.csv","a")
file3 = open ("/sas/vidhya/CompoundDb4jV2/USPTO/data/scrape/PubchemInventor.csv","a")
file4 = open ("/sas/vidhya/CompoundDb4jV2/USPTO/data/scrape/np.csv","a")

count = 0
nf = 0
np = 0
for line in fhand:
	count = count +1
	y = line.split('|')
	dirPath = "/sas/vidhya/CompoundDb4jV2/USPTO/pubchem_scrape_data/data/Patents_"+str(y[0])+".xml"
	x = path.exists(dirPath)
	if (x== True):
		try:
			tree = ET.parse(dirPath)
			root = tree.getroot()
		except:
			file4.write(str(count)+"|"+line.replace('\n','')+'\n')
			np = np + 1 
			continue

		subDate = 'NULL'
		grantDate = 'NULL'
		Title = 'NULL'
		Applicant = []
		Inventor = []

		Title = root.find('{http://pubchem.ncbi.nlm.nih.gov/pug_view}RecordTitle').text
		PatN = root.find('{http://pubchem.ncbi.nlm.nih.gov/pug_view}RecordAccession').text
		#patId= line.split("	")[0]
		patId = (y[1]).replace("\n",'')
		file.write(patId+"|"+PatN+"\n")
		for info in root.iter('{http://pubchem.ncbi.nlm.nih.gov/pug_view}Information'):
			subD = False
			grantD = False
			title = False
			app = False
			inv = False

			for name in info.findall('{http://pubchem.ncbi.nlm.nih.gov/pug_view}Name'):
				if (name.text == 'Filing Date'):
					subD = True
				elif (name.text == 'Grant Date'):
					grantD = True
				elif (name.text == 'Assignee'):
					app = True
				elif (name.text == 'Inventor'):
					inv = True

			i = info.find('{http://pubchem.ncbi.nlm.nih.gov/pug_view}Value')
			for value in i.iter():
				if (app and value.tag == "{http://pubchem.ncbi.nlm.nih.gov/pug_view}String"):
					Applicant.append(value.text)
						
				if (inv and value.tag == "{http://pubchem.ncbi.nlm.nih.gov/pug_view}String"):
					Inventor.append(value.text)

				if (grantD and value.tag == "{http://pubchem.ncbi.nlm.nih.gov/pug_view}DateISO8601"):
					grantDate = value.text

				if (subD and value.tag == "{http://pubchem.ncbi.nlm.nih.gov/pug_view}DateISO8601"):
					subDate = value.text

			record = PatN + "|" + subDate + "|" + grantDate + "|" + Title + "\n"
		file1.write(record)
		
		for name in Applicant:
			file2.write(PatN+"|"+name.strip()+"\n")
			
		for name in Inventor:
			file3.write(PatN+"|"+name.strip()+"\n")
		
	else :
		#file4.write(str(count)+"|"+line[-1])
		nf =nf + 1
	
	if (count%100 == 0):
		print(str(count)+"	np: "+str(np)+"    nf   "+str(nf))
		#break
	

fhand.close()
file.close()
file1.close()
file2.close()
file3.close()
file4.close()
