:begin
Create Constraint On (node:AACT_Condition) Assert node.id Is Unique;
:commit
Using Periodic Commit 10000 Load CSV  WITH HEADERS From 
"file:/sas/vidhya/CompoundDb4jV2/ClinicalTrials/AACT/Mar21/conditions_03_2021.csv" 
As line Create (c:AACT_Condition{ id:line.id , nct_id:line.nct_id, 
condition_name:line.name,condition_downcasename:line.downcase_name});
