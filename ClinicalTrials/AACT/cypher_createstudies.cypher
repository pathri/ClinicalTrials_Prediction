:begin
Create Constraint On (node:AACT_Studies) Assert node.nct_id Is Unique;
:commit
Using Periodic Commit 10000 Load CSV  WITH HEADERS From 
"file:/sas/vidhya/CompoundDb4jV2/ClinicalTrials/AACT/Mar21/studies_03_2021_nctonly.csv" 
As line Create (c:AACT_Studies{ nct_id:line.nct_id,
completion_date:line.completion_date,status:line.overall_status,
phase:line.phase});