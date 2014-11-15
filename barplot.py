#!/usr/bin/env python2.7
import sys
import pdb
import argparse
import re
import pandas as pd
import matplotlib.pyplot as plt
import prettyplotlib as ppl
import numpy as np

if __name__ == '__main__':
    fig, axes = plt.subplots()
    ppl.bar(axes, [0], [80], label="Redshift", xticklabels=[])
    ppl.bar(axes, [0], [40], bottom=[80],
            color=ppl.colors.set2[1], label="CSV")
    xlim = axes.get_xlim()
    xlim_right = 1.5 * xlim[1]
    newXlim = (xlim[0], xlim_right)
    axes.set_xlim(newXlim)
    axes.set_ylabel("time (s)")
    axes.legend(loc=0, frameon=False)
    fig.savefig("RedshiftCSV_bar.pdf")
