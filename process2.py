#!/usr/bin/env python2.7
import sys
import pdb
import argparse
import re
import pandas as pd
import matplotlib.pyplot as plt
import prettyplotlib as ppl
import numpy as np

def calculateProbability(dft):
    length_5min = len(dft.ix[dft.ix[:, "cost"] >= 300, 0])
    totalLen = len(dft)

    length_10min = len(dft.ix[dft.ix[:, "cost"] >= 600, 0])
    time = np.arange(1, 11, 1)
    prob = map(lambda x: "%.3f" % (len(dft.ix[dft.ix[:, "cost"] <= x * 60, 0]) / float(totalLen)), time)
    df = pd.DataFrame({"time cost": time, "probability": prob})
    # for i in range(60, 601, 60):

    # print "take 5 min to respond: %.3f" % (length_5min / float(totalLen))
    # print "take 10 min to respond: %.3f" % length_10min / float(totalLen) 

if __name__ == '__main__':
    o = sys.stdout
    e = sys.stderr
    
    df = pd.read_csv("data.csv")
    dft = df.set_index("timeStamp")
    index = [pd.to_datetime(date) for date in dft.index]
    dft.index = index
    data = dft.groupby(lambda x: x.hour)
    # fig, axes = plt.subplots(nrows = 2, ncols = 1)
    fig, axes = plt.subplots()
    ax = axes
    names = data.groups.keys()
    # values = [dft.ix[index, :] for index in data.groups.values()]
    # lvalues = map(lambda x: x.ix[:, 0].tolist(), values)

    ret = data.boxplot(subplots=False,
                       ax=ax,
                       notch=True
                       )
    # ret = data.boxplot(subplots = False, ax= ax, showcaps = False)
    ax.set_ylim(0, 660)
    ax.set_xticklabels(
        map(lambda x: "%r:00" % x, data.groups.keys()), rotation=30, fontsize='small')
    y_ticks = np.arange(0, 660, 60)
    ax.set_yticks(y_ticks)
    ax.set_yticklabels(map(lambda x: str(x) + ' min', y_ticks / 60))
    ax.set_xlabel("time slots")
    ax.set_ylabel("mapper startup time")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    ax.grid()  # turn grid off
    fig.savefig("mapper_startup_time_distribution.pdf")
