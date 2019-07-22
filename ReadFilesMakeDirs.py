# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 13:34:55 2019
This script reads files, extracts dates and filenames, creates directories
based on filenames for different categories (in this case sound recordings from 
three different mics), and moves files to the right directory.
@author: Helene van Ettinger-Veenstra
"""

import os
import re
from datetime import datetime

data_root = "YourDataRoot"
dict_mics = {1: 'Your', 2: 'Different', 3: 'Categories'}

# This function is unused at the moment as the datum is extracted from the
# filename instead for our case.

def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formatted_date = d.strftime('%m_%d_%Y')
    return formatted_date

def get_files():
    dir_entries = os.scandir(data_root)
    all_files = []
    for entry in dir_entries:
        if entry.is_file():
            info = entry.stat()
            datum_modified = convert_date(info.st_mtime)
            ## The print commands are for checking purposes and therefore
            ## commented out in the final version            
            # print(f'{entry.name}\t Last Modified: ', datum_modified)
            all_files.append(entry.name)
    return all_files
    
all_files = get_files()
print('There are', len(all_files), 'files in the specified directory.')

# This function runs for a specified mic and returns a list with relevant data
# extracted from filenames, to create directories from
def file_from_mic(which_mic, all_files):
    dir_name = []
    relevant_files = []
    dir_and_files = []
    for i in range(1,(len(all_files)+1)):
        file = all_files[i-1]
        if re.match(dict_mics[which_mic], file):
            try:
                # Find the constant part of your filenames
                found = re.search('YOURSPECIFICSTRING(.*?).flac', file).group(1)
                # Extract the for you relevant part of your filename
                dir_name.append(found[5:9])
                relevant_files.append(file)                
            except AttributeError:
                # if filename is not XXX.flac
                print('irregular filename', file) # apply your error handling
    dir_and_files = dir_name, relevant_files
    return dir_name, dir_and_files

# The function runs 3 times for each mic
dir_one, dir_and_files_one = file_from_mic(1, all_files)
dir_two, dir_and_files_two = file_from_mic(2, all_files)
dir_three, dir_and_files_three = file_from_mic(3, all_files)

# create different directories for extracted part from filename
def dir_for_mic(which_dir, mic, dir_and_files):
    newdir_list = []
    dir_unique = list(set(which_dir))
    for f in range(1,(len(dir_unique))+1):
        newdir_name = (data_root + '0' + mic + '/'+ dir_unique[f-1])
        newdir_list.append(newdir_name)
        if not os.path.exists(newdir_name):
            os.makedirs(newdir_name)
            ## for tests: comment out previous line and uncomment next;
            ## which will only print dir_name and not make directories.
#            print('this would be the dir name:', newdir_name)


    ## move all files from the specific mic to the new folder
    for g in range(1,(len(dir_and_files[0])+1)):
        old_path = os.path.join(data_root, dir_and_files[1][g-1])
        old_path = old_path.replace(os.sep, '/')
        new_path = os.path.join(data_root,'0'+ mic, which_dir[g-1], dir_and_files[1][g-1])
        new_path = new_path.replace(os.sep, '/')
        os.rename(old_path, new_path)
        ## for tests: comment out previous line and uncomment next;
        ## which will only print dir_name and not make directories.
#        print('old path =', old_path)
#        print('new path =', new_path)

# Print how many different unique directories are found and made
    print('The unique directories for mic nr', mic, 'are: ', dir_unique)
    return dir_unique

# The function runs 3 times for each mic
dir_for_mic(dir_one, '1', dir_and_files_one)
dir_for_mic(dir_two, '2', dir_and_files_two)
dir_for_mic(dir_three, '3', dir_and_files_three)
