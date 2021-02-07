import sys
import os
import subprocess
import re
import pyseq
import time
import fileseq
import interface
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5.QtCore import QUrl

import fsutil
from pathlib import Path

from pprint import pprint
from interface import Ui_MainWindow

import qtmodern.styles
import qtmodern.windows

""" root = Path()
if getattr(sys, 'frozen', False):
    root = Path(sys._MEIPASS)
    qtmodern.styles._STYLESHEET = root / 'qtmodern/style.qss'
    qtmodern.windows._FL_STYLESHEET = root / 'qtmodern/frameless.qss' """

### Generates a command line string that converts rendered frames into denoised frames

path = "H:\\test"




""" selected_file = "H:\\tes232t\\r_frame187687.exr"
print("selected file is :" + selected_file)
without_extention = selected_file.replace(".exr", "")
my_regex_pattern =  r"\d+\b"
print("no ext = " + str(without_extention))
without_number = re.sub(my_regex_pattern, "-----------" ,without_extention)
#s = without_extention.sub("^\d+\s|\s\d+\s|\s\d+$", " ", s)
print(without_number)
print("========================================")

mijn_sequences = fileseq.findSequencesOnDisk('H:/test/r_frame@.exr')


regex = "\d*\b"

print("fileseq is"  +  str(mijn_sequences))
print(type(mijn_sequences))
print(len(mijn_sequences))
for p in mijn_sequences:

    for u in p:
        pass
        #print("waarde is: " + str(u))
 """


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


print(get_single_file_url(folder, sequences))
print(folder_path)

#print(sequences.dirname(path))



nr_of_sequences = len(sequences)

for i  in sequences:
    
    for x in i:
        folder = "H:\\test\\"
        # filepath = folder + "\\" +  x
        full_file_path = str(folder) + str(x)
        print(denoiser_path)
        print(full_file_path)

        #simple_denoise(denoiser_path,full_file_path)



class Mainwindow(qtw.QMainWindow):
    def __init__(self,*arg,**kwargs):
        super().__init__(*arg,**kwargs)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.select_render_btn.clicked.connect(self.selectRender)
        self.ui.selectDirectory_btn.clicked.connect(self.selectFolder)
        self.ui.denoise_btn.clicked.connect(self.denoiseRender)


        self.denoise_command = []
        self.folderPath = [""]
        self.command_string = ""

        print(self.denoise_command)
        self.show()

    def selectFolder(self):
        catch_folderPath = str(qtw.QFileDialog.getExistingDirectory (self, "Selecteer een Directory"))
        print(catch_folderPath)

        self.folderPath.append(catch_folderPath)
        self.ui.custom_folder_label.setText(catch_folderPath)




    def selectRender(self):
        file = str(qtw.QFileDialog.getOpenFileName (self, "Selecteer een Directory"))
        file_list=file.split(",")
        first_filepath_item = file_list[0]
        print("first_filepath_item is : " + str(first_filepath_item))
        first_filepath_itemUrl = first_filepath_item[1:]

        self.ui.selected_render_label.setText(first_filepath_itemUrl)
        print("label is : " + first_filepath_itemUrl)

        #create render sequence list
        selected_file = first_filepath_itemUrl
        without_extention = selected_file.replace(".exr", "")
        my_regex_pattern =  r"\d+\b"
        sequence_name_with_replaced_number = re.sub(my_regex_pattern, "@.exr" ,without_extention)
        cleaned_sequence = sequence_name_with_replaced_number[1:-1]
        mijn_sequences = fileseq.findSequencesOnDisk(cleaned_sequence)




        print("9999999999999999999999999999")
        print(type(sequence_name_with_replaced_number))
        print("sequence_name_with_replaced_number = " + sequence_name_with_replaced_number)
        print(len(sequence_name_with_replaced_number))
        mijn_woord = "H:/test/r_frame@.exr"
        print(len(mijn_woord))
        print(mijn_sequences)
        for p in mijn_sequences:
            print(" mijn P waarde is: " + str(p))
            for u in p:
                print("ECHTE __________ waarde is: " + str(u))
        print("2222222222222222222222222222")




        render_sequence = pyseq.get_sequences(str(first_filepath_itemUrl))
        #print(pyseq.__dict__)

        print(type(render_sequence))
        print(render_sequence)
        #print(frames(render_sequence))

        # get correctversion of the denoiser .exe
        #denoise_path = self.ui.denoiser1.text()


    def denoiseRender(self):

        # APPEND TO THE CORR MAIN COMMAND
        if (len(self.ui.denoiser1.text()) > 1 and self.ui.denoiser_radio1.isChecked()):
            self.denoise_command.append(self.ui.denoiser1.text())
            print(self.denoise_command)

        if (len(self.ui.denoiser2.text()) > 1 and self.ui.denoiser_radio2.isChecked()):
            self.denoise_command.append(self.ui.denoiser2.text())
            print(self.denoise_command)

        if (len(self.ui.denoiser3.text()) > 1 and self.ui.denoiser_radio3.isChecked()):
            self.denoise_command.append(self.ui.denoiser3.text())
            print(self.denoise_command)

        if (len(self.ui.denoiser4.text()) > 1 and self.ui.denoiser_radio4.isChecked()):
            self.denoise_command.append(self.ui.denoiser4.text())
            print(self.denoise_command)

        if (len(self.ui.denoiser5.text()) > 1 and self.ui.denoiser_radio5.isChecked()):
            self.denoise_command.append(self.ui.denoiser5.text())
            print(self.denoise_command)

        if (len(self.ui.denoiser6.text()) > 1 and self.ui.denoiser_radio6.isChecked()):
            self.denoise_command.append(self.ui.denoiser6.text())
            print(self.denoise_command)

        if (len(self.ui.denoiser7.text()) > 1 and self.ui.denoiser_radio7.isChecked()):
            self.denoise_command.append(self.ui.denoiser7.text())
            print(self.denoise_command)

        if (len(self.ui.denoiser8.text()) > 1 and self.ui.denoiser_radio8.isChecked()):
            self.denoise_command.append(self.ui.denoiser8.text())
            print(self.denoise_command)

        if (len(self.ui.denoiser9.text()) > 1 and self.ui.denoiser_radio9.isChecked()):
            self.denoise_command.append(self.ui.denoiser9.text())
            print(self.denoise_command)

        if (self.ui.radioButton_gpu_yes.isChecked() ):
            self.denoise_command.append("--override gpuIndex 0")

        if (self.ui.radioButton_skipfirst_yes.isChecked()):
            self.denoise_command.append("--skipfirst, -F")

        if (self.ui.radioButton_skiplast_yes.isChecked()):
            self.denoise_command.append("--skiplast, -L")

        if (len(self.ui.textEdit_suffix.text()) > 1):
            self.denoise_command.append(self.ui.textEdit_suffix.text())

        if (self.ui.radioButton_crossframe_yes.isChecked()):
            self.denoise_command.append("--crossframe")

        denoise_filter = self.ui.comboBox_filter.currentText()
        self.denoise_command.append("-f " + str(denoise_filter))

        denoise_premade_filter = self.ui.comboBox_premade_filters.currentText()
        self.denoise_command.append("-f " + str(denoise_premade_filter))

        threads = self.ui.comboBox_threads.currentText()
        self.denoise_command.append("-t " + str(threads))


        dc_denoise_command = ""
        for command_item in self.denoise_command:
            print(command_item)
            spaced_item = " " + str(command_item) + " "

            dc_denoise_command += str(spaced_item)

            #self.command_string.join(command_item)
            folderpath_command = "--outdir " + str(self.folderPath[1])
        clean_denoise_command = dc_denoise_command + folderpath_command

        #adds frames
        final_denoise_command = clean_denoise_command 

        print("clean command is : " + str(clean_denoise_command))

        sequences2 = detect_sequences(self.ui.selected_render_label.text())
        print(sequences2)

        #print("command string is: " + str(self.command_string))

        render_sequence = pyseq.get_sequences("H:\\test")
        print("label is : " + str(self.ui.selected_render_label.text()))
        print(type(render_sequence))
        print(render_sequence)

        for p in range(10):
            print("boom")

        for g in render_sequence:
            print("g is : " + str(g))
            for x in g:
                print("x is : " + str(x))
                folder2 = "H:\\test\\"
                # filepath = folder + "\\" +  x
                full_file_path = str(folder2) + str(x) + ".exr"
                print("full filepath is: " + str(full_file_path))


                final_denoise_command2 = final_denoise_command + " " + full_file_path
                print(final_denoise_command2)
                subprocess.check_output(final_denoise_command2, shell=True) 





#comboBox_filter


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    w = Mainwindow()

    qtmodern.styles.dark(app)
    mw = qtmodern.windows.ModernWindow(w)
    mw.show()
    sys.exit(app.exec_())