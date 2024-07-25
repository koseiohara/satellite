# Satellite Oceanography Homework

This script makes figures from satellite AVHRR data.
Figures are the brightness temperature from channel4 and 5 and the estimated Sea Surface Temperature (SST).
SST is estimated by Multi-Channel SST (MCSST) method.


## Script Files
- main.py  
  The main program to execute the script.

- filein.py  
  A class to read no header binary files.

- AVHRR.py  
  A class to get AVHRR data.
  The calibration table and grid point value are gained from each file and they are decoded.

- ZenithAngle.py  
  Compute the cosine of the zenith angle.
  The nadir angle of the satellite can be computed by
  $$\alpha = 110.8 {\left(x - 1023.5\right) \over 2048}$$
  where 2048 is the number of grids along the scan line and $`x`$ is the index of each grid.
  110.8 is the maximum nadir angle.  
  The sine of the zenith angle is defined by
  $$\sin{\theta_{SZA}} = {h+R \over R} \sin{\alpha}$$

- get\_sst.py  
  SST is estimated by MCSST method from channel 4 and 5 brightness temperatures.

- filter.py
  Get the domain of clouds and lands.

- plot.py  
  make figures

- error.py
  Compute the differences between AVHRR SST and OISST.

- sakaida.py
  A program provided by the lecturer.
  SST is computed from OISST data.


