from py2neo import Graph, Node, Relationship
file1 = open("clinical.cypher","w")
def exportCSV(file):
    with open(file) as f:
        lines = f.readlines()
        for line in lines:
            i = 0
            query = '''USING PERIODIC COMMIT LOAD CSV WITH HEADERS FROM \"file:///AllTables_CSV/'''
            for word in line.split(','):
                if i==0:
                    query = query + word + ".csv\" AS row FIELDTERMINATOR ',' CREATE (:clinicaltrials_"+word+"{"
                    i=i+1
                else:
                    query = query + word + ":row." + word + ", "
            query = query[:-2]
            query = query + "});"
            i=0
            #print query
            file1.write(query)
            file1.write("\n")
            # graph.run(query)

# def combine_nodes(merge_node, delete_node, primary_key):
#     q1 = '''match (n:''' + delete_node + ''') return keys(n) as keys limit 1'''
#     dict = graph.run(q1)
#     list = dict.data()[0]["keys"]
#     query = '''match (x:''' + merge_node + '''), (y:''' + delete_node + ''') where x.''' + primary_key + ''' = y.''' + primary_key + ''' set '''
#     for i in list:
#         if i != primary_key:
#             query = query + '''x.''' + i + ''' = y.''' + i + ''', '''
#     query = query[:-2]
#     query = query + ''' detach delete y return x limit 100000'''
#     print(query)
#     q2 = '''MATCH (n:''' + delete_node+ ''') RETURN count(n)'''
#     value = graph.run(q2).data()
#     value = value[0]["count(n)"]
#     temp = -1
#     while(value != 0 and temp != value):
#         graph.run(query)
#         temp = value
#         value = graph.run(q2).data()
#         value = value[0]["count(n)"]
#         print(value)


# def write_to_csv():
#     q1 = '''match (n) return distinct labels(n)'''
#     list = graph.run(q1)
#     for i in list:
# 	   print(i[0][0])
# 	   q2 = '''match (n:''' + i[0][0] + ''') return keys(n) as keys limit 1'''
# 	   dict = graph.run(q2)
# 	   list2 = dict.data()[0]["keys"]
# 	   q3 = '''call apoc.export.csv.query(\"match (n:''' + i[0][0] + ''') return '''
# 	   for j in list2:
# 	       q3 = q3 + '''n.''' + j + ''' as ''' + j + ''', '''
# 	       q3 = q3[:-2]
#     q3 = q3 + '''\", \"/tmp/''' + i[0][0] +'''.csv\", {batchSize:100000})'''
# 		print(q3)


# def deleteProcessed():
#     query = "match (n:processed) with n limit 100000 remove n:processed return count(*) as processed"
#     if query != "":
#         values = graph.run(query).data()
#         value = values[0]["processed"]
#         while(value==100000):
#             values = graph.run(query).data()
#             value = values[0]["processed"]

# def relationships():
#     csv = []
#     keys = []
#     with open("primarykey.txt") as f:
#         lines = f.readlines()
#         for line in lines:
#             i=0
#             for word in line.split():
#                 if i==0:
#                     csv.append(word)
#                     i=i+1
#                 else:
#                     keys.append(word)
#     with open("schema_select_tables.txt") as f:
#         lines = f.readlines()
#         for line in lines:
#             i=0
#             query = ""
#             for word in line.split():
#                 if i==0:
#                     file = word
#                     i=i+1
#                 else:
#                     for key in range(0, len(keys)):
#                         if keys[key] == word and csv[key]!=file:
#                             query = "MATCH (a:"+csv[key] + ") WITH a MATCH (p:" + file + "{" + word + ": a." + word +"} ) WHERE NOT p:processed WITH a, p LIMIT 10000 MERGE (p) - [:child_of] -> (a) SET p:processed RETURN COUNT(*) AS processed"
#                             #print(query)
#                             values = graph.run(query).data()
#                             value = values[0]["processed"]
#                             print(value)
#                             while(value==100000):
#                                 print(value)
#                                 values = graph.run(query).data()
#                                 value = values[0]["processed"]
#                             #print value
#                             deleteProcessed()
#                             #print "Deleted processed"
#                             #print csv[key] + word

# def delete():
#     query = "MATCH ()-[r:child_of]-() with r limit 100000 DELETE r return count(r) as deletedrelations"
#     if query != "":
#         values = graph.run(query).data()
#         value = values[0]["deletedrelations"]
#         while(value==100000):
#             values = graph.run(query).data()
#             value = values[0]["deletedrelations"]
#             #print value

# def relationships_with_names(from_node, to_node, property_node, pk_relation, pk_property, relation_name):
#     query = '''match (a:''' + from_node + '''), (b:''' + to_node + '''), (c:''' + property_node + ''') where b.''' + pk_property + ''' = c.''' + pk_property + ''' and a.''' + pk_relation + ''' = b.''' + pk_relation + ''' and NOT a:processed with a,b,c limit 10000 merge (a)-[r:''' + relation_name + '''{'''
#     q1 = '''match (n:''' + property_node + ''') return keys(n) as keys limit 1'''
#     dict = graph.run(q1)
#     list = dict.data()[0]["keys"]
#     for i in list:
#         query = query + i + ''': c.''' + i + ''', '''
#     query = query[:-2]
#     query = query + '''}]->(b) set a:processed return count(*) as processed'''
#     values = graph.run(query).data()
#     value = values[0]["processed"]
#     while(value==100000):
#         print(value)
#         values = graph.run(query).data()
#         value = values[0]["processed"]
#     print(value)
#     deleteProcessed()
#     print("Deleted processed")

# def relations(from_node, to_node, property_node, pk_from, pk_to, relation_name):
#     query = '''match (a:''' + from_node + '''), (b:''' + to_node + '''), (c:''' + property_node + ''') where a.''' + pk_from + ''' = c.''' + pk_from + ''' and b.''' + pk_to + ''' = c.''' + pk_to + ''' and NOT c:processed with a,b,c limit 100000 merge (a)-[r:''' + relation_name + '''{'''
#     q1 = '''match (n:''' + property_node + ''') return keys(n) as keys limit 1'''
#     dict = graph.run(q1)
#     list = dict.data()[0]["keys"]
#     for i in list:
#         query = query + i + ''': c.''' + i + ''', '''
#     query = query[:-2]
#     query = query + '''}]->(b) set c:processed return count(*) as processed'''
#     print(query)
#     values = graph.run(query).data()
#     value = values[0]["processed"]
#     while(value==100000):
#         print(value)
#         values = graph.run(query).data()
#         value = values[0]["processed"]
#     print(value)
#     deleteProcessed()
#     print("Deleted processed")
    
# def relationships_without_property(from_node, to_node, pk, relation_name):
#     query = '''match (a:''' + from_node + '''), (b:''' + to_node + ''') where b.''' + pk + ''' = a.''' + pk +  ''' and NOT a:processed with a,b limit 10000 merge (a)-[r:''' + relation_name 
#     query = query + ''']->(b) set a:processed return count(*) as processed'''
#     print(query)
#     values = graph.run(query).data()
#     value = values[0]["processed"]
#     while(value==10000):
#         print(value)
#         values = graph.run(query).data()
#         value = values[0]["processed"]
#     print(value)
#     deleteProcessed()
#     print("Deleted processed")
def relaitonClinicalTrials(filename, from_table, to_table, from_attribute, to_attribute, relation_name, i ):
    file2 = open(filename,'r')
    for lines in file2:
        attributes = lines.split('\t')
        # query = '''match (a:Compound_DrugBank),(b:clinicaltrials_fda_approvals) where any(x in a.synonyms where tolower(x)=\'''' + attributes[1] +'''\') and tolower(b.name)=\''''+ attributes[1]+ '''\' merge  (a)-[r:Synonyms_drugbank_clinicaltrials]->(b)'''
        query = '''match (a:''' + from_table +'),(b:' + to_table + ')where a.'+from_attribute + '=\"' + attributes[i] + '\" and tolower(b.' + to_attribute + ')=tolower(\"' + attributes[1] + '\") merge (a)-[r:' + relation_name + ']->(b)'
        file4.write(query+';\n')


# uri = "bolt://localhost:7687"
# user = "neo4j"
# password = ""
# graph = Graph(uri=uri, user=user, password=password)
# file4 = open('cypher_file5.cypher','a')
exportCSV("clinicaltrials.txt")
# relaitonClinicalTrials('/sas/vidhya/CompoundDb4jV2/ClinicalTrials/UniqSaltOutcome.csv', 'Salt_DrugBank', 'clinicaltrials_fda_applications', 'name', 'drug_name', 'exits_drugbank_clinicaltrials',1)
# relaitonClinicalTrials('/sas/vidhya/CompoundDb4jV2/ClinicalTrials/UniqProduct.csv', 'Product_DrugBank', 'clinicaltrials_fda_applications', 'name', 'drug_name', 'exits_drugbank_clinicaltrials',1)
# relaitonClinicalTrials('/sas/vidhya/CompoundDb4jV2/ClinicalTrials/UniqDescription.csv', 'Compound_DrugBank', 'clinicaltrials_fda_applications', 'identifier', 'drug_name', 'exits_drugbank_clinicaltrials',0)
# relaitonClinicalTrials('/sas/vidhya/CompoundDb4jV2/ClinicalTrials/UniqBrands.csv', 'Compound_DrugBank', 'clinicaltrials_fda_applications', 'identifier', 'drug_name', 'exits_drugbank_clinicaltrials',0)
# relaitonClinicalTrials('/sas/vidhya/CompoundDb4jV2/ClinicalTrials/UniqNames.csv', 'Compound_DrugBank', 'clinicaltrials_fda_applications', 'identifier', 'drug_name', 'exits_drugbank_clinicaltrials',0)
# relaitonClinicalTrials('/sas/vidhya/CompoundDb4jV2/ClinicalTrials/UniqSyn.csv', 'Compound_DrugBank', 'clinicaltrials_fda_applications', 'identifier', 'drug_name', 'exits_drugbank_clinicaltrials',0)