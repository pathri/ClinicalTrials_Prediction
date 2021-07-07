import csv
import sys
import datetime, re
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

# dictionary synonym to disease id
dict_synonym_to_disease_id={}

# dictionary ctd id to name
dict_ctd_id_to_name={}

def integrate_information_into_dict():
    """
    get all node ids from the database
    :return:
    """
    query = '''MATCH (n:%s) RETURN n.disease_id, n.name, n.synonyms'''
    query = query % ('CTD_disease')
    results = g.run(query)

    for identifier, name, synonyms, in results:

        name=name.lower()

        dict_ctd_id_to_name[identifier]=name
        if not name in dict_name_to_disease_id:
            dict_name_to_disease_id[name]=set()
        dict_name_to_disease_id[name].add(identifier)

        if synonyms:
            for synonym in synonyms:
                synonym=synonym.lower()
                if not synonym in dict_synonym_to_disease_id:
                    dict_synonym_to_disease_id[synonym]=set()
                dict_synonym_to_disease_id[synonym].add(identifier)

    print('number of name in database', len(dict_name_to_disease_id))
    print('number of synonyms in database', len(dict_synonym_to_disease_id))


def prepare_query(file_name):
    cypher_file = open('cypher_disease.cypher', 'w', encoding='utf-8')
    query = '''Using Periodic Commit 10000 Load CSV  WITH HEADERS From "file:''' + path_of_directory + '''master_database_change/mapping_and_merging_into_hetionet/%s" As line FIELDTERMINATOR "\\t" MATCH (n:CTDdisease{disease_id:line.ctd_disease_id}), (g:condition{id:line.ot_disease_id}) Create (n)-[:equal_disease}]->(g);\n'''
    query = query % ( file_name)
    cypher_file.write(query)

dict_condition_id_to_ctd_disease_id={}

def write_into_files(identifier,name, dictionary_name_to_disease, counter_multi, csv_mapping, csv_mapping_multi):
    """
    write mapping into the files
    :param identifier: string
    :param name: string
    :param dictionary_name_to_disease: dictionary
    :param counter_multi: int
    :return: int
    """
    multi = False
    if len(dictionary_name_to_disease[name]) > 1 and not identifier in dict_condition_id_to_ctd_disease_id:  #
        multi = True
        counter_multi += 1
    elif identifier in dict_condition_id_to_ctd_disease_id:
        csv_mapping.writerow([dict_condition_id_to_ctd_disease_id[identifier], identifier])
        return

    for ctd_id in dictionary_name_to_disease[name]:
        csv_mapping.writerow([ctd_id, identifier, name])
        if multi:
            csv_mapping_multi.writerow([identifier, name, ctd_id, dict_ctd_id_to_name[ctd_id]])
    return counter_multi

def get_all_conditions():
    """
    prepare files and write information into files
    :return:
    """

    # prepare files
    file_name =  'mapping_disease.csv'
    mapping_file = open(file_name, 'w', encoding='utf-8')
    csv_mapping = csv.writer(mapping_file, delimiter='\t')
    csv_mapping.writerow(['ctd_disease_id', 'condition_id'])

    prepare_query(file_name)

    file_name = 'mapping_disease_multi.csv'
    mapping_file_multi = open(file_name, 'w', encoding='utf-8')
    csv_mapping_multi = csv.writer(mapping_file_multi, delimiter='\t')
    csv_mapping_multi.writerow(['ot_disease_id','ot_disease_name','ctd_disease_id', 'ctd_name'])


    not_mapping_file = open('not_mapped_disease', 'w', encoding='utf-8')
    csv_not_mapping = csv.writer(not_mapping_file, delimiter='\t')
    csv_not_mapping.writerow(['id', 'name'])


    # get data
    openTrial_file=open('conditions.txt','r',encoding='utf-8')
    csv_reader=csv.reader(openTrial_file,delimiter='|', quotechar='"')

    # openTrial_file=open('part_condition.tsv','r',encoding='utf-8')
    # csv_reader=csv.reader(openTrial_file,delimiter='\t', quotechar='"')
    next(csv_reader)

    #dictionary disease_id_to_name
    dict_id_to_name={}

    counter_mapper=0
    counter_multi=0
    count_all=0
    for line in csv_reader:
        identifier = line[0]
        name=line[3]
        if name[-1]==')':
            print(name)
            name=re.sub(' \([a-z]+\)$','',name)
        count_all+=1
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
            counter_multi=write_into_files(identifier, name, dict_name_to_disease_id, counter_multi, csv_mapping, csv_mapping_multi)
        elif name in dict_synonym_to_disease_id:
            counter_mapper+=1
            counter_multi=write_into_files(identifier,name,dict_synonym_to_disease_id, counter_multi, csv_mapping, csv_mapping_multi)
        else:
            csv_not_mapping.writerow([identifier,name])
    print(len(dict_id_to_name),' total number')
    print('mapped ',counter_mapper)
    print('counter of multi:',counter_multi)
    print('all conditions:',count_all)


def main():
    print(datetime.datetime.utcnow())

    global path_of_directory
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

    get_all_conditions()

    print('##########################################################################')

    print(datetime.datetime.utcnow())


if __name__ == "__main__":
    # execute only if run as a script
    main()
