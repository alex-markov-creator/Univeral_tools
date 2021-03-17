#-*- coding: utf-8 -*-
"""
*py - name file
"""
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

fig = plt.figure(constrained_layout=True)

gs = GridSpec(3,3, figure=fig)
ax1 = fig.add_subplot(gs[0, :])
#
ax2 = fig.add_subplot(gs[1, :-1])
ax3 = fig.add_subplot(gs[1:, -1])
ax4 = fig.add_subplot(gs[-1, 0])
ax5 = fig.add_subplot(gs[-1, -2])

fig.suptitle("GridSpec")

plt.show()
