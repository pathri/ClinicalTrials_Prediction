**Pubchem and USPO Integration**

*Data to be Downloaded:*

-   CID-Patent.gz - Download CID-Patent.gz tar zile in the following FTP link of pubchem (ftp://[*ftp.ncbi.nlm.nih.gov/pubchem/Compound/Extras/*](http://ftp.ncbi.nlm.nih.gov/pubchem/Compound/Extras/))

-   full\_download.zip - Patent data from the [*https://ped.uspto.gov/peds/*](https://ped.uspto.gov/peds/) . In this link, choose **download all** option drop down Entire dataset xml button.

-   patents.tab.zip - Download all Synonyms for Patent ([*https://drive.google.com/file/d/1phRP9Zq\_KlD0vsHEKcIV6JYrgtF04Z2L/view?usp=sharing*](https://drive.google.com/file/d/1phRP9Zq_KlD0vsHEKcIV6JYrgtF04Z2L/view?usp=sharing) )

*Step 1 (Extracting and Formatting USPTO data from xml files to csv
files) :*

-   **full\_download.zip** has xml files from 1910-2020 of patent data Each xml file belongs to a year containing all patents applied in that year.

-   Parse all the xml files and store the data in .csv files with **lxmlparser.py and execute\_lxml.py** scripts

    -   Remember to change the directory as per tar file in execute\_lxml.py before executing

    -   Command : python3 execute\_lxml.py

    -   Input : full\_download.zip

    -   Output : 3 csv files with patent data **(**ALLPatents.csv , ALLPatentInventor.csv, ALLPatentApplicant.csv **)**

-   From ALLPatents.csv file retrieved only PatentNumber,PublicationNumber and ApplicationNumber along with the year (for easier grep) and store into new file with help of  ExtractNumUSPTO.py script.

    -   Command : python3 ExtractNumUSPTO.py

    -   Input : ALLPatents.csv

    -   Output : PubPatAppUSPTO.csv

-   Store all patent and publication numbers in pickles with help of GetPickles.py script

    -   Command : python3 GetPickels.py

    -   Input : PubPatAppUSPTO.csv

    -   Output : Pat.pickle, Pub.pickle

*Step 2 ( Formatting Compound IDs and Patent IDs from CID-Patent.gz ) :*

-   This is a listing of all patent identifiers linked to CIDs. It is a gzipped text file with CID, tab, and patent identifier on each line.

-   From CID-Patent File extract the MAPPING for only US Patents

    -   LC\_ALL=C fgrep 'US' CID-Patent &gt; CID-USPatent.txt

    -   sed -i -E 's/\\t/|/g' CID-USPatent.txt (change delimiter from \\t to |)

-   From CID-Patent get Unique PatentIDs with help of below linux commands:

    -   cut -d' ' -f2 CID-Patent &gt; PatentID.txt (To input tab in terminal use CTR+V+Tab )

    -   sort -us -o UniqPatent.txt PatentID.txt (UniqPatent.txt has Unique PatentIds)

    -   grep '\^US.\*\$' UniqPatent.txt &gt; US.txt ( US.txt has unique US patents)

<!-- -->

-   Classify patents from US.txt into 2 Patent Number/Publication Number and Others (Based on USPTO rules) with help of SeperateIDsPubchem.py script.

    -   Command : python3 SeperateIDsPubchem.py

    -   Input : US.txt

    -   Output : AllPatPubNumbersUSPubchem.txt, AllOthersUSPubchem.txt

*Step 3 ( Formatting Compound IDs and Patent IDs from patents.tab.zip )
:*

-   From patents.tab.gz grep US Patents with help of linux command

    -   Command : LC\_ALL=C fgrep 'US' patents.tab.gz &gt;&gt; USSyn.txt

-   USSyn.txt - File of synonymns of US Patents with a Unique Identifier (ID) seperating each set of Patent Synonyms

-   Using USSyn.txt get this pickles SynID.pickle, IDSyns.pickle with help of GetPickles1.py script

    -   Command : python3 GetPickles1.py

    -   Input : USSyn.txt

    -   Output : SynID.pickle, IDSyns.pickle

*Step 4 ( Mapping Patent Ids with USPTO patent information):*

-   For each patent in AllPatPubNumbersUSPubchem.txt, check whether it is present in Pat.pickle or pub.pickle with help CheckNumUSPTO.py script.

    -   Command : python3 CheckNumUSPTO.py

    -   Input : AllPatPubNumbersUSPubchem.txt

    -   Output: Found.csv, NotFound.csv

-   Repeat above step with below mentioned scripts:

    -   GetCheckSyn.py

    -   GetCheckSyn2.py

    -   GetCheckSyn3.py

    -   CheckNum1.py

-   MapFound.csv (Patent list which are mapped)

-   MapNotFound.csv (All patents which are not mapped)

*Step 5 (Pubchem Scrapping):*

-   For remaining not found patents, scrape data from pubchem REST API for MapNotFound.csv with help of PubChemScrape.py script

    -   Command : python3 PubChemScrape.py

    -   Output : FinalData.csv , FinalApplicant.csv, FinalInventor.csv, FinalNotFound.csv

-   Above 3 files has data related to Pubchem Patent information.

1.  Consider the entire USPTO data. (15889706 patent information available)

2.  Initially filtered the Pubchem Compounds which has US Patents. ( Actually 87,83,47,918 Compound - patent mappings are present . Out of these only 34,78,93,227 mappings has US patents Unique patents count : 8856475)

3.  Mapped the following US patent ID's to USPTO patent data.( Patents mapped with USPTO data : 7219928)

    a.  Mapping with Patent No or Publication No.

    b.  With help of Patent Synonyms

4.  Then, Scraped the data from Pubchem for the remaining unmapped patents to get the corresponding patent information. (what is the logic behind scraping, pubchem api or python web , elaborate in detail)\ (Patent mapped with Pubchem data : 1635140\ Patents not mapped with neither pubchem or uspto: 1407)

5.  Finally we are ready with patent information for the pubchem compounds. We excluded pubchem compounds which have 0 USPTO patent or pubchem patent.

    a.  Add details about uspto - pubchem mapping , ref intern report, chapter 2 bulleted section at the end, any api like ped’s used ?)

**Data into Neo4j:**

1.  Firstly loaded all the Compound related information into the database. Followed by USPTO patents and Pubchem patents.

2.  Relations between Compound and Pubchem patents are created based on the matching of compound Id and publication no. respectively.

3.  Relation between Compounds and USPTO patents are created based on the matching of compound id and publication no, patent no respectively.

Corresponding Nodes in Neo4j :

-   Patent\_Pubchem (1509237)

    -   pubchem\_patent\_publicationNo

    -   pubchem\_patent\_submissionDate

    -   pubchem\_patent\_grantedDate

    -   pubchem\_patent\_title

    -   pubchem\_patent\_inventor

    -   pubchem\_patent\_applicant

-   Patent\_USPTO (15889987)

    -   uspto\_patent\_filingDate

    -   uspto\_patent\_applicationNo

    -   uspto\_patent\_publicationDate

    -   uspto\_patent\_publicationNo

    -   uspto\_patent\_grantedDate

    -   uspto\_patent\_patentNo

    -   uspto\_patent\_statusDate

    -   uspto\_patent\_status

    -   uspto\_patent\_title

    -   uspto\_patent\_inventor

    -   uspto\_patent\_applicant

-   Compound\_Pubchem (19837025)

    -   pubchem\_compound\_id

    -   pubchem\_compound\_title

    -   pubchem\_compound\_inchikey

    -   pubchem\_compound\_smile

Relations :

-   has\_pubchem\_patent (17082334)

-   has\_uspto\_patent (162560023)
