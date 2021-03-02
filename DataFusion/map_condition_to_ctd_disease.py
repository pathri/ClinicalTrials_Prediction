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


# dictionary name to disease id
dict_name_to_disease_id={}

def integrate_information_into_dict():
    """
    get all node ids from the database
    :return:
    """
    query = '''MATCH (n:%s) RETURN n.disease_id, n.name, n.synonyms'''
    query = query % ('CTDdisease')
    results = g.run(query)

    for identifier, name, synonyms, in results:
        name=name.lower()
        if not name in dict_name_to_disease_id:
            dict_name_to_disease_id[name]=set()
        dict_name_to_disease_id[name].add(identifier)

        if synonyms:
            for synonym in synonyms:
                synonym=synonym.lower()
                if not synonym in dict_name_to_disease_id:
                    dict_name_to_disease_id[synonym]=set()
                dict_name_to_disease_id[synonym].add(identifier)

    print('number of name in database', len(dict_name_to_disease_id))


def prepare_query(file_name):
    cypher_file = open('cypher_disease.cypher', 'w', encoding='utf-8')
    query = '''Using Periodic Commit 10000 Load CSV  WITH HEADERS From "file:''' + path_of_directory + '''master_database_change/mapping_and_merging_into_hetionet/%s" As line FIELDTERMINATOR "\\t" MATCH (n:CTDdisease{disease_id:line.ctd_disease_id}), (g:condition{id:line.ot_disease_id}) Create (n)-[:equal_disease}]->(g);\n'''
    query = query % ( file_name)
    cypher_file.write(query)


def get_all_adrecs_target_and_map():
    """
    prepare files and write information into files
    :return:
    """

    # prepare files
    file_name =  'mapping_disease.csv'
    mapping_file = open(file_name, 'w', encoding='utf-8')
    csv_mapping = csv.writer(mapping_file, delimiter='\t')
    csv_mapping.writerow(['ctd_disease_id', 'ot_disease_id'])

    prepare_query(file_name)


    not_mapping_file = open('not_mapped_disease', 'w', encoding='utf-8')
    csv_not_mapping = csv.writer(not_mapping_file, delimiter='\t')
    csv_not_mapping.writerow(['id', 'name'])


    # get data
    openTrial_file=open('conditions_id_name.csv','r',encoding='utf-8')
    csv_reader=csv.reader(openTrial_file,delimiter=',', quotechar='"')
    next(csv_reader)

    #dictionary disease_id_to_name
    dict_id_to_name={}

    counter_mapper=0
    for line in csv_reader:
        identifier = line[0]
        name=line[1].lower()
        if identifier not in dict_id_to_name:
            dict_id_to_name[identifier]=name
        elif name!=dict_id_to_name[identifier]:
            print('ohje')
            print(name)
            print(dict_id_to_name[identifier])
            print(identifier)
            continue
        else:
            continue

        if name in dict_name_to_disease_id:
            counter_mapper+=1
            for ctd_id in dict_name_to_disease_id[name]:
                csv_mapping.writerow([ctd_id,identifier])
        else:
            csv_not_mapping.writerow([identifier,name])
    print(len(dict_id_to_name),' total number')
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
    print('get all genes from database')

    integrate_information_into_dict()

    print('##########################################################################')

    print(datetime.datetime.utcnow())
    print('prepare file and write information of mapping in it')

    get_all_adrecs_target_and_map()

    print('##########################################################################')

    print(datetime.datetime.utcnow())


if __name__ == "__main__":
    # execute only if run as a script
    main()
