import matplotlib.pyplot as plt
import numpy as np


def plot(observe, figname, title, cmin, cmax, cloud, land):

    observe = np.ma.masked_where(cloud | land, observe)
    land    = np.ma.masked_where(cloud, land)

    cnum = 51

    fig = plt.figure(figsize=[4,6])
    ax = fig.add_subplot(111)
    #ax.invert_yaxis()
    ax.invert_xaxis()

    #cmap = plt.cm.Spectral.reversed()
    #cmap = 'rainbow'
    #cmap = plt.cm.nipy_spectral.reversed()
    #cmap = 'nipy_spectral'
    cmap = 'viridis'
    cmap = 'bwr'
    cmap = plt.cm.bwr
    #cmap = 'plasma'
    #cmap = plt.cm.gist_rainbow.reversed()

    #cmap.set_over('black')
    #cmap.set_under('white')
    #cmap.set_bad('black')

    ax.contourf(cloud[::4,::4], colors='white')
    ax.contourf( land[::4,::4], colors='black')

    cont = ax.contourf(observe[::4,::4], cmap=cmap, levels=np.linspace(cmin, cmax, cnum), extend='both')
    #cont = ax.contourf(observe[::4,::4], cmap=cmap, levels=np.linspace(cmin, cmax, cnum))
    cbar = fig.colorbar(cont, ax=ax, pad=0.01, aspect=20, ticks=np.linspace(cmin, cmax, 6), extendrect=True)

    #ax.contourf(cloud[::4,::4], colors='white', levels=[True, False])
    #ax.contourf( land[::4,::4], colors='black', levels=[True, False])

    ax.set_title(title)

    fig.savefig(figname, dpi=350, bbox_inches='tight')

