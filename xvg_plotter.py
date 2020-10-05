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
    x = np.array(x)
    # convert time from ps to ns
    x /= 1000
    # convert rmsd from nm to A
    y = np.array(y)
    y *= 10
    return x, y

# set plot parameters
def set_plot_parameters(plot_obj, xlabel, ylabel):
    fontsize = 14
    plot_obj.xticks(fontsize=fontsize)
    plot_obj.yticks(fontsize=fontsize)
    plot_obj.subplots_adjust(bottom=0.15, left=0.1, top=0.95)
    #plot_obj.title(title, fontsize=16)
    plot_obj.xlabel(xlabel, fontsize=fontsize)
    plot_obj.ylabel(ylabel, fontsize=fontsize)

# main function
if __name__ == "__main__":
    # setting up plotting parameters
    xvg_input = sys.argv[1]
    filename = sys.argv[2]
    xlabel = sys.argv[3]
    ylabel = sys.argv[4]
    if len(sys.argv) > 5:
        save_fig = True
    else:
        save_fig = False

    x, y = read_xvg(xvg_input)
    plt.plot(x, y)
    set_plot_parameters(plt, xlabel, ylabel)
    if save_fig:
        plt.savefig(filename + ".jpg", dpi=250)
    else:
        plt.show()
