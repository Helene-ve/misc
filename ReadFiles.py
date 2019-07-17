# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 13:34:55 2019

@author: Helene
"""

def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formatted_date = d.strftime('%d %b %Y')
    return formatted_date

from datetime import datetime
def get_files():
    dir_entries = os.scandir('/media/moelven/Apis/01/')
    for entry in dir_entries:
        if entry.is_file():
            info = entry.stat()
            print(f'{entryname}\t Last Modified: {convert_date(info..st_mtime)})

