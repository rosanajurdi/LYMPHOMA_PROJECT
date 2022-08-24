import os, shutil
import pandas as pd
import os
from pathlib import Path
from typing import List
import shutil
from shutil import copy2
import pandas as pd

root = '/Users/rosana.eljurdi/Documents/Projects/Lymphoma/Examens-anonymisés-et-convertis-en-nii'
source_path = Path(root)
Modality_list_per_patient = []


modality_df = pd.read_csv(os.path.join(root, "modality.csv"))
modality_df.columns = ['index', 'modality_name']
modality_list = list(modality_df['modality_name'])

f = open(os.path.join(root,"Description.txt"), "a")

i = 0
for file in os.listdir(root):
    patient_path = Path(root, file)
    i = i +1
    if os.path.isdir(os.path.join(root, file)):
        for patient_id in os.listdir(os.path.join(root,file)):

            if os.path.isdir(os.path.join(root, file, patient_id)):
                current_pat_modalities = [o for o in os.listdir(os.path.join(root,file,patient_id))]
                print('{}, {}'.format(file, current_pat_modalities))
                f.write('{}, {} \n '.format(file, current_pat_modalities))

f.close()
print(i)



