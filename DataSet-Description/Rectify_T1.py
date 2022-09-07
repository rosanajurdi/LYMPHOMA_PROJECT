import os, shutil
import pandas as pd
import os
from pathlib import Path
from typing import List
import shutil
from shutil import copy2
import pandas as pd


root = '/Users/rosana.eljurdi/Documents/Projects/Lymphoma/T1_Patient_Folder'
source_path = Path(root)
f = open(os.path.join(root,"Content.txt"), "a")
for file in os.listdir(root):
    patient_path = Path(root, file)
    if os.path.isdir(patient_path):
        modality_list = [name for name in os.listdir(patient_path) if os.path.isdir(os.path.join(patient_path, name))]
        nb = len([name for name in os.listdir(patient_path) if os.path.isdir(os.path.join(patient_path, name))])
        for mod in modality_list:
            print(file,",",mod,",",nb)


