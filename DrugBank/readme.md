# DrugBank_to_Neo4j
This integrates all open source data of DrugBank into Neo4j.

Wishart DS, Feunang YD, Guo AC, Lo EJ, Marcu A, Grant JR, Sajed T, Johnson D, Li C, Sayeeda Z, Assempour N. DrugBank 5.0: a major update to the DrugBank database for 2018. Nucleic acids research. 2018 Jan 4;46(D1):D1074-82.

This populates DrugBank (https://www.drugbank.ca/downloads) into Neo4j, but first we transform the data to tsv files with 
https://github.com/dhimmel/drugbank/blob/gh-pages/parse.ipynb
with some changes, so that also more properties and relationships are extracted. The results are multiple tsv files and not only one.

After extracting the information of XML file, they must be combined with the information from the other DrugBank files. Also, the targets are validated with the UniProt identifier (https://github.com/ckoenigs/UniProt_to_Neo4j). The program needs information where the other DrugBank files are. Also, the generated csv files from the other program are in a dictionary.

The prepared program generates csv/tsv files to integrate the DrugBank information into neo4j. However, there are two possibilities:
1. if already a neo4j database exists, then use the script : script_to_start_program_and_integrate_into_neo4j.sh 
2. if there is no neo4j database, then with the neo4j-admin import tool the data can be integrated very fast. Use the script: script_with_import_tool.sh

This should have the form:

![er_diagram](https://github.com/ckoenigs/DrugBank_to_Neo4j/blob/master/drugbank_er.png)


The Compound has so many properties:

![er_diagram](https://github.com/ckoenigs/DrugBank_to_Neo4j/blob/master/drugbank_compound.png)

The Relationships have also some properties:

![er_diagram](https://github.com/ckoenigs/DrugBank_to_Neo4j/blob/master/drugbank_er_rela.png)

Link: https://github.com/ckoenigs/DrugBank_to_Neo4j
