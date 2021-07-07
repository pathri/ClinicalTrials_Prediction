SELECT activities.activity_id, activities.assay_id, activities.standard_value,
activities.type, activities.doc_id, 
compound_records.compound_name,
component_sequences.accession, docs.journal, assays.confidence_score
FROM chembl_27.activities
INNER JOIN chembl_27.docs on activities.doc_id= docs.doc_id  
INNER JOIN chembl_27.assays on assays.assay_id= activities.assay_id 
INNER JOIN chembl_27.target_components on target_components.tid= assays.tid
INNER JOIN chembl_27.component_sequences on component_sequences.component_id= target_components.component_id
INNER JOIN chembl_27.compound_records on activities.molregno= compound_records.molregno
where assays.confidence_score > 5 
and activities.standard_value is not null
and activities.standard_value != '>'
and assays.assay_type='B'

/*total count=22021601 => exported to chembl_pchemblexport_tid_confscore.csv
//sample row=[243164 1 11.999999999999998 'Inhibition' 11087
 '2,5-Diphenyl-thiazol-4-ol' 'Q02759' 'J. Med. Chem.' 8] */
