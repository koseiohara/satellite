import numpy as np


def cloud_filter(ch2, threshold):
    output = ch2.observe > threshold

    return output


def land_filter(alb_diff, threshold):
    output = alb_diff < threshold

    return output


