###############################################################################
# matplotlib API for xvg format files
# Author: Panyue Wang (pywang@ucdavis.edu)
###############################################################################

import numpy as np
import matplotlib.pyplot as plt
import sys

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
def set_plot_parameters(plot_obj, title, xlabel, ylabel):
    plot_obj.title(title)
    plot_obj.xlabel(xlabel)
    plot_obj.ylabel(ylabel)

# main function
if __name__ == "__main__":
    # setting up plotting parameters
    xvg_input = sys.argv[1]
    title = sys.argv[2]
    xlabel = sys.argv[3]
    ylabel = sys.argv[4]

    x, y = read_xvg(xvg_input)
    plt.plot(x, y)
    set_plot_parameters(plt, title, xlabel, ylabel)
    plt.show()