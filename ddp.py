import numpy as np
from scipy import optimize as opt
class ddp:
    def __init__(self,f,p,sigma,T,v):
        self.f = f
        self.p = p
        self.sigma = sigma
        self.T = T
        self.v = v
        
    def compute():
        v_f = lambda x : self.f(x)+ self.sigma*self.p(x)*v_old
        return opt.fsolve(v_f,0)
    def solve():
        self.X=np.zeros(self.T)
        v_old= self.v
        for i in range(self.T):
            if i = self.T-1:
                X[-(k+1)]= v_old
                break
            else:
                X[-(k+1)]= v_old
                v_new = compute()
                v_old = v_new 
            
            