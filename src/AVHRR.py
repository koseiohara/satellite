import numpy as np
from filein import filein as filein


class AVHRR:

    def __init__(self, satellite, table, nx, ny, tablelen):
        
        self.__satel_fname = satellite                # filename
        self.__table_fname = table                    # filename
        self.nx            = nx
        self.ny            = ny
        self.cnv_table     = np.empty(tablelen)
        self.code          = np.empty([ny,nx], dtype=int)
        self.observe       = np.empty([ny,nx])


    def get_table(self):
        table = np.loadtxt(self.__table_fname, delimiter=',')
        self.cnv_table[:] = table[:,1]


    def get_code(self, dtype, kind):
        
        shape = [self.ny,self.nx]
        recl = self.nx * self.ny * kind
        rec = 1
        endian = 'LITTLE'
        recstep = 1
        #form = dtype + '{}'.format(kind << 3)
        #print('shape :', shape)
        #print('recl : ', recl)
        #print('form : ', form)
        satellite = filein(self.__satel_fname, shape, recl, rec, dtype, kind, endian, recstep)

        self.code[:,:] = satellite.fread()
        #self.satellite[:,:] = np.array(self.satellite[:,:], dtype=int)


    def decode(self):
        for j in range(self.ny):
            for i in range(self.nx):
                #print(self.satellite[j,i])
                self.observe[j,i] = self.cnv_table[self.code[j,i]]

