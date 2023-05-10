'''Solver for the 1D diffusion equation. '''
import numpy as np


np.set_printoptions(formatter={'float': '{: 6.1f}'.format})

def solve1d(conc,spacing,t_step,diffusivity):
    flux = -diffusivity * np.diff(conc) / spacing
    conc[1:-1] -= t_step * np.diff(flux) / spacing
    
    return conc
    
def _example():
    D = 100
    Lx = 5
    dx = 0.5
    x = np.arange(0,Lx,step=dx)
    C1 = 500
    C2 = 0
    C= np.array([C1 if i < Lx/2 else C2 for i in x]).astype('float64')
    dt = dx * dx / D /2.1
    
    print(C)
    for _ in range(1,5):
        C = solve1d(C,dx,dt,D)
        print(C)
    
if __name__ == '__main__':
    _example()