#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import math
rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
rc('text', usetex=True)
plt.rcParams["figure.dpi"] = 500
plt.rcParams['axes.linewidth'] = 0.1
class OnePetalObj(object):
    def __init__(self, phistar):
        # self.R=R
        self.phistar=phistar
        # self.Phistar=np.arcsin(math.sin(phistar) / R)
    def plotphaseMr(self):
        thetaline=np.linspace(0, math.pi, 500)
        phiconstant=np.linspace(self.phistar, 2*math.pi-self.phistar, 500)
        plt.plot(phiconstant, thetaline,'k', lw=0.2)

