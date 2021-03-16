# CompoundDb4jML



This repo contains the source code for "Machine learning and bioinformatics models to predict the success of clinical trial with an integrated drug resource"

Artifacts:
    Data Integration of multiple heterogenous chemical databases to Neo4j.
    These databases are DrugBank, ChEMBL, CTD, NDFRT, UniProt Pubchem and USPTO.

DataFusion: 
    Mapping across database and within a database 

Machine learning:
    Inhouse curated data extraction from the integrated data source, centered around ClinicalTrials, Compounds, Diseases and Targets
    Feature extraction for ML
    Model Training, paramter tuning with supervised algorithms and performance measures

**Pre-requisites for Neo4j DB Integration**: 

1. Neo4J-Community edition is installed ( We used 4.1.3 version of Unix distribution inside anaconda environment ).

Then, Open neo4j_community/conf/neo4j.conf and change the following lines.

1. Comment this line "dbms.directories.import=import"
2. Change the value of this line "dbms.security.auth_enabled=true" to false.
3. Change the value of this line "dbms.memory.heap.max_size=1G" to 70G
4. Add this line "dbms.security.allow_csv_import_from_file_urls=true"

Now,to start the graph, open terminal and go to neo4j community folder and run the following command : ./bin/neo4j console 
