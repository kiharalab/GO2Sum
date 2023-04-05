from simplet5 import SimpleT5
from codes.confidence_score import predict_with_score
from codes.go_description import get_go_description
import os
import math
import csv





modelFunc = SimpleT5()
modelFunc.from_pretrained(model_type="t5", model_name="t5-base")
modelSubunit = SimpleT5()
modelSubunit.from_pretrained(model_type="t5", model_name="t5-base")
modelPathway = SimpleT5()
modelPathway.from_pretrained(model_type="t5", model_name="t5-base")
beam_size=10
num_of_summary=1
result_dir='results/'

def get_confidence_score(score):
    score = -3.5
    positive_score = math.exp(-score)
    return positive_score
   


def function(df,filename):
    print('Started generating Function CC on the dataset !')
    if not os.path.exists(result_dir):
        os.makedirs(result_dir)
    model_path ='models/functionCC'
    modelFunc.load_model("t5",model_path, use_gpu=False)
    result_file = result_dir+'function_'+filename
    with open(result_file, 'w',newline='') as file:
        writer = csv.writer(file,delimiter='\t')
        for item, row in df.iterrows(): 
            protein = row['Protein']
            go_id  = row['GO_IDs']
            go_ids = go_id.split(";")
            GO_Document=get_go_description(go_ids)
            summary = predict_with_score(modelFunc,GO_Document,num_return_sequences=num_of_summary,num_beams=beam_size)
            for ele in summary:
                writer.writerow([protein, ele[0], get_confidence_score(ele[1])])
    print('Completed generating Function CC on the dataset !')


        

def subunit(df,filename):
    print('Started generating Subunit on the dataset !')
    if not os.path.exists(result_dir):
        os.makedirs(result_dir)
    model_path ='models/subunit'
    modelSubunit.load_model("t5",model_path, use_gpu=False)
    result_file = result_dir+'subunit_'+filename
    with open(result_file, 'w',newline='') as file:
        writer = csv.writer(file,delimiter='\t')
        for item, row in df.iterrows(): 
            protein = row['Protein']
            go_id  = row['GO_IDs']
            go_ids = go_id.split(";")
            GO_Document=get_go_description(go_ids)
            summary = predict_with_score(modelSubunit,GO_Document,num_return_sequences=num_of_summary,num_beams=beam_size)
            for ele in summary:
                writer.writerow([protein, ele[0], get_confidence_score(ele[1])])
    print('Completed generating Subunit on the dataset !')
    

def pathway(df,filename):
    print('Started generating Pathway on the dataset !')
    if not os.path.exists(result_dir):
        os.makedirs(result_dir)
    model_path ='models/pathway'
    modelPathway.load_model("t5",model_path, use_gpu=False)
    result_file = result_dir+'pathway_'+filename
    with open(result_file, 'w',newline='') as file:
        writer = csv.writer(file,delimiter='\t')
        for item, row in df.iterrows(): 
            protein = row['Protein']
            go_id  = row['GO_IDs']
            go_ids = go_id.split(";")
            GO_Document=get_go_description(go_ids)
            summary = predict_with_score(modelPathway,GO_Document,num_return_sequences=num_of_summary,num_beams=beam_size)
            for ele in summary:
                writer.writerow([protein, ele[0], get_confidence_score(ele[1])])
    print('Completed generating Pathway on the dataset !')
    