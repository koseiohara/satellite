# Satellite Oceanography Homework

This script makes figures from satellite AVHRR data.
Figures are the brightness temperature from channel4 and 5 and the estimated Sea Surface Temperature (SST).
SST is estimated by Multi-Channel SST (MCSST) method.


## Script Files
- main.py  
  The main program to execute the script.

- filein.py  
  A class to read no header binary files.

- get\_data.py  
  A class to get brightness temperature data.
  The calibration table and grid point value are gained from each file and they are converted to the brightness temperature field.

- get\_sst.py  
  SST is estimated by MCSST method from channel 4 and 5 brightness temperatures.

- plot.py  
  make figures

