import numpy as np

def mean_squared_error(y, t):
    return 0.5 * np.sum((y-t)**2)
    
def cross_entropy_error(y, t, one_hot_encode=False):
    delta = 1e-7
    # return -np.sum(t * np.log(y + delta))
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)
        
    batch_size = y.shape[0]
    if one_hot_encode:
        return -np.sum(t * np.log(y + delta)) / batch_size
    else:
        return -np.sum(np.log(y[np.arange(batch_size), t] + delta)) / batch_size
        
def numerical_diff(f, x):
    h = 1e-4
    return (f(x+h) - f(x-h)) / (2*h)
    
    
def numerical_gradient(f, x):
    h = 1e-4
    grad = np.zeros_like(x)
    
    for idx in range(x.size):
        tmp_val = x[idx]
        
        x[idx] = tmp_val + h
        fxh1 = f(x)
        
        x[idx] = tmp_val - h
        fxh2 = f(x)
        
        grad[idx] = (fxh1 - fxh2) / (2*h)
        x[idx] = tmp_val
        
    return grad
    
def gradient_descent(f, init_x, lr=.01, step_num=100):
    x = init_x
    for i in range(step_num):
        grad = numerical_gradient(f, x)
        x -= lr * grad
    return x
