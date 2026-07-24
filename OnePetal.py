#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import math
import logging
import sys
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
    def CountAndFindXArriveMrout(self,x:list):
        phi=x[0]
        theta=x[1]
        count=0
        MroutX=[phi,theta]
        while((not phi%2*math.pi<self.phistar) and not (phi%(2*math.pi)<self.phistar)):
            MroutX = [phi, theta]
            phi+=2*theta
            if(phi==self.phistar or phi==2*math.pi-self.phistar):
                logging.error("The trajecory from %s"%x+" after %d"%count+ "collisions hits a corner.")
                sys.exit(1)
            count+=1
        logging.info("The trajecory from %s"%x+" after %d"%count+ "collisions arrives Mrout at %s"%MroutX)
        return MroutX
