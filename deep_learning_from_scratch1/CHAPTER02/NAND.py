import numpy as np

def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-.5, -.5])
    b = .7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


