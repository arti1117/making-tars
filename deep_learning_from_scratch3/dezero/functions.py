import numpy as np
from dezero.core import Variable
from dezero.core import Function
from dezero.core import as_variable, as_array
from dezero import utils
from dezero import cuda
import dezero

class Square(Function):
    def forward(self, x):
        xp = cuda.get_array_module(x)
        return xp.power(x, 2)    
    
    def backward(self, gy):
        return 2 * self.inputs[0] * gy
      
    
class Exp(Function):
    def forward(self, x):
        xp = cuda.get_array_module(x)
        return xp.exp(x)    
    
    def backward(self, gy):
        xp = cuda.get_array_module(x)
        return xp.exp(self.inputs[0].data) * gy
    
    
class Sin(Function):
    def forward(self, x):
        xp = cuda.get_array_module(x)
        return xp.sin(x)
    
    def backward(self, gy):
        return gy * cos(self.inputs[0])
    

class Cos(Function):
    def forward(self, x):
        xp = cuda.get_array_module(x)
        return xp.cos(x)
    
    def backward(self, gy):
        return -gy * sin(self.inputs[0])


class Tanh(Function):
    def forward(self, x):
        xp = cuda.get_array_module(x)
        return xp.tanh(x)
    
    def backward(self, gy):
        y = self.outputs[0]()
        return gy * (1 - y * y)
    
    
class Softmax(Function):
    def __init__(self, axis=1):
        self.axis = axis

    def forward(self, x):
        y = x - x.max(axis=self.axis, keepdims=True)
        xp = cuda.get_array_module(x)
        y = xp.exp(y)
        y /= y.sum(axis=self.axis, keepdims=True)
        return y

    def backward(self, gy):
        y = self.outputs[0]()
        gx = y * gy
        sumdx = gx.sum(axis=self.axis, keepdims=True)
        gx -= y * sumdx
        return gx

class ReLU(Function):
    def forward(self, x):
        xp = cuda.get_array_module(x)
        return xp.maximum(x, 0.0)
    
    def backward(self, gy):
        return gy * (self.inputs[0].data > 0)
    
class Reshape(Function):
    def __init__(self, shape):
        self.shape = shape
        
    def forward(self, x):
        self.x_shape = x.shape
        return x.reshape(self.shape)
    
    def backward(self, gy):
        return reshape(gy, self.x_shape)
    
    
class Transpose(Function):
    def forward(self, x):
        xp = cuda.get_array_module(x)
        return xp.transpose(x)
    
    def backward(self, gy):
        return transpose(gy)

    
class GetItem(Function):
    def __init__(self, slices):
        self.slices = slices

    def forward(self, x):
        y = x[self.slices]
        return y

    def backward(self, gy):
        x, = self.inputs
        f = GetItemGrad(self.slices, x.shape)
        return f(gy)
    
    
class GetItemGrad(Function):
    def __init__(self, slices, in_shape):
        self.slices = slices
        self.in_shape = in_shape

    def forward(self, gy):
        xp = cuda.get_array_module(x)
        gx = xp.zeros(self.in_shape, dtype=gy.dtype)
        xp = cuda.get_array_module(x)
        xp.add.at(gx, self.slices, gy)
        return gx

    def backward(self, ggx):
        return get_item(ggx, self.slices)
    
    
class Sum(Function):
    def __init__(self, axis, keepdims):
        self.axis = axis
        self.keepdims = keepdims
    
    def forward(self, x):
        self.x_shape = x.shape
        return x.sum(axis=self.axis, keepdims=self.keepdims)
    
    def backward(self, gy):
        gy = utils.reshape_sum_backward(gy, self.x_shape, 
                                        self.axis, self.keepdims)
        return broadcast_to(gy, self.x_shape)
    
    
class BroadcastTo(Function):
    def __init__(self, shape):
        self.shape = shape
        
    def forward(self, x):
        self.x_shape = x.shape
        xp = cuda.get_array_module(x)
        return xp.broadcast_to(x, self.shape)
    
    def backward(self, gy):
        return sum_to(gy, self.x_shape)
    

class SumTo(Function):
    def __init__(self, shape):
        self.shape = shape
        
    def forward(self, x):
        self.x_shape = x.shape
        return utils.sum_to(x, self.shape)
    
    def backward(self, gy):
        return broadcast_to(gy, self.x_shape)
    

class MatMul(Function):
    def forward(self, x, W):
        return x.dot(W)
    
    def backward(self, gy):
        x, W = self.inputs
        return matmul(gy, W.T), matmul(x.T, gy)
    

class MeanSquaredError(Function):
    def forward(self, x0, x1):
        diff = x0 - x1
        return ((diff) ** 2).sum() / len(diff)
    
    def backward(self, gy):
        x0, x1 = self.inputs
        diff = x0 - x1
        gx0 = gy * diff * (2. / len(diff))
        gx1 = -gx0
        return gx0, gx1
        
        
class Linear(Function):
    def forward(self, x, W, b):
        y = x.dot(W)
        if b is not None:
            y += b
        return y

    def backward(self, gy):
        x, W, b = self.inputs
        gb = None if b.data is None else sum_to(gy, b.shape)
        gx = matmul(gy, W.T)
        gW = matmul(x.T, gy)
        return gx, gW, gb
    
    
class Sigmoid(Function):
    def forward(self, x):
        xp = cuda.get_array_module(x)
        y = xp.tanh(x * 0.5) * 0.5 + 0.5  # Better implementation
        return y

    def backward(self, gy):
        y = self.outputs[0]()
        gx = gy * y * (1 - y)
        return gx


class Clip(Function):
    def __init__(self, x_min, x_max):
        self.x_min = x_min
        self.x_max = x_max

    def forward(self, x):
        xp = cuda.get_array_module(x)
        y = xp.clip(x, self.x_min, self.x_max)
        return y

    def backward(self, gy):
        x, = self.inputs
        mask = (x.data >= self.x_min) * (x.data <= self.x_max)
        gx = gy * mask
        return gx

    
class SoftmaxCrossEntropy(Function):
    def forward(self, x, t):
        N = x.shape[0]
        log_z = utils.logsumexp(x, axis=1)
        log_p = x - log_z
        xp = cuda.get_array_module(x)
        log_p = log_p[xp.arange(N), t.ravel()]
        y = -log_p.sum() / xp.float32(N)
        return y

    def backward(self, gy):
        x, t = self.inputs
        N, CLS_NUM = x.shape

        gy *= 1/N
        y = softmax(x)
        # convert to one-hot
        xp = cuda.get_array_module(x)
        t_onehot = xp.eye(CLS_NUM, dtype=t.dtype)[t.data]
        y = (y - t_onehot) * gy
        return y



#########################################################
def numerical_diff(f, x, eps=1e-4):
    x0 = Variable(x.data - eps)
    x1 = Variable(x.data + eps)
    
    y0 = f(x0)
    y1 = f(x1)
    
    return (y1.data - y0.data) / (2 * eps)

def softmax_simple(x, axis=1):
    x = as_variable(x)
    y = exp(x)
    sum_y = sum(y, axis=axis, keepdims=True)
    return y / sum_y

def softmax_cross_entropy_simple(x, t):
    x, t = as_variable(x), as_variable(t)
    N = x.shape[0]
    
    p = softmax(x)
    p = clip(p, 1e-15, 1.0)
    log_p = log(p)
    xp = cuda.get_array_module(x)
    tlog_p = log_p[xp.arange(N), t.data]
    return -1 * sum(tlog_p) / N

def accuracy(y, t):
    y, t = as_variable(y), as_variable(t)
    
    pred = y.data.argmax(axis=1).reshape(t.shape)
    result = (pred == t.data)
    acc = result.mean()
    return Variable(as_array(acc))

def square(x):
    return Square()(x)  

def exp(x):
    return Exp()(x)

def sin(x):
    return Sin()(x)

def cos(x):
    return Cos()(x)

def tanh(x):
    return Tanh()(x)

def softmax(x, axis=1):
    return Softmax(axis)(x)

def relu(x):
    return ReLU()(x)

def reshape(x, shape):
    if x.shape == shape:
        return as_variable(x)
    return Reshape(shape)(x)

def transpose(x):
    return Transpose()(x)

def get_item(x, slices):
    f = GetItem(slices)
    return f(x)

def sum(x, axis=None, keepdims=False):
    return Sum(axis, keepdims)(x)

def broadcast_to(x, shape):
    if x.shape == shape:
        return as_variable(x)
    return BroadcastTo(shape)(x)

def sum_to(x, shape):
    if x.shape == shape:
        return as_variable(x)
    return SumTo(shape)(x)

def matmul(x, W):
    return MatMul()(x, W)

def mean_squared_error(x0, x1):
    return MeanSquaredError()(x0, x1)

def linear(x, W, b=None):
    return Linear()(x, W, b)

def linear_simple(x, W, b=None):
    t = matmul(x, W)
    if b is None:
        return t
    y = t + b
    t.data = None
    return y

def sigmoid(x):
    return Sigmoid()(x)

def sigmoid_simple(x):
    x = as_variable(x)
    return 1 / (1 + exp(-x))

def clip(x, x_min, x_max):
    return Clip(x_min, x_max)(x)

def softmax_cross_entropy(x, t):
    return SoftmaxCrossEntropy()(x, t)

def dropout(x, dropout_ratio=0.5):
    x = as_variable(x)
    
    if dezero.core.Config.train:
        xp = cuda.get_array_module(x)
        mask = xp.random.rand(*x.shape) > dropout_ratio
        scale = xp.array(1.0 - dropout_ratio).astype(x.dtype)
        return x * mask / scale
    else:
        return x

    
from dezero.functions_conv import conv2d
from dezero.functions_conv import deconv2d
from dezero.functions_conv import conv2d_simple
from dezero.functions_conv import im2col
from dezero.functions_conv import col2im
from dezero.functions_conv import pooling_simple
from dezero.functions_conv import pooling
from dezero.functions_conv import average_pooling