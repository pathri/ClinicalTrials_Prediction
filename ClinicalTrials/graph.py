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