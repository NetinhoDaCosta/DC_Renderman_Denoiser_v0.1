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

RenderManProServerFolder = r"C:\Program Files\Pixar\RenderManProServer-23.1"
denoiser_path = RenderManProServerFolder + r"\bin\denoise.exe"


noisefilter = r"C:\Program Files\Pixar\RenderManProServer-23.1\lib\denoise\splitVariances.filteroverride.json"


def simple_denoise(denoiser_path, filename):
    command = f'"{denoiser_path}" --crossframe -v variance --override gpuIndex 1 -t 6 -f "{noisefilter}" "{filename}"'
    print(command)
    subprocess.check_output(command, shell=True)


def detect_sequences(pad): # geeft een pad aan en ontvang alle sequences uit dat pad.
    seq = pyseq.get_sequences(pad) # dit is een pad waar meerdere sequences in bestaan
    #pp = pprint.PrettyPrinter(indent=4)
    #pp.pprint(folder)
    #print(str(pad) + " bevat volgende aantal file sequenses: " + str(len(folder))) # aantal folder in folder
    #print_lijstnamen(folder)
    #print("type folder is:" +  str(type(folder)))
    return seq


sequences = detect_sequences(path)

folder = "H:\\test\\"

def get_single_file_url(folder, sequences):
    for sequence in sequences:
        #returns one sequence as a list
        for filename in sequence:
            full_file_path = str(folder) + str(filename)
            print(full_file_path)
            return full_file_path



def get_folder(file_path):
    folder_path = os.path.dirname(file_path)
    return folder_path

folder_path = get_folder(get_single_file_url(folder,sequences))


print("boom")
print(get_single_file_url(folder, sequences))
print(folder_path)
print("fiets")
print(sequences.dirname(path))
print("aap")


nr_of_sequences = len(sequences)

for i  in sequences:
    print("test_denoising")
    for x in i:
        folder = "H:\\test\\"
        # filepath = folder + "\\" +  x
        full_file_path = str(folder) + str(x)
        print(denoiser_path)
        print(full_file_path)

        #simple_denoise(denoiser_path,full_file_path)

