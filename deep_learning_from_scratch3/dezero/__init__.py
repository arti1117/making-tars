is_simple_core = False #True

if is_simple_core:
    from dezero.core_simple import Variable
    from dezero.core_simple import Function
    from dezero.core_simple import using_config
    from dezero.core_simple import no_grad
    from dezero.core_simple import as_array
    from dezero.core_simple import as_variable
    from dezero.core_simple import setup_variable
else:
    from dezero.core import Variable
    from dezero.core import Parameter
    from dezero.core import Function
    from dezero.core import using_config
    from dezero.core import no_grad
    from dezero.core import as_array
    from dezero.core import as_variable
    from dezero.core import test_mode
    from dezero.core import setup_variable
    
    
from dezero.layers import Layer, RNN
from dezero.models import Model, MLP, VGG16
from dezero.optimizers import SGD, MomentumSGD

from dezero import datasets
from dezero.dataloaders import DataLoader

from dezero import functions as F
from dezero import functions_conv as FC
from dezero import layers as L
from dezero import utils as U

setup_variable()

