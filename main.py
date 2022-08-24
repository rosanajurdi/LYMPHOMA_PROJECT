# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os
import dicom2nifti


import dicom2nifti

#dicom2nifti.convert_directory('/Volumes/HDD_ExFAT/trial/1075196', '/Volumes/HDD_ExFAT/nifty')

# Press the green button in the gutter to run the script.
root_dir = '/Volumes/HDD_ExFAT/trial_dicom'
destination_dir ='/Volumes/HDD_ExFAT/trial_nifty'
k = 1

if __name__ == '__main__':
    for file in os.listdir(root_dir):
        print(file)
        k = k + 1
        !ls -1
        #dicom2nifti.convert_directory('/Volumes/HDD_ExFAT/trial_dicom/{}'.format(file), '/Volumes/HDD_ExFAT/trial_nifty')
        print(k)
print(k)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
