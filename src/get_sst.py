#from get_data import get_temperature
import numpy as np


def sst_estimate(ch4, ch5, zenith_cos, nx, ny):

    output = np.empty([ny,nx])

    for j in range(ny):
        output[j,:] = 0.994_9 * ch4.temperature[j,:]                                                                + \
                      (2.249_1 + 0.485_24/zenith_cos[:] - 0.485_24) * (ch4.temperature[j,:] - ch5.temperature[j,:]) + \
                      0.631
    
    return output


