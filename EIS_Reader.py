import codecs
import matplotlib.pyplot as plt
from Meth_blue_06_09 import get_data_paths

class EISReader:

    def __init__(self, filename, set_cycle=0):
        with codecs.open(filename, 'r', encoding='utf-8', errors='ignore') as file:
            file_lines = file.readlines()
            header_line = self.get_header_line_number(file_lines)

            self.eis = EISData()
            for line in file_lines[header_line:]:
                if not set_cycle:
                    set_cycle = float(line.split()[10])
                if float(line.split()[10]) == set_cycle:
                    eis_data = [line.split()[0],line.split()[3],line.split()[4]]

                    for data, data_list in zip(eis_data, self.eis.data_list):
                        data_list.append(data)

    def get_header_line_number(self,file_lines):
        for file in file_lines:
            if 'Nb header' in file:
                header_string = str(file)
                split_header_string =header_string.split()
                return int(split_header_string[-1])



class EISData:
    def __init__(self):
        self.frequency = list()
        self.magnitude = list()
        self.phase = list()
        self.data_list = [self.frequency, self.magnitude, self.phase]

