import numpy as np


def bias(estim, real):

    output = np.mean(estim[:] - real[:])

    return output


def rmse(estim, real):

    diff = estim[:] - real[:]
    #len = np.size(diff[:])

    #output = np.sqrt(np.sum(diff[:]*diff[:])/len)
    output = np.sqrt(np.mean(diff[:]*diff[:]))

    return output


def standardDeviation(estim, real):

    diff = estim[:] - real[:]
    #len = np.size(diff[:])

    mean_diff = np.mean(diff[:])

    #output = np.sqrt(np.sum((diff[:]-mean_diff)**2)/len)
    output = np.sqrt(np.mean((diff[:]-mean_diff)**2))
    return output


def masking(observe, cloud, land):
    
    output= observe[(~ cloud) & (~ land)]
    return output
    
