import numpy as np

def ZenithCosine(pixels):
    EarthRadius = 6_378_000.
    SatelliteHight = 850_000.

    alpha = NadirAngle(pixels)

    zenith_sin = (SatelliteHight + EarthRadius) * np.sin(alpha) / EarthRadius
    output = np.sqrt(1. - zenith_sin*zenith_sin)

    return output


def NadirAngle(pixels):
    grids = np.linspace(0., pixels-1., pixels)
    NADIR_MAX = 110.8

    output = NADIR_MAX * (grids - (pixels-1)*0.5) / pixels
    output = output * np.pi / 180.

    return output

