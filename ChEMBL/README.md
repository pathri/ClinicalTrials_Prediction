# ChEMBL data population into Neo4J
**Step-1**: Install MySql in your local system. And also Install py2neo using the command (sudo pip install py2neo).

**Step-2**: Download the [chembl_27_mysql.tar.gz ](http://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_27/) dump and load the dump file into MySQL in your local system.

**Step-3**: Run [convertToCSV.py](https://github.com/ambf0632/CompoundDb4jML/blob/main/ChEMBL/convertToCSV.py) file in the terminal. The script will create the CSV files with required columns. The required columns list should be in [schema_select_tables.txt](https://github.com/ambf0632/CompoundDb4jML/blob/main/ChEMBL/schema_select_tables.txt) file)

**Note**: Change the user, password and db according to your MySQL information.

**Step-4**: Change the directory path of csv files accordingly in [graphs.py](https://github.com/ambf0632/CompoundDb4jML/blob/main/ChEMBL/graphs.py) script before executing. Also make required changes for user and password which are mentioned at the end of file. 

**Step-5**: graphs.py files contains different function exportCSV - for exporting CSV data into neo4j ,combine_nodes() - for merging two different types of nodes into a single node based on their primary keys, relationships() for creating relations between different nodes. Run graphs.py file in your desktop in another terminal. After the execution of that file, the data we require is loaded into Neo4J as per the schema. exportCSV function can be used to export all the tables of chembl as nodes (eventhough they are not mentioned in the below schema diagram)

This is how we merged the nodes and how we formed relations among different nodes:
![alt text](https://github.com/ambf0632/compoundDB4j/blob/master/ChEMBL/chembl_diagram_with_Chembl_er_schema.png)

**Note**: running [graphs.py](https://github.com/ambf0632/CompoundDb4jML/blob/main/ChEMBL/graphs.py) file may take some time. This is because of huge number of records of ChEMBL and the imports happen with periodic execution of cypher queries
