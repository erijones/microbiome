#!/bin/python

import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt

# ODE for single microbe + nutrients
# Y = [microbe concentration; nutrient concentration]
def integrand(Y, t, gamma = 2, mu = .2, K = 2, beta = 1, N0 = 1):
    return [ (gamma*Y[1]/(Y[1] + K) - mu)*Y[0],
             -1*(gamma*Y[1]/(Y[1] + K) - mu)*Y[0] ] #+ beta*(N0 - Y[1]) ]

# solve ODE with initial condition ic
def solve(ic, *params):
    (t0, t_end) = 0, 10 
    t = np.linspace(t0, t_end, num=1000)
    y = integrate.odeint(integrand, [ic[0], ic[1]], t, args = params)
    return t, y

def plot(t, y):
    plt.figure()
    plt.subplot(2,1,1)
    plt.plot(t, y[:,0])
    plt.ylabel('Microbe Concentration')
    plt.xlabel('$t$')
    plt.subplot(2,1,2)
    plt.ylabel('Nutrient Concentration')
    plt.xlabel('$t$')
    plt.plot(t, y[:,1])
    plt.tight_layout()
    #plt.show()
    plt.savefig('one_microbe.pdf', bbox_inches='tight')

if __name__ == '__main__':
    params = [1, .2, 2]
    t, y = solve([1, 1], *params)
    plot(t, y)
    print('a')


#params = [4, 5, 8]
#print(integrand([1, 2], *params))
