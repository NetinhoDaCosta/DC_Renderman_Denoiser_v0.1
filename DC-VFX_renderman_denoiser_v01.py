import sys
import os
import subprocess
import re
import pyseq
import time
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

import qtmodern.styles
import qtmodern.windows

from ffprobe import FFProbe
from pprint import pprint
from pymediainfo import MediaInfo
import ffmpeg

### Generates a command line string that converts rendered frames into denoised frames

path = "H:\\test"
denoiser_path = r"C:\Program Files\Pixar\RenderManProServer-23.1\bin\denoise.exe"
noisefilter = r"C:\Program Files\Pixar\RenderManProServer-23.1\lib\denoise\splitVariances.filteroverride.json"

def simple_denoise(denoiser_path, filename):
    command = f'"{denoiser_path}" --crossframe -v variance --override gpuIndex 1 -t 6 -f "{noisefilter}" "{filename}"'
    print(command)
    subprocess.check_output(command, shell=True)



def detect_sequences(pad): # geeft een pad aan en ontvang alle sequences uit dat pad.
    folder = pyseq.get_sequences(pad) # dit is een pad waar meerdere sequences in bestaan
    #pp = pprint.PrettyPrinter(indent=4)
    #pp.pprint(folder)
    #print(str(pad) + " bevat volgende aantal file sequenses: " + str(len(folder))) # aantal folder in folder
    #print_lijstnamen(folder)
    #print("type folder is:" +  str(type(folder)))
    return folder


sequences = pyseq.get_sequences(path)
nr_of_sequences = len(sequences)

for i  in sequences:
    print("test_denoising")
    for x in i:
        folder = "H:\\test\\"
        # filepath = folder + "\\" +  x
        fullpath = str(folder) + str(x)
        print(denoiser_path)
        print(fullpath)
        simple_denoise(denoiser_path,fullpath)

