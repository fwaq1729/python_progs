
#  This file is part of plot_nbody.py.
# 
#  Copyright (C) 2025 Fredy W. Aquino
# 
#  nbody is free software: you can redistribute it and/or modify it under
#  the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
# 
#  nbody is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
# 
#  You should have received a copy of the GNU Lesser General Public License
#  along with nbody.  If not, see <https://www.gnu.org/licenses/>.
#
#  Description : Plotting Analytical solutions to Gravitational N-Body problem
#  Date        : 10-07-25

import sys
import json
import matplotlib.pyplot as plt

def nbody_plot(fname):
  list_color_for_plotting = ["blue", "green", "red", "purple", "brown", "olive"]
  with open(fname, "r") as file:
    data = json.load(file)
  ndata = len([*data])
  nbody = int(len(data["step_0"]["positions"]) / 3)
  nplot_row = 3
  nplot_col = 3
  nframes = nplot_row * nplot_col
  d_ndata = (int)(ndata / nframes)
  plot_range = 4
  xtick_pos = [-plot_range + i for i in range(nframes)]
  ytick_pos = [-plot_range + i for i in range(nframes)]
  fig, axes = plt.subplots(nrows=nplot_row, ncols=nplot_col, figsize=(8, 8)) 
  j = 0
  for irow in range(0, nplot_row):
    for icol in range(0, nplot_col):
      ndata1 = j * d_ndata
      axes[irow, icol].plot(0, 0, color = 'black', marker = '.', markersize = 4, linestyle='None')
      if j == 0:
        pos = data["step_0"]["positions"]
        xdata = pos[0 : nbody]
        ydata = pos[nbody : 2 * nbody];
        axes[irow, icol].plot(xdata, ydata, color = 'black')
        axes[irow, icol].plot([xdata[nbody - 1], xdata[0]],
                              [ydata[nbody - 1], ydata[0]], color = 'black')      
      for i in range(0, ndata1):
        tag = "step_" + str(i)
        pos = data[tag]["positions"]
        xdata = pos[0 : nbody]
        ydata = pos[nbody : 2 * nbody];
        if i == ndata1 - 1:
          axes[irow, icol].plot(xdata, ydata, color = 'black')
          axes[irow, icol].plot([xdata[nbody - 1], xdata[0]],
                                [ydata[nbody - 1], ydata[0]], color = 'black')
        for k in range(0, nbody):
          axes[irow, icol].plot(xdata[k], ydata[k],
                                color = list_color_for_plotting[k],
                                marker = '.', markersize = 2, linestyle='None')
      axes[irow, icol].set_xlim(-plot_range, plot_range)
      axes[irow, icol].set_ylim(-plot_range, plot_range)
      axes[irow, icol].set_xticks(xtick_pos)
      axes[irow, icol].set_yticks(ytick_pos)
      axes[irow, icol].tick_params(axis='both', labelsize = 8)
      j += 1
  fig.suptitle('Trajectories of N bodies (around center-of-mass), N = %d'%nbody, x = 0.5, y = 0.92)
  plt.show()

if __name__ == '__main__':
  if len(sys.argv) < 2:
    sys.exit('specify Nbody case (e.g. 0, 1, 2, ..., 6)')
  case_data = (int)(sys.argv[1])
  if (not(case_data == 0 or case_data == 1 or case_data == 2 or
          case_data == 3 or case_data == 4 or case_data == 5 or
          case_data == 6)):
    print('Error case_data ne 0, 1, 2, 3, 4, 5 , 6')
    sys.exit()
  fname = "./data/nbody_output_case_%d.json"%case_data
  print('Reading fname = %s'%fname)
  nbody_plot(fname)
