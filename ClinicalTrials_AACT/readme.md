
# ClinicalTrials - AACT data population into Neo4J

Clinical Trials dataset used is downloaded in pipe delimited falt file format. Data as on March 2021 can be downloaded from https://aact.ctti-clinicaltrials.org/static/exported_files/monthly/20210301_pipe-delimited-export.zip


AACT data comprises multiple tables as in schema : https://aact.ctti-clinicaltrials.org/static/documentation/aact_schema.png

In this study we make use of core information such as Studies, Interventions and Conditions. NCT_ID serves as an unique identifier. 

We join the tables based on NCT_ID (https://github.com/ambf0632/CompoundDb4jML/blob/main/ClinicalTrials_AACT/join_studies_conditions_interv_03_21.py)

We prepare cypher files to create nodes in Neo4j (cypher_createconditions, cypher_createintervention, cypher_createstudies)

Files with 'relation_' in names are used to create relations in Neo4j

  	* relation_studies => Creates relation between AACT_Studies and AACT_Interventions_Drug, AACT_Interventions_Drug and AACT_Condition
	* relation_trials_drugbank => Creates relation between AACT_Interventions_Drug -> Compound_DrugBank, Salt_DrugBank
	* relation_ctd_trials => Creates relation between AACT_Condition -> CTD_disease    


