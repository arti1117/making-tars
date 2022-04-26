import numpy as np

def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([.5, .5])
    b = -.2
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


