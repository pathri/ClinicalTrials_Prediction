
### Importing Clinical Trials to Neo4J and integrating with DrugBank

For importing and integrating clinical trails, the file integrating_clinicaltrails_with_neo4j.py has to be executed.

The file clinicaltrials.txt has the schema of the Clinical Trials database. This is given as an input to the exportCSV function which imports all the data as nodes in to neo4j.

After importing all the required nodes to Neo4j, for creating the relations between DrugBank and Clinical trials, cypher files are created by giving proper input to the function relationClinicalTrial. 

For this function, we have to input the files created after executing the file https://github.com/ambf0632/CompoundDb4jML/blob/main/DataFusion/C4jV2DataFusion_ClinTrials.ipynb.

Additionally, details like from table, to table, from attribute, to attribute are also given as input to generate the cypher files. On executing the integrating_clinicaltrails_with_neo4j.py, cypher file is generated with commands which creates relationship between 
- Salts of durgbank and clinicaltrails fda applications
- products of drugbank and clinicaltrails fda applications
- compounds of drugbank and clinicaltrails fda applications
