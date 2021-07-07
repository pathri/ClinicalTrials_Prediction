:begin
Create Constraint On (node:AACT_Interventions_Drug) Assert node.id Is Unique;
:commit
Using Periodic Commit 10000 Load CSV  WITH HEADERS From 
"file:/sas/vidhya/CompoundDb4jV2/ClinicalTrials/AACT/Mar21/interventions_typeDrug_03_2021.csv" 
As line Create (c:AACT_Interventions_Drug{ id:line.id,
nct_id:line.nct_id,type:line.intervention_type,
intervention_name:line.name});