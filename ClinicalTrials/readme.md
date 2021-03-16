
# ClinicalTrials data population into Neo4J

* [clinicaltrials.txt](https://github.com/ambf0632/CompoundDb4jML/blob/main/ClinicalTrials/clinicaltrials.txt) file contains the schema of ClinicalTrials database. This file is given as input to [clinicalTrialsDataToNeo4j()](https://github.com/ambf0632/CompoundDb4jML/blob/1c91c3e7e931b48ded625587bf262e073ab48f43/ClinicalTrials/integrating_clinicaltrials_with_neo4j.py#L27) function, so that our script only populates specified tables and columns of ClinicalTrials data that are mentioned in clinicaltrials.txt in Neo4J.
* Execution of [clinicialTrialsDataIntoNeo4J.py](https://github.com/ambf0632/CompoundDb4jML/blob/main/ClinicalTrials/clinicialTrialsDataIntoNeo4J.py) script gives clinicalTrailsData.cypher file as output.
* Execution of clinicalTrailsData.cypher will populate the ClinicalTrials data into Neo4J.
* Terminal Command to execute clinicalTrailsData.cypher
     * cat clinicalTrailsData.cypher |  /..../neo4j-community-4.1.3/bin/cypher-shell -u username -p password -a bolt://localhost:7687 > cypher_output.txt
