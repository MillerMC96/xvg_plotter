###############################################################################
# matplotlib API for xvg format files
# Author: Panyue Wang (pywang@ucdavis.edu)
###############################################################################

import numpy as np
import matplotlib.pyplot as plt

# read xvg file

def read_xvg(xvg_file):
    xvg_file_obj = open(xvg_file, 'r')
    lines = xvg_file_obj.readlines()
    # x axis
    x = []
    # y axis
    y = []
    # data entry
    for line in lines:
        line_entry = line.split()
        # skip comments
        first_charactor = line_entry[0]
        if first_charactor[0] != '#' and first_charactor[0] != '@':
            x.append(float(line_entry[0]))
            y.append(float(line_entry[1]))

    return x, y



# set plot parameters

# main function