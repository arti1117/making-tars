import numpy as np

def softmax(a):
    c = np.max(a)
    e = np.exp(a - c)
    s = np.sum(e)
    
    return e / s
    
