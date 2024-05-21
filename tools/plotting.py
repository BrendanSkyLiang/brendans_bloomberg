import sys
sys.path.append(r'/Users/brendanliang/Code/brendans_bloomberg') 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from interface.company import Company
from interface.indicator import Yahoo_Indicator


def plotter(ax,  years, shs_out, labels, data, n):
    if len(labels) != len(data):
        raise ValueError("labels and data must be the same length")
    for i in range(len(labels)):
        ax.plot(years, np.array(data[i])/np.array(shs_out), label=labels[i])
        ax.legend(fontsize="5")
        ax.grid()