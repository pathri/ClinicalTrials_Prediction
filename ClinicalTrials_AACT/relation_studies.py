from py2neo import Graph, Node, Relationship
import csv

def trialscondition_relation():
    #path to file where we have all matches between chembl and drugbank for compounds or salts
    with open('/sas/vidhya/CompoundDb4jV2/ClinicalTrials/AACT/Mar21/studies_condition.csv', 'r') as rf:
        data1 = [row for row in csv.reader(rf)]
        cnt=0
        for i in range(1, len(data1)):
            #print(data[i])
            query1 = '''match (n:AACT_Studies), (m:AACT_Condition) where n.nct_id = "''' + data1[i][0] +'''" and m.id = "''' + data1[i][1] + '''" create (n)-[r:studies_condition]->(m) return count(r) as count'''
            print(query1)
            q1 = graph.run(query1)
            #cnt = cnt + q.data()[0]["count"]
            print(i)
            #break

def trialsinterv_relation():
    #path to file where we have all matches between chembl and drugbank for compounds or salts
    with open('/sas/vidhya/CompoundDb4jV2/ClinicalTrials/AACT/Mar21/studies_intervention.csv', 'r') as rf:
        data2 = [row for row in csv.reader(rf)]
        cnt=0
        for i in range(1, len(data2)):
            #print(data[i])
            query2 = '''match (p:AACT_Studies), (q:AACT_Interventions_Drug) where p.nct_id = "''' + data2[i][0] +'''" and q.id = "''' + data2[i][1] + '''" create (p)-[r:studies_intervention]->(q) return count(r) as count'''
            #print(query)
            q2 = graph.run(query2)
            #cnt = cnt + q.data()[0]["count"]
            print(i)
            #break

graph = Graph()
trialscondition_relation()
trialsinterv_relation()