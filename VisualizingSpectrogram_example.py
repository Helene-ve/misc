# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 11:42:29 2019

@author: Helene
"""
from __future__ import absolute_import, division, print_function, unicode_literals
import os

import matplotlib
from matplotlib import pyplot as plt

import soundfile as sf
import scipy.signal as signal

data_root = "YourDataPathRoot"

## date is not used currently, print is commented out for now,
## but retained code in this module for future purposes
def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formatted_date = d.strftime('%m_%d_%Y')
    return formatted_date

from datetime import datetime
def get_files():
    dir_entries = os.scandir(data_root)
    all_files = []
    for entry in dir_entries:
        if entry.is_file():
            info = entry.stat()
            datum_modified = convert_date(info.st_mtime)
#            print(f'{entry.name}\t Last Modified: ', datum_modified)
            all_files.append(entry.name)
    return all_files
    
all_files = get_files()
print('There are', len(all_files), 'files in the specified directory.')

#Range runs to 20 to avoid opening too many figures.
for i in range(1,20):
    file1 = all_files[i]
    
    # open new figure for each new plot
    plt.figure()
    
    # read in data and calculate spectrogram with scipy.signal and plot it with matplotlib
    data, samplerate = sf.read(data_root + file1)
    Pxx, freqs, bins, im = plt.specgram(data, Fs=samplerate)
    
    # add axis labels
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [sec]; Plot: %s' %file1)


## Alternative spectrogram
    #freq, time, Sxx = signal.spectrogram(data, samplerate, scaling='spectrum')
    #plt.pcolormesh(time, freq, Sxx)