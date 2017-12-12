from EC_Lab_CVReader import CV_Plotter
import os

ph6_directory = 'E:\\Chrome Download\\Surface Nile Blue\\ph6'
ph7_directory = 'E:\\Chrome Download\\Surface Nile Blue\\ph7'
ph8_directory = 'E:\\Chrome Download\\Surface Nile Blue\\ph8'

ph6_cv_plot = CV_Plotter(os.path.join(ph6_directory, 'CV'))
ph7_cv_plot = CV_Plotter(os.path.join(ph7_directory, 'CV'))
ph8_cv_plot = CV_Plotter(os.path.join(ph8_directory, 'CV'))