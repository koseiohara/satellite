import numpy as np


def cloud_filter(target, ch2, threshold, undef):
    output = np.where(ch2.observe > threshold, undef, target.observe)
    output = ch2.observe > threshold

    return output


def land_filter(target, alb_diff, threshold, undef):
    output = np.where(alb_diff < threshold, undef, target.observe)
    output = alb_diff < threshold

    return output


