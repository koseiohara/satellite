import numpy as np
import matplotlib.pyplot as plt


def rmse(estim, real, cloud, land):
    estim_domain = estim[(~ cloud) & (~ land)]
    real_domain  =  real[(~ cloud) & (~ land)]

    diff = estim_domain[:] - real_domain[:]
    len = np.size(diff[:])

    output = np.sqrt(np.sum(diff[:]*diff[:])/len)

    print('RMSE : ', output)

    return output


    #y = int(np.size(estim_domain)/300)
    #x = int(np.size(estim_domain)/3)
    ##plt.contourf(np.reshape(estim_domain[:300*y], [300, y]), cmap='bwr', levels=np.linspace(-35, 35, 51))
    #plt.contourf(np.reshape(estim_domain[:], [3, x]), cmap='bwr', levels=np.linspace(-35, 35, 51))
    #plt.savefig('estim.png')
    ##plt.contourf(np.reshape(real_domain[:300*y], [300, y]), cmap='bwr', levels=np.linspace(-35, 35, 51))
    #plt.contourf(np.reshape(real_domain[:], [3,x]), cmap='bwr', levels=np.linspace(-35, 35, 51))
    ##plt.contourf(real_domain, cmap='bwr', levels=np.linspace(-35, 35, 51))
    #plt.savefig('real.png')

