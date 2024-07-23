import matplotlib.pyplot as plt
import numpy as np


def plot(temperature, figname, title, cmin, cmax):

    cnum = 21

    fig = plt.figure(figsize=[4,6])
    ax = fig.add_subplot(111)
    ax.invert_yaxis()

    #cmap = plt.cm.Spectral.reversed()
    #cmap = 'rainbow'
    #cmap = plt.cm.nipy_spectral.reversed()
    #cmap = 'nipy_spectral'
    cmap = 'viridis'
    #cmap = 'plasma'
    #cmap = plt.cm.gist_rainbow.reversed()

    #cont = ax.contourf(temperature[::-1,:], cmap='viridis', levels=np.linspace(cmin, cmax, cnum), extend='both')
    #cont = ax.contourf(temperature[::-1,:], cmap='Spectral', levels=np.linspace(cmin, cmax, cnum), extend='both')
    #cont = ax.contourf(temperature[::-1,:], cmap=cmap, levels=np.linspace(cmin, cmax, cnum), extend='both')
    cont = ax.contourf(temperature, cmap=cmap, levels=np.linspace(cmin, cmax, cnum), extend='both')
    cbar = fig.colorbar(cont, ax=ax, pad=0.01, aspect=15, ticks=np.linspace(cmin, cmax, 6))

    ax.set_title(title)

    fig.savefig(figname, dpi=350, bbox_inches='tight')

