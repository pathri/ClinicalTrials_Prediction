# ClinicalTrials_Prediction



This repo contains the source code for "Predicting Clinical Trial Outcomes Using Drug Bioactivities through Graph Database Integration and Ensemble Learning"

Artifacts:
    Data Integration of multiple heterogenous chemical databases to Neo4j.
    These databases are DrugBank, ChEMBL, AACT, CTD, and UniProt.

DataFusion: 
    Mapping across database and within a database 

Machine learning:
    Inhouse curated data extraction from the integrated data source, centered around ClinicalTrials, Compounds, Diseases and Targets
    Feature extraction for ML
    Model Training, paramter tuning with supervised algorithms and performance measures

**Pre-requisites for Neo4j DB Integration**: 

1. Neo4J-Community edition is installed ( We used 4.1.3 version of Unix distribution inside anaconda environment ).

2. Open neo4j_community/conf/neo4j.conf and change the following lines.

    1. Comment this line "dbms.directories.import=import"
    2. Change the value of this line "dbms.security.auth_enabled=true" to false.
    3. Change the value of this line "dbms.memory.heap.max_size=1G" to 70G
    4. Add this line "dbms.security.allow_csv_import_from_file_urls=true"

Now,to start the graph, open terminal and go to neo4j community folder and run the following command : ./bin/neo4j console 


**Note**:  

    The integrated data can be download from Figshare : https://doi.org/10.6084/m9.figshare.18631901     
    Copy the unzipped file to data folder of Neo4j (e.g. neo4j-community-4.1.3/data/databases)
