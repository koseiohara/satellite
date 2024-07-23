import matplotlib.pyplot as plt

from get_data    import get_temperature
from ZenithAngle import ZenithCosine
from get_sst     import sst_estimate
from plot        import plot


nx = 2048
ny = 4483

ch4 = get_temperature('../data/N88110903_H_ch4.ex', '../data/N88110903_H_cv4.txt', nx, ny, 1_024)
ch5 = get_temperature('../data/N88110903_H_ch5.ex', '../data/N88110903_H_cv5.txt', nx, ny, 1_024)

ch4.get_calib()
ch5.get_calib()

ch4.get_satellite('uint', 2)
ch5.get_satellite('uint', 2)

ch4.get_temperature()
ch5.get_temperature()

zenith_cos = ZenithCosine(nx)
#for i in range(2_048):
#    print(zenith_cos[i])

sst = sst_estimate(ch4, ch5, zenith_cos, nx, ny)

cmin = -20
cmax = 35
print(ch4.temperature[4400,1000])
plot(ch4.temperature[4390:4410,:], '../output/ch4_temperature.png', 'ch4', cmin, cmax)
#plot(ch5.temperature, '../output/ch5_temperature.png', 'ch5', cmin, cmax)
#plot(sst, '../output/sst_estimate.png', 'AVHRR SST Estimate', cmin, cmax)


