import os, shutil
import pandas as pd
import os
from pathlib import Path
from typing import List
import shutil
from shutil import copy2
import pandas as pd


# The excel sheet with the T1 modalities
df = pd.read_csv('/Users/rosana.eljurdi/PycharmProjects/Lymphoma-Project-clinicadl/DataSet-Description/T1_Modality_ordered.csv')
modality_list = list(df['Acronyms for T1 sequence after contrast '].dropna())

root = '/Users/rosana.eljurdi/Documents/Projects/Lymphoma/dataset_60'
source_path = Path(root)

T1ds_path = '/Users/rosana.eljurdi/Documents/Projects/Lymphoma/T1_Patient_Folder'


'''
# Removing nifty files and their corresponding json ones.
nii_paths: List[Path] = list(source_path.rglob('*.bvec'))
for file in nii_paths:
    print(file)
    os.remove(file)
'''
def Is_mod_inT1List(key):
    for mod in modality_list:
        if mod in key:
            return True
T1mod_list = []
for file in os.listdir(root):
    patient_path = Path(root, file)
    dst_path = Path(T1ds_path, file)
    dst_path.mkdir(parents=True, exist_ok=True)
    if file != '.DS_Store':
        for patient_id in os.listdir(os.path.join(root,file)):

            if os.path.isdir(os.path.join(root, file, patient_id)):
                current_pat_modalities = [os.path.join(root, file, patient_id, o)
                              for o in os.listdir(os.path.join(root,file,patient_id))]

                for modality in current_pat_modalities:
                    key = os.path.basename(modality).replace('_', ' ')
                     # file instead of patient_id
                    in_check = Is_mod_inT1List(key)
                    if in_check:
                        print(file, key)
                        #T1mod_list.append([file, key])
                        src = os.path.join(patient_path, file, patient_id, modality)
                        dst = os.path.join(T1ds_path, file, os.path.basename(modality))
                        shutil.copytree(src, dst, copy_function=copy2)

T1mod = pd.DataFrame(T1mod_list)
T1mod.to_csv(os.path.join(T1ds_path, 'T1_modality_new.csv'))

