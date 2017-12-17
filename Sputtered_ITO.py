from EIS_Reader import EISReader, EISPlotter
import os
from EC_Lab_CVReader import get_data_paths

directory = '/Users/st659/Google Drive/Sputtered ITO/EIS'

plotter = EISPlotter(directory, block=True)
average_plotter = EISPlotter(directory,average=True, legends=['10 O$_{2}$', '10 O$_{2}$ 500 Anneal', '3 O$_{2}$', '5 O$_{2}$'])