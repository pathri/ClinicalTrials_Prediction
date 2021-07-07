from py2neo import Graph, Node, Relationship
import csv

def trialsdrugbank_relation():
    #intervention_compounddb_fail intervention_compounddb_passb2 intervention_compounddb_passb1
    with open('/sas/vidhya/CompoundDb4jV2/ClinicalTrials/AACT/Mar21/intervention_compounddb_fail.csv', 'r') as rf:
        data = [row for row in csv.reader(rf)]
        cnt=0
        for i in range(1, len(data)):
            #print(data[i])
            query = '''match (n:AACT_Interventions_Drug), (m:Compound_DrugBank) where n.id= "''' + data[i][1] +'''" and m.identifier = "''' + data[i][2] + '''" create (n)-[r:equal_drug_DrugBank]->(m) return count(r) as count'''
            #print(query)
            q = graph.run(query)
            #cnt = cnt + q.data()[0]["count"]
            print(i)
            #break

def trialsdrugbanksalt_relation():
    #intervention_saltdb_fail intervention_saltdb_passb1 

    with open('/sas/vidhya/CompoundDb4jV2/ClinicalTrials/AACT/Mar21/intervention_saltdb_fail.csv', 'r') as rf:
        data = [row for row in csv.reader(rf)]
        cnt=0
        for i in range(1, len(data)):
            #print(data[i])
            query = '''match (n:AACT_Interventions_Drug), (m:Salt_DrugBank) where n.id= "''' + data[i][1] +'''" and m.identifier = "''' + data[i][2] + '''" create (n)-[r:equal_drug_DrugBank]->(m) return count(r) as count'''
            #print(query)
            q = graph.run(query)
            #cnt = cnt + q.data()[0]["count"]
            print(i)

graph = Graph()
trialsdrugbank_relation()
#trialsdrugbanksalt_relation()