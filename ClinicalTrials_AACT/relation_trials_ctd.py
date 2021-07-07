from py2neo import Graph, Node, Relationship
import csv

def trialscondition_ctddisease_relation():
    #path to file where we have all matches between chembl and drugbank for compounds or salts
    with open('/sas/vidhya/CompoundDb4jV2/ClinicalTrials/AACT/Mar21/mapping_disease.csv', 'r') as rf:
        data = [row for row in csv.reader(rf)]
        cnt=0
        for i in range(1, len(data)):
            #print(data[i])
            query = '''match (n:CTD_disease), (m:AACT_Condition) where n.disease_id = "''' + data[i][0] +'''" and m.id = "''' + data[i][1] + '''" create (m)-[r:equal_disease_CTD]->(n) return count(r) as count'''
            #print(query)
            q = graph.run(query)
            cnt = cnt + q.data()[0]["count"]
            print(i)
            

graph = Graph()
trialscondition_ctddisease_relation()