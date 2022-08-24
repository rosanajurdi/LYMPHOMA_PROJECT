import os, shutil
import pandas as pd
import os
from pathlib import Path
from typing import List
import shutil
from shutil import copy2
import pandas as pd

def test_string(string_1, string_2):
    if string_1 in string_2:
        return string_1, True
root = '/Users/rosana.eljurdi/Documents/Lymphoma/Examens anonymisés et convertis en nii'
source_path = Path(root)

df = pd.read_csv('/Users/rosana.eljurdi/PycharmProjects/Lymphoma-Project-clinicadl/DataSet-Description/T1_Modality_ordered.csv')
modality_list = list(df['Acronyms for T1 sequence after contrast '].dropna())

nii_paths: List[Path] = list(source_path.rglob('*.json'))
for file in nii_paths:
    print(file)
    os.remove(file)

for file in os.listdir(root):
    for patient_id in os.listdir(os.path.join(root,file)):
        if os.path.isdir(os.path.join(root, file, patient_id)):
            modalities = [os.path.join(root, file, patient_id, o)
                          for o in os.listdir(os.path.join(root,file,patient_id))]

            for modality in modalities:
                # key = os.path.basename(modality).replace('_', ' ')
                for modality in modality_list:
                    s, ins =  test_string(key, modality)
                    if ins is True:
                        print(s)

                    print(modality)

