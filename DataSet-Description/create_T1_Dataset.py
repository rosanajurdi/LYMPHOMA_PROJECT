'''
Created on Feb 13, 2020
@author: eljurros
'''
'''
Created on Mar 20, 2019
@author: Rosana EL JURDI: 
Script to generate the T1 dataset from the lymphoma data.
'''
import os
from pathlib import Path
from typing import List
import shutil
from shutil import copy2
import pandas as pd

path = Path('/Users/rosana.eljurdi/Documents/Lymphoma/Segm_LOC')
source_path = '/Users/rosana.eljurdi/Documents/Lymphoma/Examens anonymisés et convertis en nii'
dest_path = '/Users/rosana.eljurdi/Documents/Lymphoma/dataset_60_NEW'

Annotated_paths: List[Path] = list(path.rglob('*_segm.nii.gz'))
anotated_patients = [pat.name.split('_segm.nii.gz')[0] for pat in Annotated_paths]
assert len(Annotated_paths) == 60

df = pd.read_csv('/Users/rosana.eljurdi/PycharmProjects/Lymphoma-Project-clinicadl/DataSet-Description/T1_Modality_ordered.csv')
modality_list = list(df['Acronyms for T1 sequence after contrast '].dropna())


for patient in anotated_patients:
    try:
        dst = os.path.join(dest_path, patient)
        src = os.path.join(source_path, patient)
        assert os.path.exists(src)
        assert os.path.exists(dst) == False
        shutil.copytree(src, dst, copy_function=copy2)
    except:
        print(patient)


