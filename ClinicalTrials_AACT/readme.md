
# ClinicalTrials - AACT data population into Neo4J
Tasneem A, Aberle L, Ananth H, Chakraborty S, Chiswell K, McCourt BJ, Pietrobon R. The database for aggregate analysis of ClinicalTrials. gov (AACT) and subsequent regrouping by clinical specialty. PloS one. 2012 Mar 16;7(3):e33677.

Clinical Trials dataset used is downloaded in pipe delimited falt file format. Data as on March 2021 can be downloaded from https://aact.ctti-clinicaltrials.org/static/exported_files/monthly/20210301_pipe-delimited-export.zip


AACT data comprises multiple tables as in schema : https://aact.ctti-clinicaltrials.org/static/documentation/aact_schema.png

In this study we make use of core information such as Studies, Interventions and Conditions. NCT_ID serves as an unique identifier to connect these tables

We join the tables based on NCT_ID (https://github.com/ambf0632/CompoundDb4jML/blob/main/ClinicalTrials_AACT/join_studies_conditions_interv_03_21.py)

We prepare cypher files to create nodes in Neo4j (cypher_createconditions, cypher_createintervention, cypher_createstudies)

Files with 'relation_' in names are used to create relations in Neo4j

  	* relation_studies => Creates relation between AACT_Studies and AACT_Interventions_Drug, AACT_Interventions_Drug and AACT_Condition
	* relation_trials_drugbank => Creates relation between AACT_Interventions_Drug -> Compound_DrugBank, Salt_DrugBank
	* relation_ctd_trials => Creates relation between AACT_Condition -> CTD_disease    

	


![image](https://user-images.githubusercontent.com/59961900/124712810-64049680-df1d-11eb-9b40-0e4013ead586.png)
