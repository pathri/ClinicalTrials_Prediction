
### Clinical Trials data population into Neo4J

For populating ClinicalTrails data into Neo4J, we need to execute [integrating_clinicaltrials_with_neo4j.py](https://github.com/ambf0632/CompoundDb4jML/blob/main/ClinicalTrials/integrating_clinicaltrials_with_neo4j.py) script.

The file [clinicaltrials.txt](https://github.com/ambf0632/CompoundDb4jML/blob/main/ClinicalTrials/clinicaltrials.txt) has the schema of the Clinical Trials database. This is given as an input to the clinicalTrialsDataToNeo4j() function which imports all the data as nodes in to neo4j.

Result of the above execute file is a cypher file which can be given 
