
# ClinicalTrials data population into Neo4J

Latest version of dump in PostgreSQL format) is downloaded from from https://explorer.opentrials.net/data
the data is ecported to csv for all the tables using psql copy command as below:
    psql -U usersa -d DATABAS -c "Copy (Select * From conditions) To STDOUT With CSV HEADER DELIMITER ',';" > /sas/vidhya/conditions.csv


* [clinicaltrials.txt](https://github.com/ambf0632/CompoundDb4jML/blob/main/ClinicalTrials/clinicaltrials.txt) file contains the schema of ClinicalTrials database. This file is given as input to [clinicalTrialsDataToNeo4j()](https://github.com/ambf0632/CompoundDb4jML/blob/1c91c3e7e931b48ded625587bf262e073ab48f43/ClinicalTrials/integrating_clinicaltrials_with_neo4j.py#L27) function, so that our script only populates specified tables and columns of ClinicalTrials data that are mentioned in clinicaltrials.txt in Neo4J.
* Execution of [clinicialTrialsDataIntoNeo4J.py](https://github.com/ambf0632/CompoundDb4jML/blob/main/ClinicalTrials/clinicialTrialsDataIntoNeo4J.py) script gives clinicalTrialsData.cypher file as output.
* Execution of clinicalTrialsData.cypher will populate the ClinicalTrials data into Neo4J.
* Example as below:
     * cat clinicalTrailsData.cypher |  /..../neo4j-community-4.1.3/bin/cypher-shell -u username -p password -a bolt://localhost:7687 > cypher_output.txt



![image](https://user-images.githubusercontent.com/59961900/111308438-b117e080-8680-11eb-968a-294d61541c56.png)

