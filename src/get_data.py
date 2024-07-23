import numpy as np
from filein import filein as filein


class get_temperature:

    def __init__(self, satellite, calib, nx, ny, clen):
        
        self.__satel_fname = satellite                # filename
        self.__calib_fname = calib                    # filename
        self.__nx          = nx
        self.__ny          = ny
        self.temperature   = np.empty([ny,nx])
        self.satellite     = np.empty([ny,nx])
        self.calib         = np.empty(clen)


    def get_calib(self):
        ctmap = np.loadtxt(self.__calib_fname, delimiter=',')
        self.calib[:] = ctmap[:,1]


    def get_satellite(self, dtype, kind):
        
        shape = [self.__ny,self.__nx]
        recl = self.__nx * self.__ny * kind
        rec = 1
        endian = 'LITTLE'
        recstep = 1
        #form = dtype + '{}'.format(kind << 3)
        #print('shape :', shape)
        #print('recl : ', recl)
        #print('form : ', form)
        satellite = filein(self.__satel_fname, shape, recl, rec, dtype, kind, endian, recstep)

        self.satellite[:,:] = satellite.fread()
        #self.satellite[:,:] = np.array(self.satellite[:,:], dtype=int)


    def get_temperature(self):
        for j in range(self.__ny):
            for i in range(self.__nx):
                #print(self.satellite[j,i])
                self.temperature[j,i] = self.calib[int(self.satellite[j,i])]

