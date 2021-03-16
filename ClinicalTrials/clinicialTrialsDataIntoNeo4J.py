from py2neo import Graph, Node, Relationship
file1 = open("clinical.cypher","w")
def clinicalTrialsDataToNeo4j(file):
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





clinicalTrialsDataToNeo4j("clinicaltrials.txt")
