# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def harmonic(n,k):
    ans=0.0
    for i in range(1,n+1):
        ans+=1.0/(i**k)
    return ans
def fun(n,first):
    ans=[]
    val = first
    for i in range(1, n+1):
        ans.append(val)
        val+=(val*val)/(i*i)
    return ans
# Press the green button in the gutter to run the script.
class LemmonBilliard(object):
    def __init__(self,openning):
        self.openning=openning

    def CycleTransition(self,ph,theta,expansion):
        while(((ph+2.0*theta)%(2.0*math.pi)<(2.0*math.pi-self.openning)) and ((ph+2.0*theta)%(2.0*math.pi)>self.openning)):
            ph+=2.0*theta
            ph%=2.0*math.pi
#       print([ph,theta])
        d0=math.sin(theta)
        tau0=(math.cos(self.openning)-math.cos(ph))/(-math.sin(ph+theta))
        #print(tau0)
        #print(d0)
        X1=math.sin(ph)+tau0*math.cos(ph+theta)
        #print(X1)
        #print(math.sin(self.openning))
        THETA1=(2.0*math.pi-ph-theta)%(2.0*math.pi)
        #print(THETA1)
        b_coeff=(2.0*X1*math.cos(THETA1)-2.0*math.cos(self.openning)*math.sin(THETA1))
        c_coeff=(X1*X1-math.sin(self.openning)*math.sin(self.openning))
        delta=b_coeff*b_coeff-4.0*c_coeff
        #print(delta)
        tau1=(0.5*(-1.0*b_coeff+math.sqrt(delta)))
#        print ([tau0,tau1,d0])
        expansion*=math.fabs(-1.0-(tau1+tau0-2.0*d0)/d0)
#        print(expansion)
        new_x0=X1+tau1*math.cos(THETA1)
        new_y0=-1.0*math.cos(self.openning)+tau1*math.sin(THETA1)
#        print((2.0*math.pi+math.atan2(new_y0,new_x0))%(2.0*math.pi)-1.5*math.pi)
        new_ph=(2.0*math.pi+math.atan2(new_y0,new_x0))%(2.0*math.pi)-1.5*math.pi
#        print(new_ph-THETA1)
        print(X1,new_x0*new_x0+new_y0*new_y0)
        return [new_ph,new_ph-THETA1,expansion]

if __name__ == '__main__':
    print_hi('PyCharm')
    L=LemmonBilliard(0.15)
    [z,w,u]=L.CycleTransition(0.15,0.15,1.0)
    print([z,w,u])
    [z, w, u] = L.CycleTransition(z, w, u)
    print([z,w,u])
    [z, w, u] = L.CycleTransition(z, w, u)
    print([z,w,u])
    [z, w, u] = L.CycleTransition(z, w, u)
    print([z, w, u])
    # v=harmonic(2,2)
    # ans=fun(2,0.4)
    # h=(math.pi**2)/6.0
    # print(h)
    # print(v)
    # print(ans[-1])
    # print(h-v+ans[-1])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
