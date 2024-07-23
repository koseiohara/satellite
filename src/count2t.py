import numpy as np


def count2t(calib, satelite, nx, ny):
    temperature = np.empty([ny,nx])
    for j in range(ny):
        for i in range(nx):
            temperature[j,i] = calib[satelite[j,i]]

    return temperature

