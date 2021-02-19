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
from PyQt5.QtWidgets import QMessageBox
import importlib


import fsutil
from pathlib import Path

from pprint import pprint
from interface import Ui_MainWindow

import qtmodern.styles
import qtmodern.windows


root = Path()
if getattr(sys, 'frozen', False):
    root = Path(sys._MEIPASS)
    qtmodern.styles._STYLESHEET = root / 'qtmodern/style.qss'
    qtmodern.windows._FL_STYLESHEET = root / 'qtmodern/frameless.qss'



logical_processors_count = os.cpu_count()
logical_processors_count_default = logical_processors_count -2


A_path = os.environ.get('DC_RENDERMAN_DENOISER_1')
B_path = os.environ.get("DC_RENDERMAN_DENOISER_2")
C_path = os.environ.get("DC_RENDERMAN_DENOISER_3")
D_path = os.environ.get("DC_RENDERMAN_DENOISER_4")
E_path = os.environ.get("DC_RENDERMAN_DENOISER_5")
F_path = os.environ.get("DC_RENDERMAN_DENOISER_6")
G_path = os.environ.get("DC_RENDERMAN_DENOISER_7")
H_path = os.environ.get("DC_RENDERMAN_DENOISER_8")
I_path = os.environ.get("DC_RENDERMAN_DENOISER_9")




mijn_sequences = ""

RenderManProServerFolder = r"C:\Program Files\Pixar\RenderManProServer-23.1"
denoiser_path = RenderManProServerFolder + r"\bin\denoise.exe"

noisefilter = r"C:\Program Files\Pixar\RenderManProServer-23.1\lib\denoise\splitVariances.filteroverride.json"
noise_filter_path = RenderManProServerFolder + "\lib\denoise\\"

def simple_denoise(denoiser_path, filename):
    command = f'"{denoiser_path}" --crossframe -v variance --override gpuIndex 1 -t 6 -f "{noisefilter}" "{filename}"'
    print(command)
    subprocess.check_output(command, shell=True)


def detect_sequences(pad): # geeft een pad aan en ontvang alle sequences uit dat pad.
    seq = pyseq.get_sequences(pad) # dit is een pad waar meerdere sequences in bestaan

    return seq



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
        print("folderpath: " + str(self.folderPath))
        print("custom folder label is: " +  self.ui.custom_folder_label.text())
        self.ui.comboBox_threads.setCurrentIndex(logical_processors_count_default)

        self.show()



    def selectFolder(self):
        catch_folderPath = str(qtw.QFileDialog.getExistingDirectory (self, "Selecteer een Directory"))
        self.folderPath.append(catch_folderPath)
        self.ui.custom_folder_label.setText(catch_folderPath)




    def selectRender(self):

        #gets the render file
        file = str(qtw.QFileDialog.getOpenFileName (self, "Selecteer een Directory"))
        file_list=file.split(",")
        first_filepath_item = file_list[0]
        print("first_filepath_item is : " + str(first_filepath_item))
        first_filepath_itemUrl = first_filepath_item[1:]

        #Adds the render sequence path to the UI
        self.ui.selected_render_label.setText(first_filepath_itemUrl)
        print("label is : " + first_filepath_itemUrl)

        #create the real render sequence list
        selected_file = first_filepath_itemUrl
        without_extention = selected_file.replace(".exr", "")
        my_regex_pattern =  r"\d+\b"
        sequence_name_with_replaced_number = re.sub(my_regex_pattern, "@.exr" ,without_extention)
        cleaned_sequence = sequence_name_with_replaced_number[1:-1]
        mijn_sequences = fileseq.findSequencesOnDisk(cleaned_sequence)

        for p in mijn_sequences:
            for u in p:
                pass

        self.mijn_sequences = mijn_sequences




    def denoiseRender(self):

        # APPEND TO THE CORR MAIN COMMAND

        if (len(self.ui.denoiser1.text()) > 1):
            Denoiser1_value = self.ui.denoiser1.text()
        else:
            Denoiser1_value = A_path

        if (len(self.ui.denoiser2.text()) > 1):
            Denoiser2_value = self.ui.denoiser2.text()
        else:
            Denoiser2_value = B_path

        if (len(self.ui.denoiser3.text()) > 1):
            Denoiser3_value = self.ui.denoiser3.text()
        else:
            Denoiser3_value = C_path

        if (len(self.ui.denoiser4.text()) > 1):
            Denoiser4_value = self.ui.denoiser4.text()
        else:
            Denoiser4_value = D_path

        if (len(self.ui.denoiser5.text()) > 1):
            Denoiser5_value = self.ui.denoiser5.text()
        else:
            Denoiser5_value = E_path

        if (len(self.ui.denoiser6.text()) > 1):
            Denoiser6_value = self.ui.denoiser6.text()
        else:
            Denoiser6_value = F_path

        if (len(self.ui.denoiser7.text()) > 1):
            Denoiser7_value = self.ui.denoiser7.text()
        else:
            Denoiser7_value = G_path

        if (len(self.ui.denoiser8.text()) > 1):
            Denoiser8_value = self.ui.denoiser8.text()
        else:
            Denoiser8_value = H_path

        if (len(self.ui.denoiser9.text()) > 1):
            Denoiser9_value = self.ui.denoiser9.text()
        else:
            Denoiser9_value = I_path


        print("Denoiser1 waarde is:" + str(Denoiser1_value))

        if (len(self.ui.denoiser1.text()) > 1 and self.ui.denoiser_radio1.isChecked()):

            denoiser1_withMarks =  '"' + Denoiser1_value + '" '
            self.denoise_command.append(denoiser1_withMarks)
            print(self.denoise_command)

        if (len(self.ui.denoiser2.text()) > 1 and self.ui.denoiser_radio2.isChecked()):

            denoiser2_withMarks =  '"' + Denoiser2_value + '" '
            self.denoise_command.append(denoiser1_withMarks)
            print(self.denoise_command)

        if (len(self.ui.denoiser3.text()) > 1 and self.ui.denoiser_radio3.isChecked()):

            denoiser3_withMarks =  '"' + Denoiser3_value + '" '
            self.denoise_command.append(denoiser3_withMarks)
            print(self.denoise_command)

        if (len(self.ui.denoiser4.text()) > 1 and self.ui.denoiser_radio4.isChecked()):

            denoiser4_withMarks =  '"' + Denoiser4_value + '" '
            self.denoise_command.append(denoiser4_withMarks)
            print(self.denoise_command)

        if (len(self.ui.denoiser5.text()) > 1 and self.ui.denoiser_radio5.isChecked()):

            denoiser5_withMarks =  '"' + Denoiser5_value + '" '
            self.denoise_command.append(denoiser5_withMarks)
            print(self.denoise_command)

        if (len(self.ui.denoiser6.text()) > 1 and self.ui.denoiser_radio6.isChecked()):

            denoiser6_withMarks =  '"' + Denoiser6_value + '" '
            self.denoise_command.append(denoiser6_withMarks)
            print(self.denoise_command)

        if (len(self.ui.denoiser7.text()) > 1 and self.ui.denoiser_radio7.isChecked()):

            denoiser7_withMarks =  '"' + Denoiser7_value + '" '
            self.denoise_command.append(denoiser7_withMarks)
            print(self.denoise_command)

        if (len(self.ui.denoiser8.text()) > 1 and self.ui.denoiser_radio8.isChecked()):

            denoiser8_withMarks =  '"' + Denoiser8_value + '" '
            self.denoise_command.append(denoiser8_withMarks)
            print(self.denoise_command)

        if (len(self.ui.denoiser9.text()) > 1 and self.ui.denoiser_radio9.isChecked()):

            denoiser9_withMarks =  '"' + Denoiser9_value + '" '
            self.denoise_command.append(denoiser9_withMarks)
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
        denoise_filter_withPath = '"' + noise_filter_path + denoise_filter + ".filter.json" + '" '
        self.denoise_command.append("-f " + str(denoise_filter_withPath))

        denoise_premade_filter = '"' + noise_filter_path +  self.ui.comboBox_premade_filters.currentText() + '" '
        self.denoise_command.append("-f " + str(denoise_premade_filter))

        threads = self.ui.comboBox_threads.currentText()
        self.denoise_command.append("-t " + str(threads))


        # build the final denoise comand as a string -----
        dc_denoise_command = ""
        for command_item in self.denoise_command:
            print(command_item)
            spaced_item = " " + str(command_item) + " "

            dc_denoise_command += str(spaced_item)

            #self.command_string.join(command_item)
            if self.ui.custom_folder_label.text() != "..." :
                folderpath_command = "--outdir " + str(self.folderPath[1])
            if self.ui.custom_folder_label.text() == "..." :
                folderpath_command = " "

        clean_denoise_command = dc_denoise_command + folderpath_command

        #adds frames
        final_denoise_command = clean_denoise_command 

        # for every sequence deo teh command

        for render_item in self.mijn_sequences:
            print("render_item is: " + str(render_item))
            for render_file in render_item:
                print("render_file value is: " + str(render_file))
                clean_render_file = render_file.replace("/", "\\")
                print(clean_render_file)
                batch_command = final_denoise_command + " " + clean_render_file
                print("batch command is: " + batch_command)
                subprocess.check_output(batch_command, shell=True)

        sequences2 = detect_sequences(self.ui.selected_render_label.text())
        print(sequences2)

        #print("command string is: " + str(self.command_string))

        render_sequence = pyseq.get_sequences("H:\\test")
        print("label is : " + str(self.ui.selected_render_label.text()))
        print(type(render_sequence))
        print(render_sequence)

    def show_missing_exe():
        pass

#comboBox_filter


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    w = Mainwindow()

    qtmodern.styles.dark(app)
    mw = qtmodern.windows.ModernWindow(w)
    mw.show()
    sys.exit(app.exec_())