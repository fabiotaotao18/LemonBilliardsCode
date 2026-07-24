#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import math
import logging
import sys
import LemonSingularities
rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
rc('text', usetex=True)
plt.rcParams["figure.dpi"] = 500
plt.rcParams['axes.linewidth'] = 0.1
class OnePetalObj(object):
    def __init__(self, phistar):
        # self.R=R
        self.phistar=phistar
        self.expansion=1.0
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
        while((not phi%(2*math.pi)<self.phistar) and (not phi%(2*math.pi)>(2.0*math.pi-self.phistar))):
            MroutX = [phi, theta]
            phi=(phi+2*theta)%(2*math.pi)
            if(phi==self.phistar or phi==2*math.pi-self.phistar):
                logging.error("The trajectory from %s"%x+" after %d"%count+ " shears collisions hits a corner.")
                sys.exit(1)
            count+=1
        # print((not phi%(2*math.pi)<self.phistar) and (not phi%(2*math.pi)>(2.0*math.pi-self.phistar)))
        logging.warning("The trajectory from Mrin: %s"%x+" after %d"%count+ " shears collisions arrives Mrout at %s"%MroutX)
        return MroutX
    def GetMfPositionAngle(self,MroutX:list):
        MfTheta=2*math.pi-(MroutX[0]+MroutX[1])
        if(MfTheta<0 or MfTheta>math.pi):
            logging.error("Incorrect MroutX: %s"%MroutX)
            sys.exit(1)
        tau0=(-1.0*math.cos(MroutX[0])+math.cos(self.phistar))/math.sin(MfTheta)
        MfX=1.0*math.sin(MroutX[0])-tau0*math.cos(MroutX[0]+MroutX[1]-math.pi)
        # MfX=(-1.0*math.cos(MroutX[0])+math.cos(self.phistar))*1.0/math.tan(MfTheta)
        d0=math.sin(MroutX[1])
        return[d0,tau0,MfX,MfTheta]
    def GetMrinXFromMfPositionAngle(self,Mfs:list):
        [d0,tau0, MfX, MfTheta]=Mfs;
        # print(MfX)
        # print ([2*MfX*math.cos(MfTheta)-2*math.cos(self.phistar)*math.sin(MfTheta),MfX**2-math.sin(self.phistar)**2])
        tau1=LemonSingularities.QuadraticPolynomialOneRoot(2*MfX*math.cos(MfTheta)-2*math.cos(self.phistar)*math.sin(MfTheta),MfX**2-math.sin(self.phistar)**2)
        # print([d0,tau0,tau1])
        logging.warning("The expansion at Mf %s"%Mfs+" is %f"%(1+(tau0+tau1-2*d0)/d0))
        self.expansion*=(1+(tau0+tau1-2*d0)/d0)
        x2=MfX+tau1*math.cos(MfTheta)
        y2=-1.0*math.cos(self.phistar)+tau1*math.sin(MfTheta)
        phi2=(math.atan2(y2,x2)%(2*math.pi)+math.pi/2)%(2*math.pi)
        theta2=phi2-MfTheta
        MrinX=[phi2,theta2]
        logging.warning("The trajectory from Mf: %s" % Mfs+" arrives Mrin at %s" % MrinX)
        return MrinX
    def VerifyNStepFlatTransitionExpansion(self,N):
        self.expansion=1.0
        start = [3 * self.phistar, self.phistar]
        for i in range(N):
            MroutX = self.CountAndFindXArriveMrout(start)
            MfX = self.GetMfPositionAngle(MroutX)
            MrinX = self.GetMrinXFromMfPositionAngle(MfX)
            start = MrinX
        print("Accumulation of Expansion is at least %f"%self.expansion+" in %d"%N+" flat transition steps.")
def VerifyPhistarFeasibilityInNStepTransition(phistar,N):
    PBobj = OnePetalObj(phistar)
    PBobj.VerifyNStepFlatTransitionExpansion(N)


if __name__ == '__main__':
    # phistar=math.pi/20.1
    VerifyPhistarFeasibilityInNStepTransition(math.pi/25.13, 4)