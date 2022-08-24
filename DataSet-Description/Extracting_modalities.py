import pandas as pd

import os
from pathlib import Path
from typing import Dict, List, Tuple
import json
from pandas.io.json import json_normalize

train_path: Path = Path('/Users/rosana.eljurdi/Documents/Projects/Lymphoma/Examens-anonymisés-et-convertis-en-nii')
all_nii_path: List[Path] = list(train_path.rglob('*.nii'))
all_paths: List[Path] = list(train_path.rglob('*.json'))

print(len(all_paths))
print(len(all_nii_path))

modality_list =[]
for file in all_paths:
    try:
        with open(file) as json_data:
            data = json.load(json_data)
        if data['SeriesDescription'] not in modality_list:
            modality_list.append(data['SeriesDescription'])

    except:
        print(file)

print('heelo')
mod = pd.DataFrame(modality_list)
mod.to_csv(os.path.join(train_path, 'modality_new.csv'))