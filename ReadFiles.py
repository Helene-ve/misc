# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 13:34:55 2019

@author: Helene
"""

import os
def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formatted_date = d.strftime('%m_%d_%Y')
    return formatted_date

from datetime import datetime
def get_files():
    dir_entries = os.scandir('YourDataPath')
    for entry in dir_entries:
        if entry.is_file():
            info = entry.stat()
            datum_modified = convert_date(info.st_mtime)
            print(f'{entry.name}\t Last Modified: ', datum_modified)
    
get_files()

print('Program has executed')
