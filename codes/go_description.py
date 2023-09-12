import pickle
import re
import os


gene_ontology = dict()
current_file = os.path.abspath(os.path.dirname(__file__))
path_to_gene_ontology =  os.path.join(current_file, '../data/', 'gene_ontology.pkl' )

with open(path_to_gene_ontology, "rb") as f:
    gene_ontology = pickle.load(f)

def remove_evidence_code(text):
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r'\[|\]', '', text)
    text = text.rstrip()
    return text
    
def get_go_description(goterms):
    descriptions = []
    for goterm in goterms:
        try:
            des = gene_ontology[goterm]['def'].replace('"', '')
            des = remove_evidence_code(des)
            if not des.endswith('.'):
                des += '.'
            descriptions.append(des)
          
        except KeyError:
            # handle missing keys here
            print(f"Warning: key {goterm} not found in gene_ontology")
    
    go_description = ' '.join(descriptions)
    # go_description_pro = remove_evidence_code(go_description)
    # print(go_description_pro)
    return go_description
