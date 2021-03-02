import csv
import sys
import datetime
from py2neo import Graph

'''
create a connection with neo4j
'''


def create_connection_with_neo4j():
    # set up authentication parameters and connection
    global g
    g = Graph("http://localhost:7474/db/data/", auth=("neo4j", "test"))


# dictionary uniprot id to gene id
dict_uniprot_id_to_gene_id={}

# dictionary gene symbol to gene id
dict_gene_symbol_to_gene_id={}


def integrate_information_into_dict():
    """
    get all node ids from the database
    :return:
    """
    query = '''MATCH (n:%s) RETURN n.gene_id, n.uniProtIDs, n.geneSymbol'''
    query = query % ('CTDgene')
    results = g.run(query)

    for identifier, uniprot_ids, gene_symbol, in results:
        if not gene_symbol in dict_gene_symbol_to_gene_id:
            dict_gene_symbol_to_gene_id[gene_symbol]=set()
        dict_gene_symbol_to_gene_id[gene_symbol].add(identifier)

        if uniprot_ids:
            for uniprot_id in uniprot_ids:
                if not uniprot_id in dict_uniprot_id_to_gene_id:
                    dict_uniprot_id_to_gene_id[uniprot_id]=set()
                dict_uniprot_id_to_gene_id[uniprot_id].add(identifier)

    print('number of uniprot_ids in database', len(dict_uniprot_id_to_gene_id))
    print('number of gene symbol in database', len(dict_gene_symbol_to_gene_id))


def prepare_query(file_name,  second_label):
    cypher_file = open( 'cypher_protein.cypher', 'w', encoding='utf-8')
    query = '''Using Periodic Commit 10000 Load CSV  WITH HEADERS From "file:''' + path_of_directory + '''master_database_change/mapping_and_merging_into_hetionet/%s" As line FIELDTERMINATOR "\\t" MATCH (n:CTDgene{gene_id:line.ctd_gene_id}), (g:%s{identifier:line.protein_id}) Create (n)-[:equal_gene_protein}]->(g);\n'''
    query = query % ( file_name, second_label)
    cypher_file.write(query)



def get_all_proteins_and_map(label):
    """
    prepare files and write information into files
    :return:
    """

    # prepare files
    file_name =  'mapping_protein.csv'
    mapping_file = open(file_name, 'w', encoding='utf-8')
    csv_mapping = csv.writer(mapping_file, delimiter='\t')
    csv_mapping.writerow(['ctd_gene_id', 'protein_id'])

    prepare_query(file_name, label)


    not_mapping_file = open('not_mapped', 'w', encoding='utf-8')
    csv_not_mapping = csv.writer(not_mapping_file, delimiter='\t')
    csv_not_mapping.writerow(['id', 'name'])

    counter_mapper=0
    counter=0

    #  uniProtIDs
    query = '''MATCH (n:%s) RETURN n.identifier,  n.gene_name''' % label
    results = g.run(query)
    for uniprot_id, gene_symbol, in results:
        counter+=1
        if uniprot_id in dict_uniprot_id_to_gene_id:
            counter_mapper+=1
            for ctd_id in dict_uniprot_id_to_gene_id[uniprot_id]:
                csv_mapping.writerow([ctd_id,uniprot_id])
        elif type(gene_symbol)==str  and gene_symbol in dict_gene_symbol_to_gene_id:
            counter_mapper+=1
            for ctd_id in dict_gene_symbol_to_gene_id[gene_symbol]:
                csv_mapping.writerow([ctd_id,uniprot_id])
        elif type(gene_symbol)==list:
            mapped_symbol=False
            for symbol in gene_symbol:
                if symbol in dict_gene_symbol_to_gene_id:
                    mapped_symbol=True
                    for ctd_id in dict_gene_symbol_to_gene_id[symbol]:
                        csv_mapping.writerow([ctd_id, uniprot_id])
            if mapped_symbol:
                counter_mapper+=1
            else:
                csv_not_mapping.writerow([uniprot_id, gene_symbol])
        else:
            csv_not_mapping.writerow([uniprot_id,gene_symbol])
    print(counter,' total number')
    print('mapped ',counter_mapper)


def main():
    print(datetime.datetime.utcnow())

    global path_of_directory, director
    if len(sys.argv) > 1:
        path_of_directory = sys.argv[1]
    else:
        sys.exit('need a path adrecs-target and directory')

    print('##########################################################################')

    print(datetime.datetime.utcnow())
    print('create connection to neo4j')

    create_connection_with_neo4j()

    print('##########################################################################')

    print(datetime.datetime.utcnow())
    print('prepare for each label the files')

    print('##########################################################################')

    print(datetime.datetime.utcnow())
    print('get all proteins from database')

    integrate_information_into_dict()

    print('##########################################################################')

    print(datetime.datetime.utcnow())
    print('prepare file and write information of mapping in it')

    # with drugbank : Protein_DrugBank
    # with uniprot : Protein_Uniprot
    get_all_proteins_and_map('Protein_Uniprot')

    print('##########################################################################')

    print(datetime.datetime.utcnow())


if __name__ == "__main__":
    # execute only if run as a script
    main()
