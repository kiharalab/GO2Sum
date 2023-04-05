import pickle


gene_ontology = dict()
with open("data/gene_ontology.pkl", "rb") as f:
    gene_ontology = pickle.load(f)

    
def get_go_description(goterms):
    descriptions = []
    for goterm in goterms:
        try:
            des = gene_ontology[goterm]['def'].replace('"', '')
            descriptions.append(des)
        except KeyError:
            # handle missing keys here
            print(f"Warning: key {goterm} not found in gene_ontology")
    
    go_description = ' '.join(descriptions)
    return go_description
