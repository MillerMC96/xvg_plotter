###############################################################################
# matplotlib API for xvg format files
# Author: Panyue Wang (pywang@ucdavis.edu)
###############################################################################

import numpy as np
import matplotlib.pyplot as plt

# read xvg file
# data entry
for line in lines:
    line_entry = line.split()
    # skip comments
    first_charactor = line_entry[0]
    if first_charactor[0] != '#' and first_charactor[0] != '@':

# set plot parameters

# main function