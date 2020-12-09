#run pip install numpy==1.19.3, current version is 1.19.4 but gives runtime issue
import numpy as np

def bezPatch(u,v):
    buA = (1 - u)**2
    buB = 2*u*(1-u)
    buC = u**2
    bvA = (1 - v)**2
    bvB = 2*v*(1-v)
    bvC = v**2
    #M^T Matrix
    M = [buA, buB, buC]
    #N Matrix
    N = [bvA, bvB, bvC]
    #B1 - 3 = first column vectors
    B1 = np.array([0, 0, 6])
    B2 = np.array([0, 3, 3])
    B3 = np.array([0, 6, 6])
    #B4 - 6 = second column vectors
    B4 = np.array([3, 0, 0])
    B5 = np.array([3, 3, 0])
    B6 = np.array([3, 6, 0])
    #B7 - 9 = third column vectors
    B7 = np.array([6, 0, 0])
    B8 = np.array([6, 3, 0])
    B9 = np.array([6, 6, 0])
    #M^T * B
    R10 = M[0] * B1
    R11 = M[0] * B4
    R12 = M[0] * B7
    R20 = M[1] * B2
    R21 = M[1] * B5
    R22 = M[1] * B8
    R30 = M[2] * B3
    R31 = M[2] * B6
    R32 = M[2] * B9
    #Add Corresponding Columns
    C0 = R10 + R20 + R30
    C1 = R11 + R21 + R31
    C2 = R12 + R22 + R32
    #Multiply by N
    Res = C0*N[0] + C1*N[1] + C2*N[2]
    return Res
    
print(bezPatch(0.4, 0.95));
