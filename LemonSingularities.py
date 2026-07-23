#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
rc('text', usetex=True)
plt.rcParams["figure.dpi"] = 500
plt.rcParams['axes.linewidth'] = 0.1
# plt.rcParams["figure.figsize"] = (3,5.5)
import math
def QuadraticPolynomialOneRoot(b,c):
    x1=(-b + math.sqrt(b**2.0-4.0*c))/2.0
    return x1
def generate_theta(n,Phi,Phistar):
    return (Phi+Phistar)/(2.0*n)
class LemmonObj(object):
    def __init__(self, R, phistar):
        self.R=R
        self.phistar=phistar
        self.Phistar=np.arcsin(math.sin(phistar) / R)
    def plotphaseMr(self):
        thetaline=np.linspace(0, self.phistar, 500)
        phiconstant=np.linspace(self.phistar, self.phistar, 500)
        plt.plot(phiconstant, thetaline,'k', lw=0.2)
        # plt.axvline(x=self.phistar, ymin=0, ymax=self.phistar,
        #             label='theta')
def PlotSingularcurve(n,R,LemonObjInstance,color,samplesize):
    # R=13000
    # n=1
    phistar=LemonObjInstance.phistar
    Phistar = np.arcsin(math.sin(phistar)/R)
    b = R*np.cos(Phistar) - np.cos(phistar)
    # LBobj=LemmonBilliard(phistar,R)
    PhiL = Phistar - 2 * Phistar / (n + 1.0)
    Phi1 = np.linspace(PhiL, Phistar, samplesize)
    theta1 = (Phi1 + Phistar) / (2.0 * n)
    c1 = 2.0 * (-R * np.sin(theta1) + b * np.sin(Phi1 + theta1))
    c2 = R ** 2 - 2.0 * b * R * np.cos(Phi1) + b ** 2 - 1
    L1 = (np.sqrt(np.square(c1) - 4.0 * c2) - c1) / 2.0
    # print(L1)
    # print(len(L1))
    xQ = (L1 * np.cos(Phi1 + theta1) + R * np.sin(Phi1))
    yQ = (L1 * np.sin(Phi1 + theta1) + b - R * np.cos(Phi1))
    # print(xQ)
    # print(xQ[-1]**2+yQ[-1]**2)
    # print(xQ[0])
    # print(xQ[-1])
    # print(np.square(yQ)+np.square(xQ))
    # print(math.sin(phistar))

    phi2 = np.arcsin(xQ)
    theta2 = phi2 - (Phi1 + theta1)
    # print(theta2[-1])
    slopes = 1 - np.sin(theta2) / (L1 - (2 * n) / (2 * n + 1) * R * np.sin(theta1))
    slopedenominator = (L1 - (2 * n) / (2 * n + 1) * R * np.sin(theta1))

    # print(30000/(math.sin(phistar)**2))
    # print ((theta2[0]-theta2[2])/(phi2[0]-phi2[2]))
    # print(slopes[0])
#    print(slopedenominator[0])
 #   print(2 * (n + 1) / (2 * n + 1) * R * np.sin(Phistar / (n + 1)))
    # plt.plot(phi2, theta2, "b-", lw=0.5)
    # fig, ax = plt.subplots()
    # ax.plot([1, 2, 3], [4, 5, 6])

    plt.plot(phi2, theta2, color, lw=0.1)
    # plt.show()

def PlotBoundaryA0A1NearBWithInterpolate(LemonObjInstance,color,samplesize):
    R=LemonObjInstance.R
    phistar = LemonObjInstance.phistar
    Phistar = LemonObjInstance.Phistar
    b = R * np.cos(Phistar) - np.cos(phistar)
    # LBobj=LemmonBilliard(phistar,R)
    PhiL = -1.0*Phistar
    Phi1 = np.linspace(PhiL, Phistar, samplesize)
    theta1 = np.arcsin(np.sqrt(4/R))
    c1 = 2.0 * (-R * np.sin(theta1) + b * np.sin(Phi1 + theta1))
    c2 = R ** 2 - 2.0 * b * R * np.cos(Phi1) + b ** 2 - 1
    L1 = (np.sqrt(np.square(c1) - 4.0 * c2) - c1) / 2.0
    # print(L1)
    # print(len(L1))
    xQ = (L1 * np.cos(Phi1 + theta1) + R * np.sin(Phi1))
    # print(xQ)
    yQ = (L1 * np.sin(Phi1 + theta1) + b - R * np.cos(Phi1))
    # print(phistar)

    # plt.axvline(x=phistar,color='black',linewidth=0.05)
    # plt.axis('equal')
    # plt.gcf().set_size_inches(3.2, 2.1)
    # plt.ylim(phistar-1.5*(Phistar+theta1),phistar+1.5*(Phistar+theta1))
    # plt.xlim(phistar - 0.1 * (Phistar+theta1), phistar + 2.2 * (Phistar+theta1))
    # # plt.xlim(phistar - 0.5 * Phistar, phistar + 5 * np.sqrt(4/LemonObjInstance.R))
    # plt.xlabel(r" $\phi$-axis",fontsize=3)
    # #plt.ylabel(r'$\theta$-axis',fontsize=3)
    # ax=plt.gca()
    # ax.set_ylabel(r" $\theta$-axis",fontsize=3,labelpad =0.5)
    # ax.set_xlabel(r" $\phi$-axis",fontsize=3,labelpad =-0.5)
    # plt.plot([phistar, phistar + 3.6*(Phistar+theta1)], [phistar, phistar + 1.8*(Phistar+theta1)], linewidth=0.1,color="black")
    # plt.xticks([])
    # plt.yticks([])


    phi2 = np.arcsin(xQ)
    theta2 = phi2 - (Phi1 + theta1)
    print(phistar)
    print([phi2[0],phi2[-1]])
    print([theta2[0],theta2[-1]])
    print(len(theta2))
    ToInterpTheta2=np.linspace(theta2[0], theta2[-1], samplesize)
    InterpThetaPolynomial=np.polynomial.polynomial.Polynomial.fit(theta2,phi2,20,domain=[theta2[0],theta2[-1]])
    plt.plot(InterpThetaPolynomial(ToInterpTheta2),ToInterpTheta2, color, lw=0.1)
    #plt.plot(phi2, theta2, color, lw=0.1)

def PlotBoundaryA1BNearBWithInterpolate(LemonObjInstance,color,samplesize):
    R=LemonObjInstance.R
    phistar = LemonObjInstance.phistar
    Phistar = LemonObjInstance.Phistar
    b = R * np.cos(Phistar) - np.cos(phistar)
    # LBobj=LemmonBilliard(phistar,R)
    PhiL = -1.0*Phistar
    Phi1 = np.linspace(PhiL, Phistar, samplesize)
    theta1 = np.arcsin(2/R)
    c1 = 2.0 * (-R * np.sin(theta1) + b * np.sin(Phi1 + theta1))
    c2 = R ** 2 - 2.0 * b * R * np.cos(Phi1) + b ** 2 - 1
    L1 = (np.sqrt(np.square(c1) - 4.0 * c2) - c1) / 2.0
    # print(L1)
    # print(len(L1))
    xQ = (L1 * np.cos(Phi1 + theta1) + R * np.sin(Phi1))
    # print(xQ)
    yQ = (L1 * np.sin(Phi1 + theta1) + b - R * np.cos(Phi1))

    phi2 = np.arcsin(xQ)
    theta2 = phi2 - (Phi1 + theta1)
    print([phi2[0],phi2[-1]])
    print([theta2[0],theta2[-1]])
    print(phistar)
    ToInterpTheta2=np.linspace(theta2[0], theta2[-1], samplesize)
    InterpThetaPolynomial=np.polynomial.polynomial.Polynomial.fit(theta2,phi2,20,domain=[theta2[0],theta2[-1]])
    plt.plot(InterpThetaPolynomial(ToInterpTheta2),ToInterpTheta2, color, lw=0.1)






def PlotA0A1BAndCBoundariesNearBWithInterpolate(LemonObjInstance,samplesize):
    theta1=np.arcsin(np.sqrt(4/LemonObjInstance.R))
    plt.axvline(x=phistar,color='black',linewidth=0.05)
    plt.axis('equal')
    plt.gcf().set_size_inches(3.2, 2.1)
    plt.ylim(phistar-1.5*(Phistar+theta1),phistar+1.5*(Phistar+theta1))
    plt.xlim(phistar - 0.1 * (Phistar+theta1), phistar + 2.2 * (Phistar+theta1))
    # plt.xlim(phistar - 0.5 * Phistar, phistar + 5 * np.sqrt(4/LemonObjInstance.R))
    # plt.xlabel(r" $\phi$-axis",fontsize=3)
    #plt.ylabel(r'$\theta$-axis',fontsize=3)
    ax=plt.gca()
    ax.set_ylabel(r" $\theta$-axis",fontsize=3,labelpad =0.5)
    ax.set_xlabel(r" $\phi$-axis",fontsize=3,labelpad =-0.5)
    plt.plot([phistar, phistar + 8*(Phistar+theta1)], [phistar, phistar + 4.0*(Phistar+theta1)], linewidth=0.1,color="black")


    # ax.set_ylabel(r" $\theta$-axis", fontsize=3, labelpad=0.5)
    # ax.xaxis.label.set_color('red')
    # ax.set_xlabel(r" $x_2\in M^{in}_r$ in (a0),(a1),(b),(c) cases.", color="blue", fontsize=2.3, labelpad=-0.2)
    plt.text((phistar - 0.13 * theta1), phistar + 0.25 * theta1, r"$(\zeta,\zeta)$", fontsize=3,
             color="black", weight="bold")

    plt.text((phistar - 0.1 * theta1), phistar - (math.asin(math.sqrt(4 / LemonObjInstance.R)) + 0.9*Phistar),
             r"$(\zeta,\zeta-\sin^{-1}(\sqrt{\frac{4r}{R}})-\varsigma)$", fontsize=3,
             color="black", weight="bold")
    plt.text((phistar + 0.35 * theta1), phistar - 0.1 * theta1, r"(a1)", fontsize=5,
             color="black", weight="bold")
    plt.text((phistar + 1.7 * theta1), phistar - .1 * theta1, r"(a0)", fontsize=6,
             color="black", weight="bold")
    plt.text((phistar + 0.03 * theta1), phistar - .02 * theta1, r"(b)", fontsize=2,
             color="black", weight="bold")
    plt.xticks([])
    plt.yticks([])





    plt.xticks([])
    plt.yticks([])
    # PlotSingularcurveFromAWithInterpolate(1, LemonObjInstance, "green", samplesize)
    PlotBoundaryA0A1NearBWithInterpolate(LemonObjInstance,"blue",samplesize)
    PlotBoundaryA1BNearBWithInterpolate(LemonObjInstance,"red",samplesize)

    [singphi, singtheta] = PlotSingularcurveFromAWithInterpolate(1, LemonObjInstance, "orange", samplesize)
    axins = ax.inset_axes([-0.3, 0.5, 0.2, 0.3], xticklabels=[], yticklabels=[],
                          xlim=[phistar - 1.3 * Phistar, phistar + 0.7 * Phistar ],
                          ylim=[phistar - 2.1 * Phistar, phistar + 0.2 * Phistar])
    # axins.imshow([singphi, singtheta], extent=(-3, 4, -4, 3), origin="lower")

    axins.plot(singphi, singtheta, color="orange", linewidth=0.2)
    axins.plot([ phistar, phistar], [0, np.pi], color="black", linewidth=0.02)
    axins.plot([phistar, phistar + 2.6 * Phistar], [phistar, phistar + 1.3 * Phistar],
               color="black", linewidth=0.02)
    ax.indicate_inset_zoom(axins, linewidth=0.2, linestyle='--', edgecolor="black")
    axins.text(phistar - 0.29 * Phistar, phistar - Phistar, "(c)", fontsize=4)
    axins.text(phistar +0.1 * Phistar, phistar - 0.3 * Phistar, "(b)", fontsize=2)

def PlotBoundaryA0A1NearAWithInterpolate(LemonObjInstance,color,samplesize):
    R=LemonObjInstance.R
    phistar = LemonObjInstance.phistar
    Phistar = LemonObjInstance.Phistar
    b = R * np.cos(Phistar) - np.cos(phistar)
    # LBobj=LemmonBilliard(phistar,R)
    PhiL = -1.0*Phistar
    Phi1 = np.linspace(PhiL, Phistar, samplesize)
    theta1 = np.arcsin(np.sqrt(4/R))
    c1 = 2.0 * (-R * np.sin(theta1) + b * np.sin(Phi1 + theta1))
    c2 = R ** 2 - 2.0 * b * R * np.cos(Phi1) + b ** 2 - 1
    L1 = (np.sqrt(np.square(c1) - 4.0 * c2) - c1) / 2.0
    # print(L1)
    # print(len(L1))
    xQ = (L1 * np.cos(Phi1 + theta1) + R * np.sin(Phi1))
    # print(xQ)
    yQ = (L1 * np.sin(Phi1 + theta1) + b - R * np.cos(Phi1))
    # print(phistar)

    # plt.axvline(x=phistar,color='black',linewidth=0.05)
    # plt.axis('equal')
    # plt.gcf().set_size_inches(3.2, 2.1)
    # plt.ylim(phistar-1.5*(Phistar+theta1),phistar+1.5*(Phistar+theta1))
    # plt.xlim(phistar - 0.1 * (Phistar+theta1), phistar + 2.2 * (Phistar+theta1))
    # # plt.xlim(phistar - 0.5 * Phistar, phistar + 5 * np.sqrt(4/LemonObjInstance.R))
    # plt.xlabel(r" $\phi$-axis",fontsize=3)
    # #plt.ylabel(r'$\theta$-axis',fontsize=3)
    # ax=plt.gca()
    # ax.set_ylabel(r" $\theta$-axis",fontsize=3,labelpad =0.5)
    # ax.set_xlabel(r" $\phi$-axis",fontsize=3,labelpad =-0.5)
    # plt.plot([phistar, phistar + 3.6*(Phistar+theta1)], [phistar, phistar + 1.8*(Phistar+theta1)], linewidth=0.1,color="black")
    # plt.xticks([])
    # plt.yticks([])


    phi2 = np.arcsin(xQ)
    theta2 = phi2 - (Phi1 + theta1)
    phi2 = 2 * np.pi - phi2
    print(phistar)
    print([phi2[0],phi2[-1]])
    print([theta2[0],theta2[-1]])
    print(len(theta2))
    ToInterpTheta2=np.linspace(theta2[0], theta2[-1], samplesize)
    InterpThetaPolynomial=np.polynomial.polynomial.Polynomial.fit(theta2,phi2,20,domain=[theta2[0],theta2[-1]])
    plt.plot(InterpThetaPolynomial(ToInterpTheta2),ToInterpTheta2, color, lw=0.1)

def PlotBoundaryA1BNearAWithInterpolate(LemonObjInstance,color,samplesize):
    R=LemonObjInstance.R
    phistar = LemonObjInstance.phistar
    Phistar = LemonObjInstance.Phistar
    b = R * np.cos(Phistar) - np.cos(phistar)
    # LBobj=LemmonBilliard(phistar,R)
    PhiL = -1.0*Phistar
    Phi1 = np.linspace(PhiL, Phistar, samplesize)
    theta1 = np.arcsin(2/R)
    c1 = 2.0 * (-R * np.sin(theta1) + b * np.sin(Phi1 + theta1))
    c2 = R ** 2 - 2.0 * b * R * np.cos(Phi1) + b ** 2 - 1
    L1 = (np.sqrt(np.square(c1) - 4.0 * c2) - c1) / 2.0
    # print(L1)
    # print(len(L1))
    xQ = (L1 * np.cos(Phi1 + theta1) + R * np.sin(Phi1))
    # print(xQ)
    yQ = (L1 * np.sin(Phi1 + theta1) + b - R * np.cos(Phi1))

    phi2 =np.arcsin(xQ)
    theta2 = phi2 - (Phi1 + theta1)
    phi2=2*np.pi-phi2
    print([phi2[0],phi2[-1]])
    print([theta2[0],theta2[-1]])
    print(phistar)
    print(2*np.pi-phistar)
    ToInterpTheta2=np.linspace(theta2[0], theta2[-1], samplesize)
    InterpThetaPolynomial=np.polynomial.polynomial.Polynomial.fit(theta2,phi2,20,domain=[theta2[0],theta2[-1]])
    plt.plot(InterpThetaPolynomial(ToInterpTheta2),ToInterpTheta2, color, lw=0.1)

def PlotA0A1BAndCBoundariesNearAWithInterpolate(LemonObjInstance,samplesize):
    theta1=np.arcsin(np.sqrt(4/LemonObjInstance.R))
    plt.axvline(x=2*np.pi-phistar,color='black',linewidth=0.05)
    plt.axis('equal')
    plt.gcf().set_size_inches(3.2, 2.1)
    plt.ylim(phistar-1.0*(Phistar+theta1),phistar+1.0*(Phistar+theta1))
    plt.xlim(2*np.pi-(phistar + 2.2 * (Phistar+theta1)),2*np.pi-(phistar - 0.1 * (Phistar+theta1)))
    # plt.xlim(phistar - 0.5 * Phistar, phistar + 5 * np.sqrt(4/LemonObjInstance.R))
    # plt.xlabel(r" $\phi$-axis",fontsize=3)
    #plt.ylabel(r'$\theta$-axis',fontsize=3)
    ax=plt.gca()
    ax.set_ylabel(r" $\theta$-axis",fontsize=5,labelpad =0.5)
    ax.set_xlabel(r" $\phi$-axis", fontsize=5, labelpad=-0.2)
    # ax.xaxis.label.set_color('red')
    # ax.set_xlabel(r" $x_0\in M^{out}_r$ in (a0),(a1),(b),(c) cases.",color="red",fontsize=2.3,labelpad =-0.2)
    plt.text(2 * np.pi - (phistar + 0.18*theta1), phistar+0.28*theta1, r"$(2\pi-\zeta,\zeta)$", fontsize=3, color="black", weight="bold")

    plt.text(2 * np.pi - (phistar - 0.05 * theta1), phistar - (math.asin(math.sqrt(4/LemonObjInstance.R))-Phistar), r"$(2\pi-\zeta,\zeta-\sin^{-1}(\sqrt{\frac{4r}{R}})-\varsigma)$", fontsize=2,
             color="black", weight="bold")
    plt.plot([2*np.pi-phistar, 2*np.pi-phistar - 4.6*(Phistar+theta1)],[phistar, phistar + 2.3*(Phistar+theta1)], linewidth=0.1,color="black")
    plt.text(2 * np.pi - (phistar + 0.9 * theta1), phistar - 0.15 * theta1, r"(a1)", fontsize=6,
             color="black", weight="bold")
    plt.text(2 * np.pi - (phistar + 2 * theta1), phistar -.15 * theta1, r"(a0)", fontsize=6,
             color="black", weight="bold")
    plt.text(2 * np.pi - (phistar + 0.1 * theta1), phistar - .1 * theta1, r"(b)", fontsize=1.7,
             color="black", weight="bold")
    plt.xticks([])
    plt.yticks([])
    # PlotSingularcurveFromAWithInterpolate(1, LemonObjInstance, "green", samplesize)
    PlotBoundaryA0A1NearAWithInterpolate(LemonObjInstance,"blue",samplesize)
    PlotBoundaryA1BNearAWithInterpolate(LemonObjInstance,"red",samplesize)
    [singphi,singtheta]=PlotSingularcurveToBWithInterpolate(1,LemonObjInstance,"green",samplesize)
    axins = ax.inset_axes([1.05, 0.5, 0.2, 0.3],xticklabels=[], yticklabels=[],xlim=[2*np.pi-phistar-0.7*Phistar,2*np.pi-phistar+1.3*Phistar],ylim=[phistar-2.1*Phistar,phistar+0.2*Phistar])
    # axins.imshow([singphi, singtheta], extent=(-3, 4, -4, 3), origin="lower")

    axins.plot(singphi, singtheta,color="green",linewidth=0.05)
    axins.plot([2*np.pi-phistar,2*np.pi-phistar],[0,np.pi],color="black",linewidth=0.02)
    axins.plot([2 * np.pi - phistar, 2 * np.pi - phistar-1.5*Phistar], [phistar, phistar+0.75*Phistar], color="black", linewidth=0.02)
    ax.indicate_inset_zoom(axins, linewidth=0.2,linestyle='--',edgecolor="black")
    axins.text(2*np.pi-phistar-0.15*Phistar,phistar-Phistar,"(c)",fontsize=2)
    axins.text(2 * np.pi - phistar -0.62 * Phistar, phistar -0.35*Phistar, "(b)", fontsize=1.5)
    # axins.set_xticklabels('')
    # axins.set_yticklabels('')


def PlotSingularcurveFromAWithInterpolate(n,LemonObjInstance,color,samplesize):
    R=LemonObjInstance.R
    phistar = LemonObjInstance.phistar
    Phistar = LemonObjInstance.Phistar
    b = R * np.cos(Phistar) - np.cos(phistar)
    # LBobj=LemmonBilliard(phistar,R)
    PhiL = Phistar - 2 * Phistar / (n + 1.0)
    Phi1 = np.linspace(PhiL, Phistar, samplesize)
    theta1 = (Phi1 + Phistar) / (2.0 * n)
    c1 = 2.0 * (-R * np.sin(theta1) + b * np.sin(Phi1 + theta1))
    c2 = R ** 2 - 2.0 * b * R * np.cos(Phi1) + b ** 2 - 1
    L1 = (np.sqrt(np.square(c1) - 4.0 * c2) - c1) / 2.0
    # print(L1)
    # print(len(L1))
    xQ = (L1 * np.cos(Phi1 + theta1) + R * np.sin(Phi1))
    yQ = (L1 * np.sin(Phi1 + theta1) + b - R * np.cos(Phi1))
    # print(xQ)
    # print(xQ[-1]**2+yQ[-1]**2)
    # print(xQ[0])
    # print(xQ[-1])
    # print(np.square(yQ)+np.square(xQ))
    # print(math.sin(phistar))

    phi2 = np.arcsin(xQ)
    theta2 = phi2 - (Phi1 + theta1)
    # print(theta2[-1])
    slopes = 1 - np.sin(theta2) / (L1 - (2 * n) / (2 * n + 1) * R * np.sin(theta1))
    slopedenominator = (L1 - (2 * n) / (2 * n + 1) * R * np.sin(theta1))

    # print(30000/(math.sin(phistar)**2))
    # print ((theta2[0]-theta2[2])/(phi2[0]-phi2[2]))
    # print(slopes[0])
    #    print(slopedenominator[0])
    #   print(2 * (n + 1) / (2 * n + 1) * R * np.sin(Phistar / (n + 1)))
    # plt.plot(phi2, theta2, "b-", lw=0.5)
    # fig, ax = plt.subplots()
    # ax.plot([1, 2, 3], [4, 5, 6])
    ToInterpTheta2=np.linspace(phistar-(n+1)/n*Phistar, phistar-n/(n+1)*Phistar, samplesize)
    InterpThetaPolynomial=np.polynomial.polynomial.Polynomial.fit(theta2,phi2,20,domain=[phistar-(n+1)/n*Phistar,phistar-n/(n+1)*Phistar])
    # print(InterpThetaPolynomial(InterpTheta2))
    # print(len(InterpTheta2))
    InterpPhiPolynomial=InterpThetaPolynomial(ToInterpTheta2)
    plt.plot(InterpThetaPolynomial(ToInterpTheta2),ToInterpTheta2, color, lw=0.1)
    return [InterpPhiPolynomial, ToInterpTheta2]
    # plt.show()
def PlotSingularcurveFromBWithInterpolate(n,LemonObjInstance,color,samplesize):
    R=LemonObjInstance.R
    phistar = LemonObjInstance.phistar
    Phistar = LemonObjInstance.Phistar
    b = R * np.cos(Phistar) - np.cos(phistar)

    PhiL = Phistar - 2 * Phistar / (n + 1.0)
    Phi1 = np.linspace(PhiL, Phistar, samplesize)
    theta1 = (Phi1 + Phistar) / (2.0 * n)
    c1 = 2.0 * (-R * np.sin(theta1) + b * np.sin(Phi1 + theta1))
    c2 = R ** 2 - 2.0 * b * R * np.cos(Phi1) + b ** 2 - 1
    L1 = (np.sqrt(np.square(c1) - 4.0 * c2) - c1) / 2.0

    xQ = (L1 * np.cos(Phi1 + theta1) + R * np.sin(Phi1))
    yQ = (L1 * np.sin(Phi1 + theta1) + b - R * np.cos(Phi1))

    phi2 = np.arcsin(xQ)
    theta2 = phi2 - (Phi1 + theta1)
    phi2=2*np.pi-phi2
    theta2 =np.pi-theta2

    ToInterpTheta2=np.linspace(np.pi-(phistar-n/(n+1)*Phistar),np.pi-(phistar-(n+1)/n*Phistar), samplesize)
    InterpThetaPolynomial=np.polynomial.polynomial.Polynomial.fit(theta2,phi2,20,domain=[np.pi-(phistar-n/(n+1)*Phistar),np.pi-(phistar-(n+1)/n*Phistar)])
    plt.plot(InterpThetaPolynomial(ToInterpTheta2),ToInterpTheta2, color, lw=0.1)

def PlotShearPushedSingularcurveFromAWithInterpolate(n,LemonObjInstance,color,samplesize,steps):
    R = LemonObjInstance.R
    phistar = LemonObjInstance.phistar
    Phistar = LemonObjInstance.Phistar
    b = R * np.cos(Phistar) - np.cos(phistar)
    # LBobj=LemmonBilliard(phistar,R)
    PhiL = Phistar - 2 * Phistar / (n + 1.0)
    Phi1 = np.linspace(PhiL, Phistar, samplesize)
    theta1 = (Phi1 + Phistar) / (2.0 * n)
    c1 = 2.0 * (-R * np.sin(theta1) + b * np.sin(Phi1 + theta1))
    c2 = R ** 2 - 2.0 * b * R * np.cos(Phi1) + b ** 2 - 1
    L1 = (np.sqrt(np.square(c1) - 4.0 * c2) - c1) / 2.0
    # print(L1)
    # print(len(L1))
    xQ = (L1 * np.cos(Phi1 + theta1) + R * np.sin(Phi1))
    yQ = (L1 * np.sin(Phi1 + theta1) + b - R * np.cos(Phi1))
    # print(xQ)
    # print(xQ[-1]**2+yQ[-1]**2)
    # print(xQ[0])
    # print(xQ[-1])
    # print(np.square(yQ)+np.square(xQ))
    # print(math.sin(phistar))

    phi2 = np.arcsin(xQ)
    theta2 = phi2 - (Phi1 + theta1)
    shearmatrix=np.array([[1,2],[0,1]])
    [phi2,theta2]=(shearmatrix**steps)@np.array([phi2,theta2])
    #print([phi2,theta2])
    ToInterpTheta2 = np.linspace(phistar - (n + 1) / n * Phistar,phistar - n / (n + 1) * Phistar,
                                 samplesize)
    # print(ToInterpTheta2)
    # ToInterpTheta2=np.linspace(np.pi-(phistar-n/(n+1)*Phistar),np.pi-(phistar-(n+1)/n*Phistar), samplesize)
    InterpThetaPolynomial=np.polynomial.polynomial.Polynomial.fit(theta2,phi2,25,domain=[phistar - (n + 1) / n * Phistar,phistar - n / (n + 1) * Phistar])
    # print(InterpThetaPolynomial(ToInterpTheta2))
    # print(ToInterpTheta2)
    plt.plot(InterpThetaPolynomial(ToInterpTheta2),ToInterpTheta2, color, lw=0.1)


def PlotSingularcurveToBWithInterpolate(n,LemonObjInstance,color,samplesize):
    R=LemonObjInstance.R
    phistar = LemonObjInstance.phistar
    Phistar = LemonObjInstance.Phistar
    b = R * np.cos(Phistar) - np.cos(phistar)

    PhiL = Phistar - 2 * Phistar / (n + 1.0)
    Phi1 = np.linspace(PhiL, Phistar, samplesize)
    theta1 = (Phi1 + Phistar) / (2.0 * n)
    c1 = 2.0 * (-R * np.sin(theta1) + b * np.sin(Phi1 + theta1))
    c2 = R ** 2 - 2.0 * b * R * np.cos(Phi1) + b ** 2 - 1
    L1 = (np.sqrt(np.square(c1) - 4.0 * c2) - c1) / 2.0

    xQ = (L1 * np.cos(Phi1 + theta1) + R * np.sin(Phi1))
    yQ = (L1 * np.sin(Phi1 + theta1) + b - R * np.cos(Phi1))

    phi2 = np.arcsin(xQ)
    theta2 = phi2 - (Phi1 + theta1)
    phi2=2*np.pi-phi2
    # theta2 =np.pi-theta2
    # print(phi2)
    ToInterpTheta2=np.linspace(phistar-(n+1)/n*Phistar, phistar-n/(n+1)*Phistar, samplesize)
    InterpThetaPolynomial=np.polynomial.polynomial.Polynomial.fit(theta2,phi2,20,domain=[phistar-(n+1)/n*Phistar,phistar-n/(n+1)*Phistar])
    InterpPhiPolynomial=InterpThetaPolynomial(ToInterpTheta2)
    plt.plot(InterpPhiPolynomial,ToInterpTheta2, color, lw=0.1)
    return [InterpPhiPolynomial,ToInterpTheta2]

def SingularcurveToBWithInterpolatedCurve(n,LemonObjInstance,samplesize):
    R=LemonObjInstance.R
    phistar = LemonObjInstance.phistar
    Phistar = LemonObjInstance.Phistar
    b = R * np.cos(Phistar) - np.cos(phistar)

    PhiL = Phistar - 2 * Phistar / (n + 1.0)
    Phi1 = np.linspace(PhiL, Phistar, samplesize)
    theta1 = (Phi1 + Phistar) / (2.0 * n)
    c1 = 2.0 * (-R * np.sin(theta1) + b * np.sin(Phi1 + theta1))
    c2 = R ** 2 - 2.0 * b * R * np.cos(Phi1) + b ** 2 - 1
    L1 = (np.sqrt(np.square(c1) - 4.0 * c2) - c1) / 2.0

    xQ = (L1 * np.cos(Phi1 + theta1) + R * np.sin(Phi1))
    yQ = (L1 * np.sin(Phi1 + theta1) + b - R * np.cos(Phi1))

    phi2 = np.arcsin(xQ)
    theta2 = phi2 - (Phi1 + theta1)
    phi2=2*np.pi-phi2
    # theta2 =np.pi-theta2
    # print(phi2)
    ToInterpTheta2=np.linspace(phistar-(n+1)/n*Phistar, phistar-n/(n+1)*Phistar, samplesize)
    InterpThetaPolynomial=np.polynomial.polynomial.Polynomial.fit(theta2,phi2,20,domain=[phistar-(n+1)/n*Phistar,phistar-n/(n+1)*Phistar])
    return InterpThetaPolynomial

def SingularcurveFromAWithInterpolatedCurve(n,LemonObjInstance,samplesize):
    R = LemonObjInstance.R
    phistar = LemonObjInstance.phistar
    Phistar = LemonObjInstance.Phistar
    b = R * np.cos(Phistar) - np.cos(phistar)
    # LBobj=LemmonBilliard(phistar,R)
    PhiL = Phistar - 2 * Phistar / (n + 1.0)
    Phi1 = np.linspace(PhiL, Phistar, samplesize)
    theta1 = (Phi1 + Phistar) / (2.0 * n)
    c1 = 2.0 * (-R * np.sin(theta1) + b * np.sin(Phi1 + theta1))
    c2 = R ** 2 - 2.0 * b * R * np.cos(Phi1) + b ** 2 - 1
    L1 = (np.sqrt(np.square(c1) - 4.0 * c2) - c1) / 2.0
    # print(L1)
    # print(len(L1))
    xQ = (L1 * np.cos(Phi1 + theta1) + R * np.sin(Phi1))
    yQ = (L1 * np.sin(Phi1 + theta1) + b - R * np.cos(Phi1))
    # print(xQ)
    # print(xQ[-1]**2+yQ[-1]**2)
    # print(xQ[0])
    # print(xQ[-1])
    # print(np.square(yQ)+np.square(xQ))
    # print(math.sin(phistar))

    phi2 = np.arcsin(xQ)
    theta2 = phi2 - (Phi1 + theta1)
    # print(theta2[-1])
    slopes = 1 - np.sin(theta2) / (L1 - (2 * n) / (2 * n + 1) * R * np.sin(theta1))
    slopedenominator = (L1 - (2 * n) / (2 * n + 1) * R * np.sin(theta1))

    # print(30000/(math.sin(phistar)**2))
    # print ((theta2[0]-theta2[2])/(phi2[0]-phi2[2]))
    # print(slopes[0])
    #    print(slopedenominator[0])
    #   print(2 * (n + 1) / (2 * n + 1) * R * np.sin(Phistar / (n + 1)))
    # plt.plot(phi2, theta2, "b-", lw=0.5)
    # fig, ax = plt.subplots()
    # ax.plot([1, 2, 3], [4, 5, 6])
    # ToInterpTheta2 = np.linspace(phistar - (n + 1) / n * Phistar, phistar - n / (n + 1) * Phistar, samplesize)
    InterpThetaPolynomial = np.polynomial.polynomial.Polynomial.fit(theta2, phi2, 20,domain=[phistar - (n + 1) / n * Phistar,phistar - n / (n + 1) * Phistar])
    return InterpThetaPolynomial

def PlotPushedByShearsSingularityCurveFromCornerA(LemonObjInstance,samplesize,steps):
    PlotShearPushedSingularcurveFromAWithInterpolate(1,LemonObjInstance,"blue",samplesize,steps)
    PlotShearPushedSingularcurveFromAWithInterpolate(2, LemonObjInstance, "red", samplesize, steps)
    PlotShearPushedSingularcurveFromAWithInterpolate(3, LemonObjInstance, "green", samplesize, steps)
    PlotShearPushedSingularcurveFromAWithInterpolate(4, LemonObjInstance, "purple", samplesize, steps)
    #PlotBoundaryA0A1NearBWithInterpolate(LemonObjInstance, "yellow", samplesize)
    phistar=LemonObjInstance.phistar
    Phistar=LemonObjInstance.Phistar
    # plt.axvline(x=phistar,color='black',linewidth=0.05)
    plt.axis('equal')
    plt.gcf().set_size_inches(2.1, 3.3)
    plt.ylim(phistar-2.5*Phistar,phistar+0.05*Phistar)
    # plt.xlim(phistar+2*(steps+1)*phistar - 0.5 * Phistar, phistar + 2*(steps+1)*phistar+ 0.2 * Phistar)
    plt.xlim(phistar+2*(steps)*phistar- 3.5* Phistar, phistar+2*(steps)*phistar+ 0.1*Phistar)
    # plt.xlabel(r" $\phi$-axis",fontsize=3)
    #plt.ylabel(r'$\theta$-axis',fontsize=3)
    ax=plt.gca()
    ax.set_ylabel(r" $\theta$-axis",fontsize=3,labelpad =0.5)
    ax.set_xlabel(r" $\phi$-axis",fontsize=3,labelpad =-0.5)
    # plt.plot([phistar, phistar + 0.4*Phistar], [phistar, phistar + 0.2*Phistar], linewidth=0.1,color="black")
    # plt.plot([phistar+2*steps * phistar, phistar], [phistar +2*steps*phistar+2*(steps+1)*Phistar, phistar+Phistar], linewidth=0.1, color="black")
    plt.plot([phistar + 2 * steps * phistar, phistar + 2 * steps * phistar + 2 * (steps + 1) * Phistar],
             [phistar, phistar + Phistar], linewidth=0.1,
             color="black")
    # plt.plot([phistar,0], [phistar+2*steps * phistar,phistar], linewidth=0.1, color="black")
    plt.plot([phistar, phistar + 2 * steps * phistar], [0, phistar], linewidth=0.1, color="black")
    plt.xticks([])
    plt.yticks([])
    # plt.text(phistar + 0.03*Phistar, phistar-0.2*Phistar, r"$M^{in}_r$", fontsize=4, color="blue", weight="bold")
    # plt.text(phistar - 0.35*Phistar,phistar,r"$(\zeta,\zeta)$",fontsize=1.7,color="black",weight="bold")
    # plt.text(phistar - 0.9*Phistar, phistar-0.49*Phistar, r"$(\zeta,\zeta-(1/2)\varsigma)$", fontsize=1.7, color="blue",weight="bold")
    # plt.text(phistar - 0.9*Phistar, phistar - 1.9/3.0 * Phistar, r"$(\zeta,\zeta-(2/3)\varsigma)$", fontsize=1.7, color="red",weight="bold")
    # plt.text(phistar - 0.9*Phistar, phistar - 2.95 / 4.0 * Phistar, r"$(\zeta,\zeta-(3/4)\varsigma)$",
    #          fontsize=2, color="green",weight="bold")
    # plt.text(phistar - 0.9 * Phistar, phistar - 4.15/ 5.0 * Phistar, r"$(\zeta,\zeta-(4/5)\varsigma)$",
    #          fontsize=2, color="purple",weight="bold")
    # plt.text(phistar - 0.6 * Phistar, phistar - 5.0 / 5.0 * Phistar, r"$(\zeta,\zeta-\varsigma)$",
    #          fontsize=2, color="black",weight="bold")

    # plt.plot(phistar,phistar, marker=".",color="black",markersize=0.8)
    # plt.plot(phistar, phistar-1.0/2.0*Phistar, marker=".",markersize=0.5,color="blue")
    # plt.plot(phistar, phistar -2.0/3.0* Phistar, marker=".",markersize=0.2, color="red")
    # plt.plot(phistar, phistar - 3.0/4.0*Phistar, marker=".",markersize=0.1, color="green")
    # plt.plot(phistar, phistar - 4.0/5.0 * Phistar, marker=".",markersize=0.07, color="purple")

    # plt.plot(phistar, phistar-Phistar, marker=".", color="black",markersize=0.2)

    # plt.plot(phistar, phistar - 2.0/1.0 * Phistar, marker=".",markersize=0.5,color="blue")
    # plt.plot(phistar, phistar - 3.0/2.0 * Phistar, marker=".",markersize=0.2,color="red")
    # plt.plot(phistar, phistar - 4.0/3.0 * Phistar, marker=".",markersize=0.1,color="green")
    # plt.plot(phistar, phistar - 5.0/4.0 * Phistar, marker=".",markersize=0.07,color="purple")

    # plt.text(phistar - 0.9*Phistar,phistar-2.0*Phistar,r"$(\zeta,\zeta-2\varsigma)$",fontsize=1.7,color="blue",weight="bold")
    # plt.text(phistar - 0.9* Phistar, phistar-3.2/2.0*Phistar, r"$(\zeta,\zeta-(3/2)\varsigma)$", fontsize=1.7, color="red",weight="bold")
    # plt.text(phistar - 0.9* Phistar, phistar - 4.1/3.0 * Phistar, r"$(\zeta,\zeta-(4/3)\varsigma)$", fontsize=1.7, color="green",weight="bold")
    # plt.text(phistar - 0.9* Phistar, phistar - 4.95/ 4.0 * Phistar, r"$(\zeta,\zeta-(5/4)\varsigma)$",
    #          fontsize=2, color="purple",weight="bold")


def PlotSingularityCurveFromCornerA(LemonObjInstance,samplesize):
    PlotSingularcurveFromAWithInterpolate(1,LemonObjInstance,"blue",samplesize)
    PlotSingularcurveFromAWithInterpolate(2, LemonObjInstance, "red", samplesize)
    PlotSingularcurveFromAWithInterpolate(3, LemonObjInstance, "green", samplesize)
    PlotSingularcurveFromAWithInterpolate(4, LemonObjInstance, "purple", samplesize)
    #PlotBoundaryA0A1NearBWithInterpolate(LemonObjInstance, "yellow", samplesize)
    phistar=LemonObjInstance.phistar
    Phistar=LemonObjInstance.Phistar
    plt.axvline(x=phistar,color='black',linewidth=0.05)
    plt.axis('equal')
    plt.gcf().set_size_inches(2.1, 3.3)
    plt.ylim(phistar-2.05*Phistar,phistar+0.05*Phistar)
    plt.xlim(phistar - 0.5 * Phistar, phistar + 0.2 * Phistar)
    # plt.xlim(phistar - 0.5 * Phistar, phistar + 5 * np.sqrt(4/LemonObjInstance.R))
    plt.xlabel(r" $\phi$-axis",fontsize=3)
    #plt.ylabel(r'$\theta$-axis',fontsize=3)
    ax=plt.gca()
    ax.set_ylabel(r" $\theta$-axis",fontsize=3,labelpad =0.5)
    ax.set_xlabel(r" $\phi$-axis",fontsize=3,labelpad =-0.5)
    plt.plot([phistar, phistar + 0.4*Phistar], [phistar, phistar + 0.2*Phistar], linewidth=0.1,color="black")
    plt.xticks([])
    plt.yticks([])
    plt.text(phistar + 0.03*Phistar, phistar-0.2*Phistar, r"$M^{in}_r$", fontsize=4, color="blue", weight="bold")
    plt.text(phistar - 0.35*Phistar,phistar,r"$(\zeta,\zeta)$",fontsize=1.7,color="black",weight="bold")
    plt.text(phistar - 0.9*Phistar, phistar-0.49*Phistar, r"$(\zeta,\zeta-(1/2)\varsigma)$", fontsize=1.7, color="blue",weight="bold")
    plt.text(phistar - 0.9*Phistar, phistar - 1.9/3.0 * Phistar, r"$(\zeta,\zeta-(2/3)\varsigma)$", fontsize=1.7, color="red",weight="bold")
    plt.text(phistar - 0.9*Phistar, phistar - 2.95 / 4.0 * Phistar, r"$(\zeta,\zeta-(3/4)\varsigma)$",
             fontsize=2, color="green",weight="bold")
    plt.text(phistar - 0.9 * Phistar, phistar - 4.15/ 5.0 * Phistar, r"$(\zeta,\zeta-(4/5)\varsigma)$",
             fontsize=2, color="purple",weight="bold")
    plt.text(phistar - 0.6 * Phistar, phistar - 5.0 / 5.0 * Phistar, r"$(\zeta,\zeta-\varsigma)$",
             fontsize=2, color="black",weight="bold")

    plt.plot(phistar,phistar, marker=".",color="black",markersize=0.8)
    plt.plot(phistar, phistar-1.0/2.0*Phistar, marker=".",markersize=0.5,color="blue")
    plt.plot(phistar, phistar -2.0/3.0* Phistar, marker=".",markersize=0.2, color="red")
    plt.plot(phistar, phistar - 3.0/4.0*Phistar, marker=".",markersize=0.1, color="green")
    plt.plot(phistar, phistar - 4.0/5.0 * Phistar, marker=".",markersize=0.07, color="purple")

    plt.plot(phistar, phistar-Phistar, marker=".", color="black",markersize=0.2)

    plt.plot(phistar, phistar - 2.0/1.0 * Phistar, marker=".",markersize=0.5,color="blue")
    plt.plot(phistar, phistar - 3.0/2.0 * Phistar, marker=".",markersize=0.2,color="red")
    plt.plot(phistar, phistar - 4.0/3.0 * Phistar, marker=".",markersize=0.1,color="green")
    plt.plot(phistar, phistar - 5.0/4.0 * Phistar, marker=".",markersize=0.07,color="purple")

    plt.text(phistar - 0.9*Phistar,phistar-2.0*Phistar,r"$(\zeta,\zeta-2\varsigma)$",fontsize=1.7,color="blue",weight="bold")
    plt.text(phistar - 0.9* Phistar, phistar-3.2/2.0*Phistar, r"$(\zeta,\zeta-(3/2)\varsigma)$", fontsize=1.7, color="red",weight="bold")
    plt.text(phistar - 0.9* Phistar, phistar - 4.1/3.0 * Phistar, r"$(\zeta,\zeta-(4/3)\varsigma)$", fontsize=1.7, color="green",weight="bold")
    plt.text(phistar - 0.9* Phistar, phistar - 4.95/ 4.0 * Phistar, r"$(\zeta,\zeta-(5/4)\varsigma)$",
             fontsize=2, color="purple",weight="bold")
def PlotSingularityCurveFromCornerB(LemonObjInstance,samplesize):
    PlotSingularcurveFromBWithInterpolate(1,LemonObjInstance,"blue",samplesize)
    PlotSingularcurveFromBWithInterpolate(2, LemonObjInstance, "red", samplesize)
    PlotSingularcurveFromBWithInterpolate(3, LemonObjInstance, "green", samplesize)
    PlotSingularcurveFromBWithInterpolate(4, LemonObjInstance, "purple", samplesize)
    phistar=LemonObjInstance.phistar
    Phistar=LemonObjInstance.Phistar
    plt.axvline(x=2*np.pi-phistar,color='black',linewidth=0.05)
    plt.axis('equal')
    plt.gcf().set_size_inches(2.1, 3.3)
    plt.ylim(np.pi-(phistar+0.05*Phistar),np.pi-(phistar-2.05*Phistar))
    plt.xlim(2*np.pi-(phistar + 0.2 * Phistar),2*np.pi-(phistar - 0.5 * Phistar))
    # plt.xlabel(r" $\phi$-axis",fontsize=3)
    plt.ylabel(r'$\theta$-axis',fontsize=3)
    ax=plt.gca()
    ax.set_ylabel(r" $\theta$-axis",fontsize=3,labelpad =0.5)
    ax.set_xlabel(r" $\phi$-axis",fontsize=3,labelpad =-0.5)
    plt.plot([2*np.pi-phistar, 2*np.pi-(phistar + 1.8*Phistar)],[np.pi-phistar, np.pi-(phistar + 0.9*Phistar)] , linewidth=0.1,color="black")
    plt.xticks([])
    plt.yticks([])
    plt.text(2*np.pi-(phistar + 0.3*Phistar), np.pi-(phistar-0.1*Phistar), r"$M^{in}_r$", fontsize=4, color="blue", weight="bold")
    plt.text(2*np.pi-(phistar - 0.18*Phistar),np.pi-phistar,r"$(2\pi-\zeta,\pi-\zeta)$",fontsize=2.1,color="black",weight="bold")
    plt.text(2*np.pi-(phistar - 0.13*Phistar), np.pi-(phistar-0.49*Phistar), r"$(2\pi-\zeta,\pi-(\zeta-(1/2)\varsigma))$", fontsize=2.0, color="blue",weight="bold")
    plt.text(2*np.pi-(phistar - 0.13*Phistar), np.pi-(phistar - 1.9/3.0 * Phistar), r"$(2\pi-\zeta,\pi-(\zeta-(2/3)\varsigma))$", fontsize=2.0, color="red",weight="bold")
    plt.text(2*np.pi-(phistar - 0.13*Phistar), np.pi-(phistar - 2.95 / 4.0 * Phistar), r"$(2\pi-\zeta,\pi-(\zeta-(3/4)\varsigma))$",fontsize=2.0, color="green",weight="bold")
    plt.text(2*np.pi-(phistar - 0.13*Phistar), np.pi-(phistar - 4.15/ 5.0 * Phistar), r"$(2\pi-\zeta,\pi-(\zeta-(4/5)\varsigma))$",fontsize=2, color="purple",weight="bold")
    plt.text(2*np.pi-(phistar - 0.13*Phistar), np.pi-(phistar - 5.0 / 5.0 * Phistar), r"$(2\pi-\zeta,\pi-(\zeta-\varsigma))$",fontsize=2, color="black",weight="bold")

    plt.plot(2*np.pi-phistar,np.pi-phistar, marker=".",color="black",markersize=0.8)
    plt.plot(2*np.pi-phistar,np.pi-(phistar-1.0/2.0*Phistar), marker=".",markersize=0.5,color="blue")
    plt.plot(2*np.pi-phistar,np.pi-(phistar -2.0/3.0* Phistar), marker=".",markersize=0.2, color="red")
    plt.plot(2*np.pi-phistar,np.pi-(phistar - 3.0/4.0*Phistar), marker=".",markersize=0.1, color="green")
    plt.plot(2*np.pi-phistar,np.pi-(phistar - 4.0/5.0 * Phistar), marker=".",markersize=0.07, color="purple")

    plt.plot(2*np.pi-phistar,np.pi-(phistar-Phistar), marker=".", color="black",markersize=0.2)

    plt.plot(2*np.pi-phistar, np.pi-(phistar - 2.0/1.0 * Phistar), marker=".",markersize=0.5,color="blue")
    plt.plot(2*np.pi-phistar, np.pi-(phistar - 3.0/2.0 * Phistar), marker=".",markersize=0.2,color="red")
    plt.plot(2*np.pi-phistar, np.pi-(phistar - 4.0/3.0 * Phistar), marker=".",markersize=0.1,color="green")
    plt.plot(2*np.pi-phistar, np.pi-(phistar - 5.0/4.0 * Phistar), marker=".",markersize=0.07,color="purple")

    plt.text(2*np.pi-(phistar - 0.13*Phistar),np.pi-(phistar-2.0*Phistar),r"$(2\pi-\zeta,\pi-(\zeta-2\varsigma))$",fontsize=2.0,color="blue",weight="bold")
    plt.text(2*np.pi-(phistar - 0.13* Phistar), np.pi-(phistar-3.2/2.0*Phistar), r"$(2\pi-\zeta,\pi-(\zeta-(3/2)\varsigma))$", fontsize=2.0, color="red",weight="bold")
    plt.text(2*np.pi-(phistar - 0.13* Phistar), np.pi-(phistar - 4.1/3.0 * Phistar), r"$(2\pi-\zeta,\pi-(\zeta-(4/3)\varsigma))$", fontsize=2.0, color="green",weight="bold")
    plt.text(2*np.pi-(phistar - 0.13* Phistar), np.pi-(phistar - 4.95/ 4.0 * Phistar), r"$(2\pi-\zeta,\pi-(\zeta-(5/4)\varsigma))$",fontsize=2, color="purple",weight="bold")
def PlotSingularityCurveToCornerB(LemonObjInstance,samplesize):
    PlotSingularcurveToBWithInterpolate(1,LemonObjInstance,"blue",samplesize)
    PlotSingularcurveToBWithInterpolate(2, LemonObjInstance, "red", samplesize)
    PlotSingularcurveToBWithInterpolate(3, LemonObjInstance, "green", samplesize)
    PlotSingularcurveToBWithInterpolate(4, LemonObjInstance, "purple", samplesize)
    phistar=LemonObjInstance.phistar
    Phistar=LemonObjInstance.Phistar
    plt.axvline(x=2*np.pi-phistar,color='black',linewidth=0.05)
    plt.axis('equal')
    plt.gcf().set_size_inches(2.1, 3.3)
    plt.ylim(phistar-2.05*Phistar,phistar+0.05*Phistar)
    plt.xlim(2*np.pi-(phistar + 0.2 * Phistar),2*np.pi-(phistar - 0.5 * Phistar))
    # plt.xlabel(r" $\phi$-axis",fontsize=3)
    plt.ylabel(r'$\theta$-axis',fontsize=3)
    ax=plt.gca()
    ax.set_ylabel(r" $\theta$-axis",fontsize=3,labelpad =0.5)
    ax.set_xlabel(r" $\phi$-axis",fontsize=3,labelpad =-0.5)
    plt.plot([2*np.pi-phistar, 2*np.pi-(phistar + 1.8*Phistar)],[phistar, phistar + 0.9*Phistar] , linewidth=0.1,color="black")
    plt.xticks([])
    plt.yticks([])
    plt.text(2*np.pi-(phistar + 0.3*Phistar), (phistar-0.25*Phistar), r"$M^{out}_r$", fontsize=3, color="red", weight="bold")
    plt.text(2*np.pi-(phistar - 0.18*Phistar),phistar,r"$(2\pi-\zeta,\zeta)$",fontsize=2.1,color="black",weight="bold")
    plt.text(2*np.pi-(phistar - 0.13*Phistar), (phistar-0.49*Phistar), r"$(2\pi-\zeta,\zeta-(1/2)\varsigma)$", fontsize=2.0, color="blue",weight="bold")
    plt.text(2*np.pi-(phistar - 0.13*Phistar), (phistar - 1.9/3.0 * Phistar), r"$(2\pi-\zeta,\zeta-(2/3)\varsigma)$", fontsize=2.0, color="red",weight="bold")
    plt.text(2*np.pi-(phistar - 0.13*Phistar), (phistar - 2.95 / 4.0 * Phistar), r"$(2\pi-\zeta,\zeta-(3/4)\varsigma)$",fontsize=2.0, color="green",weight="bold")
    plt.text(2*np.pi-(phistar - 0.13*Phistar), (phistar - 4.15/ 5.0 * Phistar), r"$(2\pi-\zeta,\zeta-(4/5)\varsigma)$",fontsize=2, color="purple",weight="bold")
    plt.text(2*np.pi-(phistar - 0.13*Phistar), (phistar - 5.0 / 5.0 * Phistar), r"$(2\pi-\zeta,\zeta-\varsigma)$",fontsize=2, color="black",weight="bold")

    plt.plot(2*np.pi-phistar,phistar, marker=".",color="black",markersize=0.8)
    plt.plot(2*np.pi-phistar,(phistar-1.0/2.0*Phistar), marker=".",markersize=0.5,color="blue")
    plt.plot(2*np.pi-phistar,(phistar -2.0/3.0* Phistar), marker=".",markersize=0.2, color="red")
    plt.plot(2*np.pi-phistar,(phistar - 3.0/4.0*Phistar), marker=".",markersize=0.1, color="green")
    plt.plot(2*np.pi-phistar,(phistar - 4.0/5.0 * Phistar), marker=".",markersize=0.07, color="purple")

    plt.plot(2*np.pi-phistar,(phistar-Phistar), marker=".", color="black",markersize=0.2)

    plt.plot(2*np.pi-phistar, (phistar - 2.0/1.0 * Phistar), marker=".",markersize=0.5,color="blue")
    plt.plot(2*np.pi-phistar, (phistar - 3.0/2.0 * Phistar), marker=".",markersize=0.2,color="red")
    plt.plot(2*np.pi-phistar, (phistar - 4.0/3.0 * Phistar), marker=".",markersize=0.1,color="green")
    plt.plot(2*np.pi-phistar, (phistar - 5.0/4.0 * Phistar), marker=".",markersize=0.07,color="purple")

    plt.text(2*np.pi-(phistar - 0.13*Phistar),(phistar-2.0*Phistar),r"$(2\pi-\zeta,\zeta-2\varsigma)$",fontsize=2.0,color="blue",weight="bold")
    plt.text(2*np.pi-(phistar - 0.13* Phistar),(phistar-3.2/2.0*Phistar), r"$(2\pi-\zeta,\zeta-(3/2)\varsigma)$", fontsize=2.0, color="red",weight="bold")
    plt.text(2*np.pi-(phistar - 0.13* Phistar),(phistar - 4.1/3.0 * Phistar), r"$(2\pi-\zeta,\zeta-(4/3)\varsigma)$", fontsize=2.0, color="green",weight="bold")
    plt.text(2*np.pi-(phistar - 0.13* Phistar),(phistar - 4.95/ 4.0 * Phistar), r"$(2\pi-\zeta,\zeta-(5/4)\varsigma)$",fontsize=2, color="purple",weight="bold")


def FillPlotCellMinusLowerComponent(LemonObjInstance,samplesize,n):
    phistar=LemonObjInstance.phistar
    Phistar=LemonObjInstance.Phistar
    InterpThetaPolynomialLeft=SingularcurveToBWithInterpolatedCurve(n,LemonObjInstance,samplesize)
    # ToInterpTheta2Left = np.linspace(phistar - (n + 1) / n * Phistar, phistar - n / (n + 1) * Phistar, samplesize)
    InterpThetaPolynomialRight=SingularcurveToBWithInterpolatedCurve(n+1,LemonObjInstance,samplesize)


    ToInterpTheta2RightOnCurve = np.linspace(phistar - (n + 2) / (n+1) * Phistar, phistar - (n+1) / (n + 2) * Phistar, samplesize)

    # LeftPhi2=InterpThetaPolynomialLeft(ToInterpTheta2Left)
    RightPhi2OnCurve=InterpThetaPolynomialRight(ToInterpTheta2RightOnCurve)
    # print(RightPhi2OnCurve)
    ToInterpTheta2Left1=np.linspace(phistar-(n+1)/n*Phistar,phistar -(n+2)/(n+1)*Phistar,samplesize)
    ToInterpTheta2Left2=ToInterpTheta2RightOnCurve
    ToInterpTheta2Left3 =np.linspace(phistar-(n+1)/(n+2)*Phistar, phistar-n/(n + 1)*Phistar,samplesize)

    ToInterpTheta2Left=np.concatenate((ToInterpTheta2Left1,ToInterpTheta2Left2[1:],ToInterpTheta2Left3[1:]))
    LeftInterpolatedPhi2_1=InterpThetaPolynomialLeft(ToInterpTheta2Left1)
    LeftInterpolatedPhi2_2=InterpThetaPolynomialLeft(ToInterpTheta2Left2)
    LeftInterpolatedPhi2_3=InterpThetaPolynomialLeft(ToInterpTheta2Left3)
    RightInterpolatedPhi2=np.zeros((1,samplesize))
    RightInterpolatedPhi2.fill(2*np.pi-phistar)
    # print(RightInterpolatedPhi2)
    # print([len(LeftInterpolatedPhi2),len(LeftInterpolatedPhi2),len(RightInterpolatedPhi2)])
    plt.plot(LeftInterpolatedPhi2_1, ToInterpTheta2Left1,color='red',linewidth=0.2)
    plt.plot(RightInterpolatedPhi2[0], ToInterpTheta2Left1,color='black',linewidth=0.2)
    plt.plot(LeftInterpolatedPhi2_3, ToInterpTheta2Left3, color='red', linewidth=0.2)
    plt.plot(RightInterpolatedPhi2[0], ToInterpTheta2Left3, color='black', linewidth=0.2)
    plt.plot(LeftInterpolatedPhi2_2, ToInterpTheta2Left2, color='red', linewidth=0.2)
    plt.plot(RightPhi2OnCurve, ToInterpTheta2RightOnCurve , color='green', linewidth=0.2)

    # plt.fill_betweenx(ToInterpTheta2Left1, LeftInterpolatedPhi2_1, RightInterpolatedPhi2[0],lw=0.01,alpha=0.5 ,color='orange')
    # plt.fill_betweenx(ToInterpTheta2Left2, LeftInterpolatedPhi2_2, RightPhi2OnCurve,lw=0.01, alpha=0.5,
    #                   color='orange')
    # plt.fill_betweenx(ToInterpTheta2Left3, LeftInterpolatedPhi2_3, RightInterpolatedPhi2[0],lw=0.01,alpha=0.5 ,color='orange')
    
    # plt.fill_betweenx(,alpha=0.5,color='orange')

    ToInterpTheta2Left = np.concatenate((ToInterpTheta2Left1, ToInterpTheta2Left2[1:], ToInterpTheta2Left3[1:]))
    ToInterpPhi2Left= np.concatenate((LeftInterpolatedPhi2_1, LeftInterpolatedPhi2_2[1:], LeftInterpolatedPhi2_3[1:]))
    ToInterpPhi2Right=np.concatenate((RightInterpolatedPhi2[0],RightPhi2OnCurve[1:],RightInterpolatedPhi2[0][1:]))

    plt.fill_betweenx(ToInterpTheta2Left, ToInterpPhi2Left, ToInterpPhi2Right,lw=0.01,alpha=0.5 ,color='orange')

    ax=plt.gca()
    plt.gcf().set_size_inches(2.1, 3.3)
    ax.set_ylabel(r" $\theta$-axis",fontsize=3,labelpad =0.5)
    ax.set_xlabel(r" $\phi$-axis",fontsize=3,labelpad =-0.5)
    plt.ylim(phistar-2.2*Phistar,phistar+0.3*Phistar)
    plt.xlim(2*np.pi-(phistar+0.6*Phistar),2*np.pi-(phistar - 1.7 * Phistar))
    plt.xticks([])
    plt.yticks([])
    plt.axvline(x=2 * np.pi - phistar, color='black', linewidth=0.2)
    plt.axis('equal')
    PlotSingularcurveToBWithInterpolate(1, LemonObjInstance, "blue", samplesize)
    PlotSingularcurveToBWithInterpolate(2, LemonObjInstance, "red", samplesize)
    PlotSingularcurveToBWithInterpolate(3, LemonObjInstance, "green", samplesize)
    # PlotSingularcurveToBWithInterpolate(4, LemonObjInstance, "black", samplesize)

    plt.plot(2 * np.pi - phistar, (phistar - 1.0 / 2.0 * Phistar), marker=".", markersize=0.2, color="blue")
    plt.plot(2 * np.pi - phistar, (phistar - 2.0 / 3.0 * Phistar), marker=".", markersize=0.2, color="red")
    plt.plot(2 * np.pi - phistar, (phistar - 3.0 / 4.0 * Phistar), marker=".", markersize=0.2, color="green")

    # plt.plot(2*np.pi-phistar, (phistar - 2.0/1.0 * Phistar), marker=".",markersize=0.5,color="blue")
    plt.plot(2*np.pi-phistar, (phistar - 3.0/2.0 * Phistar), marker=".",markersize=0.2,color="red")
    plt.plot(2*np.pi-phistar, (phistar - 4.0/3.0 * Phistar), marker=".",markersize=0.2,color="green")
    # plt.plot(2*np.pi-phistar, (phistar - 5.0/4.0 * Phistar), marker=".",markersize=0.07,color="purple")

    # plt.text(2 * np.pi - (phistar + .4 * Phistar), (phistar - 1.0 / 1.95 * Phistar),
    #          r"$(2\pi-\zeta,\zeta-(1/2)\varsigma)$", fontsize=4.0, color="blue", weight="bold")
    plt.text(2 * np.pi - (phistar + 0.5 * Phistar), (phistar - 2.0/3.1 * Phistar),
             r"$(2\pi-\zeta,\zeta-(2/3)\varsigma)$", fontsize=4.0, color="red", weight="bold")
    plt.text(2 * np.pi - (phistar + 0.5 * Phistar), (phistar - 3.0/3.9 * Phistar),
    r"$(2\pi-\zeta,\zeta-(3/4)\varsigma)$", fontsize=4.0, color="green", weight="bold")

    # plt.text(2*np.pi-(phistar + .4*Phistar),(phistar-2.0*Phistar),r"$(2\pi-\zeta,\zeta-2\varsigma)$",fontsize=4.0,color="blue",weight="bold")
    plt.text(2*np.pi-(phistar + .5* Phistar),(phistar-3.05/2.0*Phistar), r"$(2\pi-\zeta,\zeta-(3/2)\varsigma)$", fontsize=4.0, color="red",weight="bold")
    plt.text(2*np.pi-(phistar + 0.5* Phistar),(phistar - 4.0/3.0 * Phistar), r"$(2\pi-\zeta,\zeta-(4/3)\varsigma)$", fontsize=4.0, color="green",weight="bold")
    # plt.text(2*np.pi-(phistar - 0.13* Phistar),(phistar - 4.95/ 4.0 * Phistar), r"$(2\pi-\zeta,\zeta-(5/4)\varsigma)$",fontsize=2, color="purple",weight="bold")

    plt.text(2*np.pi-(phistar + 0.3 * Phistar), (phistar - 5.0 / 5.0 * Phistar), r"$\mathcal{D}^{out}_{2}$",
             fontsize=6.0, color="black", weight="bold")
    return len(LeftInterpolatedPhi2_1)


def FillPlotCellPlusLowerComponent(LemonObjInstance, samplesize, n):
    phistar = LemonObjInstance.phistar
    Phistar = LemonObjInstance.Phistar
    InterpThetaPolynomialLeft = SingularcurveToBWithInterpolatedCurve(n, LemonObjInstance, samplesize)
    # ToInterpTheta2Left = np.linspace(phistar - (n + 1) / n * Phistar, phistar - n / (n + 1) * Phistar, samplesize)
    InterpThetaPolynomialRight = SingularcurveToBWithInterpolatedCurve(n + 1, LemonObjInstance, samplesize)

    ToInterpTheta2RightOnCurve = np.linspace(phistar - (n + 2) / (n + 1) * Phistar,
                                             phistar - (n + 1) / (n + 2) * Phistar, samplesize)

    # LeftPhi2=InterpThetaPolynomialLeft(ToInterpTheta2Left)
    RightPhi2OnCurve = InterpThetaPolynomialRight(ToInterpTheta2RightOnCurve)
    # print(RightPhi2OnCurve)
    ToInterpTheta2Left1 = np.linspace(phistar - (n + 1) / n * Phistar, phistar - (n + 2) / (n + 1) * Phistar,
                                      samplesize)
    ToInterpTheta2Left2 = ToInterpTheta2RightOnCurve
    ToInterpTheta2Left3 = np.linspace(phistar - (n + 1) / (n + 2) * Phistar, phistar - n / (n + 1) * Phistar,
                                      samplesize)

    ToInterpTheta2Left = np.concatenate((ToInterpTheta2Left1, ToInterpTheta2Left2[1:], ToInterpTheta2Left3[1:]))
    LeftInterpolatedPhi2_1 = InterpThetaPolynomialLeft(ToInterpTheta2Left1)
    LeftInterpolatedPhi2_2 = InterpThetaPolynomialLeft(ToInterpTheta2Left2)
    LeftInterpolatedPhi2_3 = InterpThetaPolynomialLeft(ToInterpTheta2Left3)
    RightInterpolatedPhi2 = np.zeros((1, samplesize))
    RightInterpolatedPhi2.fill(2 * np.pi - phistar)
    # print(RightInterpolatedPhi2)
    # print([len(LeftInterpolatedPhi2),len(LeftInterpolatedPhi2),len(RightInterpolatedPhi2)])
    plt.axvline(x=phistar, color='black', linewidth=0.2)
    plt.plot(2*np.pi-LeftInterpolatedPhi2_1, ToInterpTheta2Left1, color='black', linewidth=0.2)
    plt.plot(2*np.pi-RightInterpolatedPhi2[0], ToInterpTheta2Left1, color='red', linewidth=0.2)
    plt.plot(2*np.pi-LeftInterpolatedPhi2_3, ToInterpTheta2Left3, color='black', linewidth=0.2)
    plt.plot(2*np.pi-RightInterpolatedPhi2[0], ToInterpTheta2Left3, color='green', linewidth=0.2)
    plt.plot(2*np.pi-LeftInterpolatedPhi2_2, ToInterpTheta2Left2, color='black', linewidth=0.2)
    plt.plot(2*np.pi-RightPhi2OnCurve, ToInterpTheta2RightOnCurve, color='black', linewidth=0.2)

    # plt.fill_betweenx(ToInterpTheta2Left1, LeftInterpolatedPhi2_1, RightInterpolatedPhi2[0],lw=0.01,alpha=0.5 ,color='orange')
    # plt.fill_betweenx(ToInterpTheta2Left2, LeftInterpolatedPhi2_2, RightPhi2OnCurve,lw=0.01, alpha=0.5,
    #                   color='orange')
    # plt.fill_betweenx(ToInterpTheta2Left3, LeftInterpolatedPhi2_3, RightInterpolatedPhi2[0],lw=0.01,alpha=0.5 ,color='orange')

    # plt.fill_betweenx(,alpha=0.5,color='orange')

    ToInterpTheta2Left = np.concatenate((ToInterpTheta2Left1, ToInterpTheta2Left2[1:], ToInterpTheta2Left3[1:]))
    ToInterpPhi2Left = np.concatenate((2*np.pi-LeftInterpolatedPhi2_1, 2*np.pi-LeftInterpolatedPhi2_2[1:], 2*np.pi-LeftInterpolatedPhi2_3[1:]))
    ToInterpPhi2Right = np.concatenate((2*np.pi-RightInterpolatedPhi2[0], 2*np.pi-RightPhi2OnCurve[1:], 2*np.pi-RightInterpolatedPhi2[0][1:]))

    plt.fill_betweenx(ToInterpTheta2Left, ToInterpPhi2Left, ToInterpPhi2Right, lw=0.01, alpha=0.5, color='orange')

    ax = plt.gca()
    plt.gcf().set_size_inches(6.3, 8.6)
    ax.set_ylabel(r" $\theta$-axis", fontsize=3, labelpad=0.5)
    ax.set_xlabel(r" $\phi$-axis", fontsize=3, labelpad=-0.5)
    plt.ylim(phistar - 2.6 * Phistar, phistar + 0.4 * Phistar)
    plt.xlim((phistar - 0.01 * Phistar),(phistar + 0.4 * Phistar))
    plt.xticks([])
    plt.yticks([])

    plt.axis('equal')
    PlotSingularcurveFromAWithInterpolate(1, LemonObjInstance, "black", samplesize)
    # PlotSingularcurveFromAWithInterpolate(1, LemonObjInstance, "blue", samplesize)
    # PlotSingularcurveFromAWithInterpolate(2, LemonObjInstance, "red", samplesize)
    # PlotSingularcurveFromAWithInterpolate(3, LemonObjInstance, "black", samplesize)
    # PlotSingularcurveFromAWithInterpolate(4, LemonObjInstance, "black", samplesize)


    # plt.plot([2*np.pi-phistar, 2*np.pi-(phistar + 1.8*Phistar)],[phistar, phistar + 0.9*Phistar] , linewidth=0.1,color="black")

    # plt.text(2*np.pi-(phistar + 0.3*Phistar), (phistar-0.25*Phistar), r"$M^{out}_r$", fontsize=3, color="red", weight="bold")
    # plt.text(2*np.pi-(phistar - 0.18*Phistar),phistar,r"$(2\pi-\zeta,\zeta)$",fontsize=2.1,color="black",weight="bold")
    plt.text((phistar + 0.13 * Phistar), (phistar - 3.0/3.9 * Phistar), r"$(\zeta,\zeta-(3/4)\varsigma)$",
              fontsize=4.0, color="green", weight="bold")
    plt.text((phistar +0.13 * Phistar), (phistar - 2.0 / 3.1 * Phistar),
             r"$(\zeta,\zeta-(2/3)\varsigma)$", fontsize=4, color="green", weight="bold")
    # plt.text((phistar +0.13 * Phistar), (phistar - 1.0 / 2.0 * Phistar),
             # r"$(\zeta,\zeta-(1/2)\varsigma)$", fontsize=4, color="red", weight="bold")

    # plt.text(2*np.pi-(phistar - 0.13*Phistar), (phistar - 2.95 / 4.0 * Phistar), r"$(2\pi-\zeta,\zeta-(3/4)\varsigma)$",fontsize=2.0, color="green",weight="bold")
    # plt.text(2*np.pi-(phistar - 0.13*Phistar), (phistar - 4.15/ 5.0 * Phistar), r"$(2\pi-\zeta,\zeta-(4/5)\varsigma)$",fontsize=2, color="purple",weight="bold")
    # plt.text((phistar - 0.5 * Phistar), (phistar - 5.0 / 5.0 * Phistar), r"$(2\pi-\zeta,\zeta-\varsigma)$",fontsize=2, color="black", weight="bold")

    plt.text((phistar + 0.21 * Phistar), (phistar - 5.0 / 5.0 * Phistar), r"$\mathcal{D}^{in}_{-2}$",
             fontsize=6.5, color="black", weight="bold")

    # plt.plot(2*np.pi-phistar,phistar, marker=".",color="black",markersize=0.8)
    plt.plot(phistar, (phistar - 1.0 / 2.0 * Phistar), marker=".", markersize=0.5, color="black")
    plt.plot(phistar, (phistar - 2.0 / 3.0 * Phistar), marker=".", markersize=0.5, color="green")
    plt.plot(phistar, (phistar - 3.0 / 4.0 * Phistar), marker=".", markersize=0.2, color="green")
    # plt.plot(2*np.pi-phistar,(phistar - 3.0/4.0*Phistar), marker=".",markersize=0.1, color="green")
    # plt.plot(2*np.pi-phistar,(phistar - 4.0/5.0 * Phistar), marker=".",markersize=0.07, color="purple")

    plt.plot(phistar, (phistar - Phistar), marker=".", color="black", markersize=0.2)


    plt.plot(phistar, (phistar - 4.0 / 3.0 * Phistar), marker=".", markersize=0.2, color="red")
    plt.plot(phistar, (phistar - 3.0 / 2.0 * Phistar), marker=".", markersize=0.5, color="red")
    plt.plot(phistar, (phistar - 2.0 / 1.0 * Phistar), marker=".", markersize=0.5, color="black")
    # plt.plot(2*np.pi-phistar, (phistar - 4.0/3.0 * Phistar), marker=".",markersize=0.1,color="green")
    # plt.plot(2*np.pi-phistar, (phistar - 5.0/4.0 * Phistar), marker=".",markersize=0.07,color="purple")

    plt.text((phistar + 0.13 * Phistar), (phistar - 4.0/3.0 * Phistar), r"$(\zeta,\zeta-(4/3)\varsigma)$",
              fontsize=4.0, color="red", weight="bold")
    plt.text((phistar + 0.13 * Phistar), (phistar - 3 / 2.0 * Phistar),
             r"$(\zeta,\zeta-(3/2)\varsigma)$", fontsize=4.0, color="red", weight="bold")
    # plt.text((phistar + 0.13 * Phistar), (phistar - 2.0 / 1.0 * Phistar), r"$(\zeta,\zeta-2\varsigma)$",
    #          fontsize=4, color="blue", weight="bold")
    # plt.text(2*np.pi-(phistar - 0.13* Phistar),(phistar - 4.1/3.0 * Phistar), r"$(2\pi-\zeta,\zeta-(4/3)\varsigma)$", fontsize=2.0, color="green",weight="bold")
    # plt.text(2*np.pi-(phistar - 0.13* Phistar),(phistar - 4.95/ 4.0 * Phistar), r"$(2\pi-\zeta,\zeta-(5/4)\varsigma)$",fontsize=2, color="purple",weight="bold")

    return len(LeftInterpolatedPhi2_1)



if __name__ == '__main__':
    R=48.5
    n=1
    phistar=np.pi/10.5
    Phistar=np.arcsin(math.sin(phistar)/R)
    b=R*np.cos(Phistar)-np.cos(phistar)
    LBobj=LemmonObj(R,phistar)
    #PlotBoundaryA0A1NearAWithInterpolate(LBobj, "blue", 500)
    # PlotA0A1BAndCBoundariesNearAWithInterpolate(LBobj, 500)
    # PlotA0A1BAndCBoundariesNearBWithInterpolate(LBobj,500)
    # PlotA0A1BAndCBoundariesNearAWithInterpolate(LBobj, 500)
    # PlotA0A1BAndCBoundariesNearBWithInterpolate(LBobj,500)
    # PlotSingularityCurveFromCornerB(LBobj,500)
    # PlotSingularityCurveToCornerB(LBobj, 500)
    # PlotSingularityCurveFromCornerA(LBobj,500)
    PlotPushedByShearsSingularityCurveFromCornerA(LBobj,500,2)
    #PlotSingularityCurveToCornerA(LBobj, 500)

    # PlotA0A1BAndCBoundariesNearBWithInterpolate(LBobj,500)
    # SingularcurveToBWithInterpolatedCurve(2,LBobj,1000)
    #print(FillPlotCellPlusLowerComponent(LBobj, 500, 2))
    # print(FillPlotCellPlusLowerComponent(LBobj, 500, 1))
    # print(FillPlotCellMinusLowerComponent(LBobj, 500, 2))
    plt.tight_layout()
    plt.margins(x=0,y=0)
    # plt.savefig("C:/Users/Thinkpad/Box/WentaoFanBoxNotes/ErgodicTheory/Billiards/LemonBilliard/figures/LemonBilliardsFigures/fig1.pdf",format='pdf')
    plt.show()