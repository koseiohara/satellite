#from get_data import get_temperature
import numpy as np


def sst_estimate(ch4, ch5, zenith_cos):

    output = np.empty([ch5.ny,ch5.nx])

    for j in range(ch5.ny):
        output[j,:] = 0.994_9 * ch4.observe[j,:]                                                            + \
                      (2.249_1 + 0.485_24/zenith_cos[:] - 0.485_24) * (ch4.observe[j,:] - ch5.observe[j,:]) + \
                      0.631
    
    return output


