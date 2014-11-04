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
  o = sys.stdout
  e = sys.stderr

  parser= argparse.ArgumentParser(description="")
  parser.add_argument("file", help="")
  args = parser.parse_args() 
  pattern = re.compile("""(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}).*took (\d+)\..*""")
  o.write("timeStamp,cost\n")
  with open (args.file) as IN: 
    for line in IN.readlines():
      m = pattern.search(line)
      if m:
        o.write("%s,%s\n" % (m.group(1), m.group(2)))
      else:
        e.write("Regex matching error!")
 
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

  ret = data.boxplot(subplots = False, ax= ax, notch = True, showcaps = False)
  # ret = data.boxplot(subplots = False, ax= ax, showcaps = False)
  ax.set_ylim(0, 660)
  ax.set_xticklabels(data.groups.keys())
  y_ticks = np.arange(0, 660, 60)
  ax.set_yticks(y_ticks)
  ax.set_yticklabels(map(lambda x: str(x) + ' min', y_ticks/60))
  ax.set_xlabel("time slots")
  ax.set_ylabel("mapper startup time")
  ax.spines["top"].set_visible(False)
  ax.spines["right"].set_visible(False)
  ax.yaxis.set_ticks_position('left')
  ax.xaxis.set_ticks_position('bottom')
  ax.grid() # turn grid off
  fig.savefig("mapper_startup_time_distribution.pdf")
