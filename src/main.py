import matplotlib.pyplot as plt
import numpy as np

from AVHRR       import AVHRR
from filter      import cloud_filter, land_filter
from ZenithAngle import ZenithCosine
from get_sst     import sst_estimate
from plot        import plot
from sakaida     import sakaida
from rmse        import rmse


nx = 2048
ny = 4483

ch1 = AVHRR('../data/N88110903_H_ch1.ex', '../data/N88110903_H_cv1.txt', nx, ny, 1_024)
ch2 = AVHRR('../data/N88110903_H_ch2.ex', '../data/N88110903_H_cv2.txt', nx, ny, 1_024)
ch4 = AVHRR('../data/N88110903_H_ch4.ex', '../data/N88110903_H_cv4.txt', nx, ny, 1_024)
ch5 = AVHRR('../data/N88110903_H_ch5.ex', '../data/N88110903_H_cv5.txt', nx, ny, 1_024)

ch1.get_table()
ch2.get_table()
ch4.get_table()
ch5.get_table()

ch1.get_code('uint', 2)
ch2.get_code('uint', 2)
ch4.get_code('uint', 2)
ch5.get_code('uint', 2)

ch1.decode()
ch2.decode()
ch4.decode()
ch5.decode()

ch1.observe = ch1.observe * 0.01
ch2.observe = ch2.observe * 0.01

#threshold = 0.15
#threshold = 0.1
threshold = 0.07
cloud = cloud_filter(ch2, threshold)

zenith_cos = ZenithCosine(nx)

sst = sst_estimate(ch4, ch5, zenith_cos)

#threshold = -0.005
threshold = -0.002
alb_diff = ch1.observe - ch2.observe
land = land_filter(alb_diff, threshold)


real = sakaida()

error = rmse(sst, real, cloud, land)


#plot(ch1.observe, '../output/ch1_albedo.png'     , 'ch1'               ,      0.,      1, cloud, land)
#plot(ch2.observe, '../output/ch2_albedo.png'     , 'ch2'               ,      0.,    0.1, cloud, land)
#plot(ch4.observe, '../output/ch4_temperature.png', 'ch4'               ,     -35,     35, cloud, land)
#plot(ch5.observe, '../output/ch5_temperature.png', 'ch5'               ,     -35,     35, cloud, land)
plot(sst        , '../output/sst_estimate.png'   , 'AVHRR SST Estimate',     -35,     35, cloud, land)
#plot(alb_diff   , '../output/alb_ch1mch2.png'    , 'Albedo ch1 - ch2'  , -0.0001, 0.0001, cloud, land)


