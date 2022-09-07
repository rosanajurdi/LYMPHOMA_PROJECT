import os
from pathlib import Path
from typing import List
import shutil
from shutil import copy2
import pandas as pd
import nibabel as nb

from Dataset_Helpers import check_dimensions













path = Path('/Users/rosana.eljurdi/Documents/Projects/Lymphoma/T1_Patient_Folder')
nifty_paths: List[Path] = list(path.rglob('*nii'))
for patient_path in nifty_paths:
    patient = nb.load(patient_path)
    print(patient_path.parents[0].name, patient.shape)
    if patient.shape[-1] == 2:
        os.remove(patient_path)
        json_file = list(patient_path.parents[0].rglob('*.json'))
        os.remove(json_file[0])
        for file in os.listdir(patient_path.parents[0]):
            if os.path.isdir(Path(patient_path.parents[0], file)):
                dcm_slices = list(patient_path.parents[0].rglob('*.dcm'))
                for dcm_sl in dcm_slices:
                    if str(dcm_sl).split('-')[-1] == '0002.dcm':
                        print('removing', str(dcm_sl))
                        os.remove(dcm_sl)
check_dimensions()
